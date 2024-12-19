#!/bin/bash

# Update pip and install Poetry
echo "Updating pip..."
pip install --upgrade pip

# Install Poetry (if not already installed)
echo "Installing Poetry..."
if ! command -v poetry &> /dev/null
then
    curl -sSL https://install.python-poetry.org | python3 -
fi

# Dynamically add Poetry to PATH (handles different user paths)
POETRY_BIN_PATH="$HOME/.local/bin"
if [ -d "$POETRY_BIN_PATH" ]; then
    export PATH="$POETRY_BIN_PATH:$PATH"
fi

# Install system dependencies for PyAudio (PortAudio libraries)
echo "Installing system dependencies for PyAudio..."
sudo apt-get update
sudo apt-get install -y portaudio19-dev

# Install dependencies using Poetry
echo "Installing dependencies using Poetry..."
poetry install

# Install Streamlit (if not already installed)
echo "Installing Streamlit..."
if ! command -v streamlit &> /dev/null
then
    pip install streamlit
fi
