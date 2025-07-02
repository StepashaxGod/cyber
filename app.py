# for web server and to work with. db 

from flask import Flask, request, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy

# to securely hash passwords
from werkzeug.security import generate_password_hash, check_password_hash

# to generate keys and cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# standard modules
import base64
import secrets
import string
import os

# app settings and database 
# secret key for sessions, sqllite setup, sqlAlchemy initialisation to work with db
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passwords.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# model for the user authentication and security during login, registration 
# id, usernmae, password_hash, salt
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    salt = db.Column(db.LargeBinary, nullable=False)

# model for securily adding encrypted passwords with corresponding websites
# id, user_id, site, username, encrypted_password(through the key) 
class PasswordEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    site = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    encrypted_password = db.Column(db.LargeBinary, nullable=False)



print("DB path:", os.path.abspath('passwords.db'))

# encryption functions
def derive_key(password, salt):
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

#
def encrypt_password(key, password):
    return Fernet(key).encrypt(password.encode())

def decrypt_password(key, encrypted_password):
    return Fernet(key).decrypt(encrypted_password).decode()

# 12 digit random password 
def generate_password():
    return ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12))

# routes
@app.route('/')
def index():
    # checks authorisation 
    if 'user_id' not in session:
        return redirect(url_for('login'))
    # takes all the passwords from the db of user 
    entries = PasswordEntry.query.filter_by(user_id=session['user_id']).all()
    key = session.get('key')
    if not key:
        flash('Session expired. Please log in.')
        return redirect(url_for('login'))
    decrypted_entries = []
    # shows in a table 
    for entry in entries:
        try:
            decrypted_entries.append({
                'site': entry.site,
                'username': entry.username,
                'password': decrypt_password(key, entry.encrypted_password) # decryption for the ui 
            })
        except:
            flash('Error decrypting passwords.')
    return render_template('index.html', entries=decrypted_entries)

# registration, the route: "/register"
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # validating length 
        if len(username) < 4 or len(password) < 8:
            flash('Username must be 4+ chars, password 8+.')
            return render_template('register.html')
        
        # validating uniquness 
        if User.query.filter_by(username=username).first():
            flash('Username taken.')
            return render_template('register.html')
         
        salt = secrets.token_bytes(16) # need salt to generate seesion key 
        password_hash = generate_password_hash(password) # store hash, to validate user password

        #storing username, password_hash, salt
        user = User(username=username, password_hash=password_hash, salt=salt)
        db.session.add(user)
        db.session.commit()
        flash('Registered! Please log in.')
        return redirect(url_for('login'))
    
    # GET request for the form
    return render_template('register.html')
 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # server looking for user
        user = User.query.filter_by(username=username).first()

        # if user if password == hash
        if user and check_password_hash(user.password_hash, password):

            # place the userid into session - thats authorisation
            session['user_id'] = user.id
            
            # create key and put into session
            session['key'] = derive_key(password, user.salt)
            flash('Logged in!')
            # user is shown the page with decrypted passwords with the session keye
            return redirect(url_for('index'))
        flash('Invalid credentials.')
    # GET request
    return render_template('login.html')

# logs out from the account, deletes data from session
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('key', None)
    flash('Logged out.')
    return redirect(url_for('login'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    generated = request.args.get('generate')
    if request.method == 'POST':
        site = request.form['site'][:100]
        username = request.form['username'][:100]
        password = request.form['password']
        if not (site and username and password):
            flash('All fields required.')
            return render_template('add.html', generated=generated)
        key = session.get('key')
        if not key:
            flash('Session expired. Please log in.')
            return redirect(url_for('login'))
        encrypted_password = encrypt_password(key, password)
        entry = PasswordEntry(user_id=session['user_id'], site=site, username=username, encrypted_password=encrypted_password)
        db.session.add(entry)
        db.session.commit()
        flash('Password saved!')
        return redirect(url_for('index'))
    return render_template('add.html', generated=generated)

# generate a random password and go to page 
@app.route('/generate')
def generate():
    return redirect(url_for('add', generate=generate_password()))

# create database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)