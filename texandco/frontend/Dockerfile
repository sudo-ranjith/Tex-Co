# Frontend Dockerfile - Multi-stage build
FROM node:18-alpine AS builder

WORKDIR /app

# Copy static files
COPY . .

# Install a simple HTTP server for production
RUN npm init -y && npm install --save-dev http-server

# Production stage
FROM node:18-alpine

WORKDIR /app

# Copy node_modules and app from builder
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/*.html ./
COPY --from=builder /app/*.css ./
COPY --from=builder /app/*.js ./

EXPOSE 3000

HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --quiet --tries=1 --spider http://localhost:3000/ || exit 1

# Start the application  
CMD ["npx", "http-server", ".", "-p", "3000", "--gzip", "-c-1"]
