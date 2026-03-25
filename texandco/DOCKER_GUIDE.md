# Tex & Co - Docker Deployment Guide

## Overview

This guide covers deploying Tex & Co using Docker and Docker Compose for both development and production environments.

## Prerequisites

### Windows
1. Install [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)
2. Enable WSL 2 (Windows Subsystem for Linux)
3. Run `setup.bat` or use Command Prompt

### Mac
1. Install [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/)
2. Run `chmod +x setup.sh && ./setup.sh`

### Linux
1. Install Docker:
   ```bash
   sudo apt-get update
   sudo apt-get install docker.io docker-compose
   ```
2. Run `chmod +x setup.sh && ./setup.sh`

## Quick Start

### Option 1: Automated Setup (Recommended)

**Windows:**
```bash
setup.bat
```

**Mac/Linux:**
```bash
bash setup.sh
```

### Option 2: Manual Setup

```bash
# Navigate to project root
cd texandco

# Build images
docker-compose build

# Start services
docker-compose up -d

# Check logs
docker-compose logs -f
```

## Accessing the Application

Once containers are running:

- **Frontend Application**: http://localhost:3000
- **Backend API**: http://localhost:5000/api
- **API Health Check**: http://localhost:5000/api/health

## Docker Compose Commands

### Start Services
```bash
# Start in background
docker-compose up -d

# Start with logs
docker-compose up
```

### View Logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f frontend
docker-compose logs -f backend
```

### Stop Services
```bash
# Stop (containers remain)
docker-compose stop

# Stop and remove (clean slate)
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

### Rebuild Services
```bash
# Rebuild all
docker-compose build

# Rebuild without cache
docker-compose build --no-cache

# Rebuild specific service
docker-compose build frontend
```

### Execute Commands in Container
```bash
# Frontend shell
docker-compose exec frontend sh

# Backend shell
docker-compose exec backend sh

# Run npm command
docker-compose exec backend npm run dev
```

## Development Workflow

### Frontend Development
```bash
# Edit files in frontend/ directory
# Changes are live with http-server

# To rebuild frontend image
docker-compose build frontend
```

### Backend Development
```bash
# With hot-reload (via nodemon)
docker-compose exec backend npm run dev

# View backend logs
docker-compose logs -f backend
```

### Testing API Endpoints
```bash
# Test health check
curl http://localhost:5000/api/health

# Get all products
curl http://localhost:5000/api/products

# Get specific product
curl http://localhost:5000/api/products/p1

# Get all orders
curl http://localhost:5000/api/orders
```

## Production Deployment

### Environment Configuration
Create `.env.production` for production settings:

```env
PORT=5000
NODE_ENV=production
CORS_ORIGIN=https://yourdomain.com
```

### Update docker-compose.yml
```yaml
environment:
  - REACT_APP_API_URL=https://api.yourdomain.com
  - NODE_ENV=production
  - CORS_ORIGIN=https://yourdomain.com
```

### Deploy to Server
```bash
# Clone repository
git clone <repo-url>
cd texandco

# Build for production
docker-compose -f docker-compose.yml build

# Start services
docker-compose up -d

# Verify
docker-compose ps
```

### Using Docker Swarm (Optional)
```bash
docker swarm init
docker stack deploy -c docker-compose.yml texandco
```

### Using Kubernetes (Optional)
```bash
# Install kubectl and Helm
# Create deployment manifests in k8s/ directory
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/backend-deployment.yaml
```

## Troubleshooting

### Port Already in Use
```bash
# Find process using port 3000
lsof -i :3000  # Mac/Linux
netstat -ano | findstr :3000  # Windows

# Change port in docker-compose.yml
ports:
  - "8080:3000"
```

### Container Won't Start
```bash
# Check logs
docker-compose logs backend

# Rebuild image
docker-compose build --no-cache backend

# Start with verbose output
docker-compose up frontend backend
```

### API Not Responding
```bash
# Check backend health
curl -v http://localhost:5000/api/health

# Check container status
docker-compose ps

# Restart backend
docker-compose restart backend
```

### Clear Everything
```bash
# Remove all containers, images, and volumes
docker-compose down -v
docker system prune -a --volumes

# Rebuild from scratch
docker-compose build --no-cache
docker-compose up -d
```

## Performance Tips

1. **Use volume mounts for development:**
   ```yaml
   volumes:
     - ./backend:/app
     - /app/node_modules
   ```

2. **Enable Docker's experimental features:**
   - Open Docker Desktop Settings
   - Enable "Use Docker Compose v2"

3. **Resource Limits:**
   ```yaml
   services:
     backend:
       deploy:
         resources:
           limits:
             cpus: '0.5'
             memory: 512M
   ```

## Monitoring

### View Container Status
```bash
docker-compose ps

# With resource usage
docker stats
```

### View Logs
```bash
# Real-time logs
docker-compose logs -f

# Last 100 lines
docker-compose logs --tail=100
```

### Health Checks
Both services have health checks configured:
```bash
# Check specific service
docker inspect texandco-backend | grep -A 5 Health
```

## Cleanup

### Remove Services
```bash
docker-compose down
```

### Remove All Docker Resources
```bash
docker system prune -a --volumes
```

### Remove Specific Images
```bash
docker rmi texandco-frontend texandco-backend
```

## Advanced Topics

### Custom Networks
Services communicate via `texandco-network` bridge network.

### Volume Management
- Frontend: static files
- Backend: application code and node_modules

### Environment Variables
Set in `.env` files or docker-compose.yml:
```yaml
environment:
  - PORT=5000
  - NODE_ENV=production
```

## Support

For issues:
1. Check logs: `docker-compose logs -f`
2. Verify Docker installation: `docker --version`
3. Check port availability: `docker ps`
4. Review docker-compose.yml syntax

## References

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Reference](https://docs.docker.com/compose/compose-file/)
- [Express.js Guide](https://expressjs.com/en/guide/routing.html)
- [Best Practices](https://docs.docker.com/develop/dev-best-practices/)
