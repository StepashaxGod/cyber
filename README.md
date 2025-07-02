How to start the project?

make sure u have python available:
python --version
or
python3 --version

Prepare project folder
• Put your entire project folder (with app.py, templates folder, etc.) somewhere convenient.

go fo the cyber folder
cd path/to/cyber

make the setup.sh an executable
chmod +x setup.sh

run the environment
./setup.sh

then activate the it
source venv/bin/activate

and finally run the python app.py

for more visualisation u can download the DB browser for sqllite to see the tables and data.
download from (https://sqlitebrowser.org/)

navigate towards the file/to/cyber

and finally
open instance/passwords.db

# 🚀 How to Start the Cyber Password Manager Project

Follow these steps to get the Cyber project up and running on your machine.

---

## ✅ Requirements

Make sure you have **Python 3** installed:

```bash
python --version
# or
python3 --version
```

---

## 📁 Set Up the Project Folder

1. Place your entire project folder (including `app.py`, `templates/`, `setup.sh`, etc.) in a convenient location.
2. Open a terminal and navigate into the project folder:

```bash
cd path/to/cyber
```

---

## ⚙️ Run the Setup Script

1. Make the `setup.sh` script executable:

```bash
chmod +x setup.sh
```

2. Run the setup script:

```bash
./setup.sh
```

This will:

- Create a virtual environment
- Activate it
- Install all necessary dependencies

---

## 🧠 Activate the Virtual Environment (if not already active)

```bash
source venv/bin/activate
```

---

## 🖥️ Run the App

```bash
python app.py
```

Your app should now be running at:

```
http://127.0.0.1:5000
```

---

## 📊 Visualize the Database (Optional)

To inspect the SQLite database:

1. Download **DB Browser for SQLite**:  
   [https://sqlitebrowser.org/](https://sqlitebrowser.org/)

2. In the browser, open the file:

```
instance/passwords.db
```

Here you can view tables, data, and structure visually.

---

Enjoy your secure password manager! 🔐
