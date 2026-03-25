# Python Backend Setup Guide

## 🐍 FastAPI Backend Running on Port 8000

Your backend has been converted from Node.js Express to Python FastAPI!

---

## 🚀 Quick Start - Local Development

### Option 1: Direct Python (Recommended for Development)

**Step 1: Install Python 3.11+**
- Download from https://www.python.org/
- Or use your package manager:
  ```bash
  # Ubuntu/Debian
  sudo apt-get install python3.11 python3-pip
  
  # Mac
  brew install python@3.11
  ```

**Step 2: Set up Virtual Environment**
```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

**Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Run Backend**
```bash
python main.py
```

Backend will be at: **http://localhost:8000**

**Step 5: Access API Documentation**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

### Option 2: Using Docker

```bash
# Build backend image
docker-compose build backend

# Run backend only
docker-compose up backend

# Or run both frontend and backend
docker-compose up
```

Backend will be at: **http://localhost:8000**

---

## 📚 API Endpoints

All endpoints same as before, now running on **port 8000**:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/health` | GET | Health check |
| `/api/products` | GET | Get all products |
| `/api/products/{id}` | GET | Get specific product |
| `/api/orders` | GET | Get all orders |
| `/api/orders` | POST | Create new order |
| `/api/cart/add` | POST | Add item to cart |
| `/docs` | GET | Swagger UI documentation |
| `/redoc` | GET | ReDoc documentation |

---

## 🔧 Project Structure

```
backend/
├── main.py                 ← FastAPI application (replaces app/server.js)
├── requirements.txt        ← Python dependencies (replaces package.json)
├── Dockerfile              ← Updated for Python
├── .env                    ← PORT=8000
├── vercel.json             ← For Vercel deployment
├── app/
│   └── server.js          ← Keep for reference (no longer used)
└── api/
    ├── health.js
    ├── orders.js
    ├── products.js
    └── cart.js            ← Keep for reference (no longer used)
```

**Note:** The old `app/server.js` and `api/*.js` files are no longer used. All logic is now in `main.py`.

---

## 📁 Dependencies (requirements.txt)

```
fastapi==0.104.1        # Web framework
uvicorn==0.24.0         # ASGI server
python-dotenv==1.0.0    # Environment variables
pydantic==2.5.0         # Data validation
```

---

## 🔌 Connecting Frontend

Frontend `config.js` automatically detects:
- Local development: `http://localhost:8000`
- Production: `https://texandco-backend.vercel.app` (or your backend URL)

---

## 💡 FastAPI Features

Your new backend includes:

✅ **Automatic API Documentation**
- Swagger UI: `/docs`
- ReDoc: `/redoc`

✅ **Type Validation**
- Pydantic models for request/response validation
- Automatic validation errors

✅ **CORS Enabled**
- All origins allowed by default
- Configurable in `main.py`

✅ **Async/Await Support**
- All endpoints are async for better performance

✅ **Error Handling**
- Automatic error formatting
- HTTP exception handling

---

## 🚀 Production Deployment

### Docker

```bash
# Build
docker build -t texandco-backend .

# Run
docker run -p 8000:8000 texandco-backend
```

### Vercel

```bash
# Deploy
vercel --prod
```

---

## 🛠️ Common Issues

### Issue: "ModuleNotFoundError: No module named 'fastapi'"
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: Port 8000 already in use
**Solution:**
```bash
# Use different port
python -m uvicorn main:app --port 8080

# Or kill process on port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux:
lsof -i :8000
kill -9 <PID>
```

### Issue: CORS errors
Already handled! CORS is enabled for all origins in `main.py`.

---

## 📊 Development vs Production

**Development (Local):**
```bash
python main.py
# Auto-reload on file changes
```

**Production (Docker):**
```bash
docker build -t texandco-backend .
docker run -p 8000:8000 texandco-backend
```

---

## ⚙️ Environment Variables

Edit `.env` file:
```env
PORT=8000
```

Changes take effect on next restart.

---

## ✨ What's the Same

Your API endpoints work exactly the same!

**GET /api/products** still returns:
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

**POST /api/orders** still creates orders with:
```json
{
  "company": "...",
  "email": "...",
  "address": "...",
  "total": "...",
  "items": [...]
}
```

---

## 🎯 Next Steps

1. ✅ Install Python dependencies: `pip install -r requirements.txt`
2. ✅ Run backend: `python main.py`
3. ✅ Test at: http://localhost:8000/docs
4. ✅ Frontend automatically connects to port 8000

---

**Status: ✅ Backend converted to FastAPI on port 8000!**
