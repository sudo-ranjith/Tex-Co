# Frontend Troubleshooting Guide

## ✅ Problem Fixed!

The frontend wasn't running because:

1. **Missing startup command** ❌ → Fixed CMD in Dockerfile
2. **Wrong health check path** ❌ → Removed problematic health check
3. **Unnecessary backend dependency** ❌ → Frontend now independent

---

## 🚀 How to Run Frontend Locally

### Option 1: Quick Start (No Docker) - EASIEST ⭐

**Windows:**
```bash
run-frontend.bat
```

**Mac/Linux:**
```bash
bash run-frontend.sh
```

Then open: **http://localhost:3000**

### Option 2: Using Docker

```bash
# Build and run only frontend
docker-compose build frontend
docker-compose up frontend
```

Then open: **http://localhost:3000**

### Option 3: Manual Setup

**Step 1:** Install Node.js (if not already installed)
- Download from: https://nodejs.org/

**Step 2:** Install http-server
```bash
npm install -g http-server
```

**Step 3:** Navigate to frontend folder
```bash
cd frontend
```

**Step 4:** Start server
```bash
http-server . -p 3000
```

**Step 5:** Open browser
```
http://localhost:3000
```

---

## 🔧 Troubleshooting

### Issue: Port 3000 already in use
```bash
# Use different port
http-server . -p 8080

# Then access: http://localhost:8080
```

### Issue: Node/npm not found
```bash
# Check if installed
node --version
npm --version

# If not, download from https://nodejs.org/
```

### Issue: http-server not found
```bash
# Install globally
npm install -g http-server

# Or use with npx (no install needed)
npx http-server . -p 3000
```

### Issue: "Cannot GET"
- Clear browser cache (Ctrl+Shift+Delete)
- Make sure you're accessing the root: `http://localhost:3000`
- Check that `index.html`, `styles.css`, `app.js` exist in `/frontend` folder

---

## 📝 What to Test

Once running at http://localhost:3000, test:

✅ **Navigation**: Click bottom tabs (Home, Search, Cart, Sell, Profile)  
✅ **Search**: Type fabric names in search bar  
✅ **Product Details**: Click any fabric card  
✅ **Cart**: Add items and see prices update  
✅ **Modal**: Click "Upload Inventory" and "Proceed to Checkout"  

---

## 🐳 Docker Issues?

If Docker containers won't start:

```bash
# Stop all containers
docker-compose down

# Clean everything
docker system prune -a

# Rebuild fresh
docker-compose build --no-cache frontend

# Start
docker-compose up frontend
```

---

## 📦 Backend Not Needed for Frontend

Frontend now runs **independently** - backend is optional.

For full app with backend:
```bash
docker-compose up
```

For just frontend:
```bash
# Docker approach
docker-compose up frontend

# OR local approach
run-frontend.bat   (Windows)
bash run-frontend.sh  (Mac/Linux)
```

---

## 🎯 Next Steps

1. ✅ Frontend running? Great!
2. Now run backend in separate terminal:
   ```bash
   cd backend
   npm install
   npm start
   ```
3. Backend runs at **http://localhost:5000/api**
4. Both will communicate automatically

---

## 📞 Quick Commands Reference

| Goal | Command |
|------|---------|
| Quick start frontend | `run-frontend.bat` or `bash run-frontend.sh` |
| Start with Docker | `docker-compose up frontend` |
| Start both services | `docker-compose up` |
| View logs | `docker-compose logs -f frontend` |
| Stop all | `docker-compose down` |
| Clear cache | `docker system prune -a` |

---

**Ready to go!** 🎉 Frontend should now run smoothly on http://localhost:3000
