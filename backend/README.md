# Tex & Co — Backend API 🧶

FastAPI backend for the **Tex & Co** textile marketplace.  
Matches the frontend's data structure (`app.js`) exactly.

---

## 📁 Project Structure

```
texandco-backend/
├── app/
│   ├── main.py               ← FastAPI app + CORS + router registration
│   ├── core/
│   │   ├── config.py         ← Settings (env vars)
│   │   ├── database.py       ← SQLAlchemy engine + session
│   │   └── security.py       ← JWT + password hashing
│   ├── models/
│   │   ├── user.py           ← User (buyer / seller / admin)
│   │   ├── product.py        ← Product (fabric listings)
│   │   ├── order.py          ← Order + OrderItem
│   │   └── cart.py           ← CartItem
│   ├── routers/
│   │   ├── auth.py           ← /api/auth — register, login
│   │   ├── products.py       ← /api/products — CRUD
│   │   ├── cart.py           ← /api/cart — add/update/remove
│   │   ├── orders.py         ← /api/orders — checkout, list
│   │   ├── sellers.py        ← /api/sellers — dashboard, orders
│   │   └── search.py         ← /api/search — text search
│   └── schemas/
│       └── schemas.py        ← Pydantic request/response models
├── scripts/
│   └── seed.py               ← Seeds all 6 products + demo orders
├── tests/
│   └── test_security.py
├── alembic/                  ← DB migrations
├── Dockerfile
├── requirements.txt
└── .env.example
```

---

## 🚀 Quick Start (Local)

```bash
# 1. Clone and enter
cd texandco-backend

# 2. Create virtual env
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy env file
cp .env.example .env

# 5. Seed the database (creates texandco.db + demo data)
python scripts/seed.py

# 6. Run the server
uvicorn app.main:app --reload --port 8000
```

Visit **http://localhost:8000/docs** for the interactive API docs (Swagger UI).

---

## 🔑 Demo Credentials

| Role   | Phone       | Password   |
|--------|-------------|------------|
| Seller | 9876543210  | seller123  |
| Buyer  | 9000000001  | buyer123   |

---

## 📡 API Endpoints

### Auth
| Method | Endpoint           | Description         |
|--------|--------------------|---------------------|
| POST   | /api/auth/register | Register new user   |
| POST   | /api/auth/login    | Login → JWT token   |

### Products
| Method | Endpoint                | Description              |
|--------|-------------------------|--------------------------|
| GET    | /api/products/          | List all (with filters)  |
| GET    | /api/products/{id}      | Get single product       |
| POST   | /api/products/          | Create listing (seller)  |
| PUT    | /api/products/{id}      | Update listing (seller)  |
| DELETE | /api/products/{id}      | Soft-delete (seller)     |

### Cart
| Method | Endpoint          | Description           |
|--------|-------------------|-----------------------|
| GET    | /api/cart/        | Get cart + totals     |
| POST   | /api/cart/add     | Add item to cart      |
| PUT    | /api/cart/{id}    | Update item qty       |
| DELETE | /api/cart/{id}    | Remove item           |
| DELETE | /api/cart/        | Clear entire cart     |

### Orders
| Method | Endpoint                    | Description             |
|--------|-----------------------------|-------------------------|
| POST   | /api/orders/checkout        | Place order from cart   |
| GET    | /api/orders/                | My orders               |
| GET    | /api/orders/{id}            | Order detail            |
| PUT    | /api/orders/{id}/status     | Update status (seller)  |

### Seller Dashboard
| Method | Endpoint              | Description          |
|--------|-----------------------|----------------------|
| GET    | /api/sellers/dashboard | Stats (sales, listings) |
| GET    | /api/sellers/orders   | Orders for my products |

### Search
| Method | Endpoint      | Description                  |
|--------|---------------|------------------------------|
| GET    | /api/search/  | Search by name + color       |

### Health
| Method | Endpoint       | Description    |
|--------|----------------|----------------|
| GET    | /api/health    | Health check   |

---

## 🌐 Connecting Frontend

Update `config.js` in your frontend:

```js
// For local dev
const API_BASE_URL = "http://localhost:8000";

// For production (Vercel / Railway / Render)
const API_BASE_URL = "https://your-backend-url.com";
```

---

## 🐳 Docker

```bash
docker build -t texandco-backend .
docker run -p 8000:8000 texandco-backend
```

---

## 🛠 Tech Stack

- **FastAPI** — Modern Python API framework
- **SQLAlchemy** — ORM (SQLite locally, Postgres in prod)
- **Pydantic v2** — Request/response validation
- **JWT** — Stateless auth via python-jose
- **Bcrypt** — Password hashing via passlib
- **Alembic** — Database migrations
- **Uvicorn** — ASGI server
