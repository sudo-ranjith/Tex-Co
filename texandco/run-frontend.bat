@echo off
REM Simple frontend server for local development - Windows

echo 🌐 Starting Tex & Co Frontend...
echo.

REM Check if node/npm is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js is not installed!
    echo 📥 Download from: https://nodejs.org/
    exit /b 1
)

echo ✅ Node.js found
echo.

REM Check if http-server is installed globally
npx http-server --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 📦 Installing http-server...
    npm install -g http-server
)

echo.
echo 🚀 Starting server on port 3000...
echo.
echo 📱 Open browser: http://localhost:3000
echo 🛑 Press Ctrl+C to stop
echo.

REM Start the server from frontend directory
cd /d "%~dp0frontend"
npx http-server . -p 3000 -o index.html

pause
