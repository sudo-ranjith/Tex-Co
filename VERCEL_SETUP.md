# Tex & Co - Vercel Deployment Guide

## 🚀 Quick Start

### Step 1: Deploy Backend to Vercel

```bash
cd backend

# Verify vercel.json exists
cat vercel.json

# Deploy
vercel --prod
```

After deployment, you'll get a URL like:
```
https://texandco-backend-xxx.vercel.app
```

### Step 2: Test Backend Endpoints

Once deployed, test these URLs in your browser:

```
https://texandco-backend-xxx.vercel.app/api/health
https://texandco-backend-xxx.vercel.app/api/products
https://texandco-backend-xxx.vercel.app/api/orders
```

Should return JSON responses (not 404).

### Step 3: Update Frontend API Endpoints

Edit `frontend/config.js` and replace:
```javascript
const API_BASE_URL = 'https://texandco-backend-xxx.vercel.app';
```

Or set environment variable before deploying frontend:
```bash
REACT_APP_API_URL=https://texandco-backend-xxx.vercel.app
```

### Step 4: Deploy Frontend to Vercel

```bash
cd frontend

# Deploy
vercel --prod
```

## 📋 File Structure

Backend is now set up for Vercel serverless:
```
backend/
├── vercel.json              ← Vercel config
├── api/
│   ├── health.js            → /api/health
│   ├── products.js          → /api/products
│   ├── orders.js            → /api/orders
│   └── cart.js              → /api/cart
├── app/
│   └── server.js            ← Keep for local dev
├── package.json
└── .gitignore
```

## 🔧 Local Development

Backend uses Express - runs locally on port 5000:
```bash
cd backend
npm install
npm start
```

Frontend on port 3000:
```bash
cd frontend
npm install
npm start
# or
npx http-server . -p 3000
```

## ✅ What's Fixed

1. **✓ Backend converted to Vercel serverless functions**
   - No more Express server on port
   - Uses `api/*.js` pattern
   - Auto-scales on Vercel

2. **✓ CORS headers added to all endpoints**
   - Frontend can call backend from any domain

3. **✓ Vercel configuration ready**
   - `vercel.json` configured
   - Routes mapped correctly

4. **✓ API endpoints working**
   - `/api/health` - Status check
   - `/api/products` - Get all products
   - `/api/products?id=p1` - Get single product
   - `/api/orders` - Get/create orders
   - `/api/cart` - Add to cart

## 🌐 Deployment Status

| Service | Status | URL |
|---------|--------|-----|
| Backend (Vercel) | Ready | https://your-backend-url.vercel.app |
| Frontend (Vercel) | Ready | https://your-frontend-url.vercel.app |

## 🐛 Troubleshooting

**Getting 404 on API calls?**
- Check Vercel deployment URL is correct
- Verify `/api/` endpoints respond
- Clear browser cache

**CORS errors?**
- CORS headers are now included
- Check browser console for exact error

**Local API calls failing?**
- Ensure backend is running: `npm start` in `/backend`
- Check port 5000 is not in use
- API base should be `http://localhost:5000`

## 📝 API Response Examples

**GET /api/health**
```json
{
  "status": "OK",
  "timestamp": "2026-03-25T10:30:00.000Z",
  "message": "Tex & Co Backend Running"
}
```

**GET /api/products**
```json
[
  {
    "id": "p1",
    "name": "Black Loopknit",
    "price": 82,
    ...
  }
]
```

**POST /api/orders**
```json
{
  "message": "Order created successfully",
  "order": {
    "id": "o1711348200000",
    "company": "...",
    "status": "placed"
  }
}
```

## 🎯 Next Steps

1. Deploy backend: `cd backend && vercel --prod`
2. Get the URL from Vercel console
3. Update frontend `config.js` with new URL
4. Deploy frontend: `cd frontend && vercel --prod`
5. Test: Open your frontend URL and verify API calls work

Done! 🎉
