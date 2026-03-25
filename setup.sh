#!/bin/bash

# Development setup script for Tex & Co

echo "🐳 Tex & Co - Docker Setup"
echo "=========================="

# Check Docker installation
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker and Docker Compose found"

# Build images
echo ""
echo "📦 Building Docker images..."
docker-compose build

# Start services
echo ""
echo "🚀 Starting services..."
docker-compose up -d

# Wait for services to be ready
echo ""
echo "⏳ Waiting for services to be ready..."
sleep 5

# Check health
echo ""
echo "🏥 Checking service health..."

if curl -f http://localhost:3000/index.html > /dev/null 2>&1; then
    echo "✅ Frontend is running at http://localhost:3000"
else
    echo "⚠️  Frontend might not be ready yet"
fi

if curl -f http://localhost:5000/api/health > /dev/null 2>&1; then
    echo "✅ Backend is running at http://localhost:5000/api"
else
    echo "⚠️  Backend might not be ready yet"
fi

echo ""
echo "✨ Setup complete!"
echo ""
echo "📱 Frontend: http://localhost:3000"
echo "🔌 Backend API: http://localhost:5000/api"
echo ""
echo "View logs with: docker-compose logs -f"
echo "Stop services with: docker-compose down"
