#!/usr/bin/env bash

echo "Setting up virtual environment and installing dependencies..."
python3 -m venv venv
source venv/bin/activate
pip install flask flask-sqlalchemy cryptography werkzeug
echo "Dependencies installed."
echo "Virtual environment activated. Execute "source venv/bin/activate" and run app.py"
