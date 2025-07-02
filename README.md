
# 🚀 How to Start the Cyber Password Manager Project

Follow these steps to get the Cyber project up and running on your machine.

---

## ✅ Requirements
through terminal
clone repo and navigate to a file

```bash
git clone https://github.com/StepashaxGod/cyber.git
cd path/to/cyber
```

Make sure you have **Python 3** installed:

```bash
python --version
# or
python3 --version
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
Presents in video for the sake of clarity.

To inspect the SQLite database:

1. Download **DB Browser for SQLite**:  
   [https://sqlitebrowser.org/](https://sqlitebrowser.org/)

open the file in /cyber

```
open instance/passwords.db
```

Enjoy your secure password manager! 🔐
