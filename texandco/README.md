# Tex & Co - Textile Marketplace

A modern, Docker-compatible textile marketplace platform built with HTML5, CSS3, JavaScript, and Node.js.

## Project Structure

```
texandco/
├── frontend/               # React-based frontend application
│   ├── index.html         # Main HTML file
│   ├── styles.css         # Styling
│   ├── app.js             # JavaScript logic
│   ├── Dockerfile         # Frontend container config
│   └── .dockerignore      # Docker ignore rules
├── backend/               # Node.js Express API
│   ├── app/
│   │   └── server.js      # Main server file
│   ├── package.json       # Dependencies
│   ├── .env               # Environment variables
│   ├── Dockerfile         # Backend container config
│   ├── .dockerignore      # Docker ignore rules
│   └── API.md             # API documentation
├── docker-compose.yml     # Docker orchestration
└── README.md             # This file
```

## Technology Stack

**Frontend:**
- HTML5
- CSS3 (Custom Design System)
- Vanilla JavaScript
- Responsive Mobile-first Design

**Backend:**
- Node.js
- Express.js
- CORS enabled
- RESTful API

**DevOps:**
- Docker
- Docker Compose
- Multi-stage builds
- Health checks

## Features

- 📱 **Responsive Design** - Mobile-optimized textile marketplace
- 🧵 **Product Catalog** - Browse fabric inventory
- 🛒 **Shopping Cart** - Add/remove fabrics
- 📦 **Order Management** - Track orders
- 👤 **Seller Dashboard** - Inventory management
- 🔍 **Search & Filter** - Find fabrics by type, color, GSM
- 💫 **Smooth Animations** - Polished UX with transitions

## Quick Start

### Prerequisites
- Docker (v20.10+)
- Docker Compose (v1.29+)

### Using Docker Compose (Recommended)

```bash
# Navigate to project root
cd texandco

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

Access the application:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000/api

### Manual Setup

**Frontend:**
```bash
cd frontend
npx http-server . -p 3000 --gzip
```

**Backend:**
```bash
cd backend
npm install
npm start
```

## API Endpoints

### Products
- `GET /api/products` - Get all fabrics
- `GET /api/products/:id` - Get specific fabric

### Orders
- `GET /api/orders` - Get all orders
- `POST /api/orders` - Create new order

### Health
- `GET /api/health` - Server health check

See [backend/API.md](backend/API.md) for detailed API documentation.

## Environment Variables

**Backend (.env):**
```
PORT=5000
NODE_ENV=production
API_URL=http://localhost:5000
```

## Docker Commands

```bash
# Build images
docker-compose build

# Run containers
docker-compose up

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop containers
docker-compose stop

# Remove containers
docker-compose down

# Remove volumes
docker-compose down -v

# Rebuild specific service
docker-compose build --no-cache frontend
```

## Development

### Frontend Development
```bash
cd frontend
# Edit index.html, styles.css, app.js
# Changes reflect immediately with http-server
```

### Backend Development
```bash
cd backend
npm install
npm run dev  # Uses nodemon for auto-reload
```

## Production Deployment

For production, update environment variables:
```yaml
# docker-compose.yml
environment:
  - REACT_APP_API_URL=https://api.yourdomain.com
  - NODE_ENV=production
  - CORS_ORIGIN=https://yourdomain.com
```

## Performance Optimizations

- ✅ Multi-stage Docker builds for smaller images
- ✅ Health checks for auto-restart
- ✅ Volume mounts for development
- ✅ Network isolation with bridge network
- ✅ Minified CSS/JavaScript
- ✅ Lazy loading components

## Troubleshooting

**Backend not connecting:**
```bash
docker-compose logs backend
```

**Frontend not loading:**
```bash
docker-compose logs frontend
```

**Port already in use:**
```bash
# Change ports in docker-compose.yml
ports:
  - "8080:3000"  # Map to different port
```

**Clear all containers:**
```bash
docker-compose down -v
docker system prune -a
```

## License

ISC

## Author

Tex & Co Team

---

**Last Updated:** March 2026
