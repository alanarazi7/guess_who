#!/bin/bash

# Update pip and install poetry
echo "Updating pip..."
pip install --upgrade pip

# Install Poetry (if not already installed)
echo "Installing Poetry..."
if ! command -v poetry &> /dev/null
then
    curl -sSL https://install.python-poetry.org | python3 -
fi

# Install dependencies using Poetry (you can adjust this for pip if needed)
echo "Installing dependencies using Poetry..."
poetry install

# Alternatively, use pip if you have a requirements.txt
# pip install -r requirements.txt

# Run Streamlit app
echo "Starting Streamlit app..."
streamlit run demo.py
