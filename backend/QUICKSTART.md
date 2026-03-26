# Python FastAPI Backend - Quick Reference

## 🎯 One-Command Startup

### Windows
```bash
cd backend
start.bat
```

### Mac/Linux
```bash
cd backend
chmod +x start.sh
./start.sh
```

---

## 📋 Manual Setup (5 Steps)

### Step 1: Navigate to Backend
```bash
cd backend
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Server
```bash
python main.py
```

### Step 5: Access API
- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## 🐳 Docker Setup

### Run Backend Only
```bash
docker-compose up backend
```

### Run Everything (Frontend + Backend)
```bash
docker-compose up
```

---

## 🔑 Environment Ports

| Service | Port | URL |
|---------|------|-----|
| Frontend | 3000 | http://localhost:3000 |
| Backend | 8000 | http://localhost:8000 |
| Swagger Docs | 8000 | http://localhost:8000/docs |

---

## 📚 API Endpoints

```
GET    /api/health           → Health check
GET    /api/products         → All products
GET    /api/products/{id}    → Single product
GET    /api/orders           → All orders
POST   /api/orders           → Create order
POST   /api/cart/add         → Add to cart
```

---

## ✅ Verify Installation

### Test Backend is Running
```bash
curl http://localhost:8000/api/health
```

Should return:
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00.123456"
}
```

### Test Frontend Connection
Open: http://localhost:3000

Should show Tex & Co homepage with no console errors.

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| Port 8000 in use | See `PYTHON_SETUP.md` for port change instructions |
| Module not found | Run `pip install -r requirements.txt` |
| Python not found | Install Python 3.11+ from python.org |
| Virtual env issues | Delete `venv/` folder and run again |
| CORS errors | Should be auto-fixed, check browser console |

---

## 📂 Project Structure

```
texandco/
├── frontend/              ← Your web app
│   ├── index.html
│   ├── app.js
│   ├── styles.css
│   └── config.js         ← Points to port 8000 ✓
├── backend/              ← Python FastAPI
│   ├── main.py           ← Main server file
│   ├── requirements.txt  ← Python dependencies
│   ├── Dockerfile
│   ├── start.bat         ← Windows quick start
│   ├── start.sh          ← Mac/Linux quick start
│   ├── .env              ← PORT=8000
│   ├── PYTHON_SETUP.md   ← Detailed setup guide
│   └── MIGRATION_GUIDE.md ← Node → Python migration
├── docker-compose.yml    ← Local dev setup
├── README.md
└── index.html            ← Root file
```

---

## 🎯 Standard Development Workflow

```bash
# Terminal 1: Start Backend
cd backend
./start.sh              # Mac/Linux
# or
start.bat              # Windows

# Terminal 2: Start Frontend (optional, usually auto-runs on 3000)
cd frontend
python -m http.server 3000

# Browser
# Frontend: http://localhost:3000
# Backend Docs: http://localhost:8000/docs
```

---

## 🚀 Ready to Deploy?

See `PYTHON_SETUP.md` section "Production Deployment" for Docker or cloud options.

---

**Status: ✅ Backend ready to run!**
