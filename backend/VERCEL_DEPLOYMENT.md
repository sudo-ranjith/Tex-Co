# Vercel Deployment Guide

## Backend Setup (Vercel Serverless)

The backend is now configured for Vercel serverless functions:

```
api/
├── health.js      → GET /api/health
├── products.js    → GET /api/products, GET /api/products?id=p1
├── orders.js      → GET /api/orders, POST /api/orders
└── cart.js        → POST /api/cart
```

## How to Deploy

1. **Install Vercel CLI**
```bash
npm install -g vercel
```

2. **From the backend directory, deploy:**
```bash
cd backend
vercel --prod
```

3. **Get your Vercel URL** (will be something like `https://texandco-backend.vercel.app`)

4. **Update frontend API calls** to new URL:
   - Replace `http://localhost:5000` with your Vercel URL
   - In `frontend/app.js`, update API_BASE if used

## API Endpoints

**Production (Vercel):**
- Health: `https://your-project.vercel.app/api/health`
- Products: `https://your-project.vercel.app/api/products`
- Orders: `https://your-project.vercel.app/api/orders`
- Cart: `https://your-project.vercel.app/api/cart`

**Local Development:**
- Health: `http://localhost:5000/api/health`
- Products: `http://localhost:5000/api/products`
- Orders: `http://localhost:5000/api/orders`
- Cart: `http://localhost:5000/api/cart`

## Environment Variables

Create `.env` file in backend:
```
NODE_ENV=production
```

## Notes

- All endpoints support CORS
- Serverless functions scale automatically
- No manual server management needed
- Cold start time: ~1-2 seconds initially
