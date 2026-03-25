#!/bin/bash
# Quick Start Script for Tex & Co - Python Backend
# Mac/Linux Shell Script

echo ""
echo "============================================"
echo "  Tex & Co - Python FastAPI Quick Start"
echo "============================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 not found!"
    echo "Please install Python 3.11+ from https://www.python.org/"
    echo ""
    exit 1
fi

echo "✓ Python found"
python3 --version
echo ""

# Navigate to backend directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"
echo "Current directory: $(pwd)"
echo ""

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "ERROR: requirements.txt not found!"
    echo "Make sure you're in the backend directory."
    exit 1
fi

echo "✓ requirements.txt found"
echo ""

# Create or activate virtual environment
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies!"
    exit 1
fi
echo "✓ Dependencies installed"
echo ""

# Run the server
echo ""
echo "============================================"
echo "   Starting FastAPI Server"
echo "============================================"
echo ""
echo "🚀 Server starting..."
echo ""
echo "✓ API will be available at: http://localhost:8000"
echo "✓ Swagger UI (docs): http://localhost:8000/docs"
echo "✓ ReDoc: http://localhost:8000/redoc"
echo ""
echo "Press CTRL+C to stop the server"
echo ""

python main.py
