
# 🚀 How to Start the Cyber Password Manager Project

Follow these steps to get the Cyber project up and running on your machine.

---

## ✅ Requirements

clone repo and navigate to a file

```bash
https://github.com/StepashaxGod/cyber.git
cd path/to/cyber
```

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
