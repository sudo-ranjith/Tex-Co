@echo off
REM Quick Start Script for Tex & Co - Python Backend
REM Windows Batch Script

echo.
echo ============================================
echo   Tex & Co - Python FastAPI Quick Start
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Please install Python 3.11+ from https://www.python.org/
    echo.
    pause
    exit /b 1
)

echo ✓ Python found
python --version
echo.

REM Navigate to backend directory
cd /d "%~dp0"
echo Current directory: %cd%
echo.

REM Check if requirements.txt exists
if not exist "requirements.txt" (
    echo ERROR: requirements.txt not found!
    echo Make sure you're in the backend directory.
    pause
    exit /b 1
)

echo ✓ requirements.txt found
echo.

REM Create or activate virtual environment
if not exist "venv" (
    echo Creating Python virtual environment...
    python -m venv venv
    echo ✓ Virtual environment created
) else (
    echo ✓ Virtual environment already exists
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo ✓ Virtual environment activated
echo.

REM Install dependencies
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies!
    pause
    exit /b 1
)
echo ✓ Dependencies installed
echo.

REM Run the server
echo.
echo ============================================
echo   Starting FastAPI Server
echo ============================================
echo.
echo 🚀 Server starting...
echo.
echo ✓ API will be available at: http://localhost:8000
echo ✓ Swagger UI (docs): http://localhost:8000/docs
echo ✓ ReDoc: http://localhost:8000/redoc
echo.
echo Press CTRL+C to stop the server
echo.

python main.py

pause
