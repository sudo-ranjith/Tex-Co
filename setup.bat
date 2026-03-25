@echo off
REM Windows setup script for Tex & Co

echo.
echo 🐳 Tex ^& Co - Docker Setup
echo ==========================

REM Check Docker installation
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker is not installed. Please install Docker Desktop first.
    exit /b 1
)

docker-compose --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker Compose is not installed. Please update Docker Desktop.
    exit /b 1
)

echo ✅ Docker and Docker Compose found
echo.

REM Build images
echo 📦 Building Docker images...
docker-compose build

REM Start services
echo.
echo 🚀 Starting services...
docker-compose up -d

REM Wait for services to be ready
echo.
echo ⏳ Waiting for services to be ready...
timeout /t 5 /nobreak

REM Check health
echo.
echo 🏥 Checking service health...

powershell -Command "(New-Object Net.WebClient).DownloadString('http://localhost:3000/index.html')" >nul 2>&1 && (
    echo ✅ Frontend is running at http://localhost:3000
) || (
    echo ⚠️  Frontend might not be ready yet
)

powershell -Command "(New-Object Net.WebClient).DownloadString('http://localhost:5000/api/health')" >nul 2>&1 && (
    echo ✅ Backend is running at http://localhost:5000/api
) || (
    echo ⚠️  Backend might not be ready yet
)

echo.
echo ✨ Setup complete!
echo.
echo 📱 Frontend: http://localhost:3000
echo 🔌 Backend API: http://localhost:5000/api
echo.
echo View logs with: docker-compose logs -f
echo Stop services with: docker-compose down
