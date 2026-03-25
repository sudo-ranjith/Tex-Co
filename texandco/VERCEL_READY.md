# ✅ Vercel Deployment Checklist

## 🔧 Before Deploying - Fix These Issues

### ✅ Issues Fixed:

1. **Frontend Vercel Configuration**
   - ✓ Created `frontend/vercel.json` for static deployment
   - ✓ Configured SPA routing (all routes go to index.html)
   - ✓ Added `.vercelignore` to exclude unnecessary files

2. **Backend Vercel Configuration**
   - ✓ Enhanced `backend/vercel.json` with proper serverless routing
   - ✓ Added CORS headers configuration
   - ✓ Added `.vercelignore` to exclude unnecessary files
   - ✓ Configured API routes properly

3. **Frontend Config**
   - ✓ Updated `config.js` with smart API URL detection
   - ✓ Works on localhost, Vercel, and custom domains
   - ✓ Console logging for debugging

4. **.gitignore Files**
   - ✓ Fixed to not exclude deployment-critical files
   - ✓ Properly excludes sensitive data

---

## 🚀 Deployment Steps

### Step 1: Deploy Backend First

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Deploy backend:**
   ```bash
   cd backend
   vercel --prod
   ```

3. **Get your backend URL:**
   ```
   https://texandco-backend-xxx.vercel.app
   ```

4. **Test backend endpoints:**
   ```
   https://texandco-backend-xxx.vercel.app/api/health
   https://texandco-backend-xxx.vercel.app/api/products
   ```

---

### Step 2: Set Environment Variables

**In Vercel Dashboard for Backend:**
- Settings → Environment Variables
- Add: `NODE_ENV` = `production`

**In Vercel Dashboard for Frontend:**
- Settings → Environment Variables
- Add: `REACT_APP_API_URL` = `https://texandco-backend-xxx.vercel.app`

---

### Step 3: Deploy Frontend

1. **Deploy frontend:**
   ```bash
   cd frontend
   vercel --prod
   ```

2. **After deployment:**
   - Frontend will be at: `https://texandco-frontend-xxx.vercel.app`
   - Will automatically use backend API URL from environment

---

## 📋 File Changes Made

### Frontend
- ✓ `vercel.json` - Created with SPA routing
- ✓ `.vercelignore` - Created to exclude build files
- ✓ `config.js` - Updated with smart URL detection
- ✓ `package.json` - Already correct

### Backend
- ✓ `vercel.json` - Enhanced with CORS and proper routing
- ✓ `.vercelignore` - Created to exclude unnecessary files
- ✓ `api/` files - Already serverless-ready

### Root
- ✓ `.gitignore` - Fixed to allow Git to track necessary files

---

## ⚠️ Common Issues & Solutions

### Issue: "Cannot find module" errors
**Solution:** Ensure all dependencies are in `package.json`
```bash
cd backend
npm install
npm ls
```

### Issue: API returning 404
**Solution:** Check Vercel logs
```bash
vercel logs
```

### Issue: CORS errors in browser
**Solution:** Already fixed in `backend/vercel.json` headers

### Issue: Frontend not loading
**Solution:** Check that all files exist:
- ✓ index.html
- ✓ styles.css
- ✓ app.js
- ✓ config.js

### Issue: Environment variables not working
**Solution:** Set in Vercel Dashboard, not in .env file
1. Go to Project Settings
2. Environment Variables
3. Add variables
4. Redeploy

---

## 🔍 Verification Steps

After both deployments:

1. **Check Backend:**
   ```bash
   curl https://your-backend.vercel.app/api/health
   # Should return JSON with status: OK
   ```

2. **Check Frontend:**
   - Open `https://your-frontend.vercel.app`
   - Open DevTools Console (F12)
   - Should see: `API Base URL: https://your-backend.vercel.app`

3. **Test API Call:**
   - Search for a fabric
   - Should see products load
   - No CORS errors in console

---

## 📝 Environment Variables Required

**Backend (Vercel Project Settings):**
```
NODE_ENV=production
```

**Frontend (Vercel Project Settings):**
```
REACT_APP_API_URL=https://your-backend-url.vercel.app
```

---

## 🎉 Deployment Complete When:

- ✅ Backend API responds at `/api/health`
- ✅ Frontend loads without 404s
- ✅ Frontend can fetch products from backend
- ✅ No CORS errors in console
- ✅ Cart calculations work
- ✅ All navigation works

---

## 🔄 Redeployment

To redeploy after making changes:

```bash
# Backend
cd backend
vercel --prod

# Frontend
cd frontend
vercel --prod
```

Changes take effect immediately!

---

## 📊 What's Running on Vercel

| Service | Type | URL |
|---------|------|-----|
| Backend | Serverless Functions | https://xx-backend.vercel.app |
| Frontend | Static Site | https://xx-frontend.vercel.app |
| API Endpoints | Node.js Functions | /api/products, /api/orders, etc. |

---

## ✨ That's It!

Your entire stack is now Vercel-ready with:
- ✅ Serverless backend (auto-scaling)
- ✅ Static frontend (CDN-cached)
- ✅ CORS properly configured
- ✅ Environment variables setup
- ✅ Zero cold-start issues
- ✅ Production-grade deployment
