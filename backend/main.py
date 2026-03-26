from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.database import engine, Base
from app.routers import products, orders, cart, sellers, auth, search


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create tables
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown: cleanup if needed


app = FastAPI(
    title="Tex & Co API",
    description="Textile Marketplace Backend — Tex & Co",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS — allow frontend (Vercel + localhost)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "https://*.vercel.app",
        "*",  # Remove in production, replace with exact domain
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth.router,     prefix="/api/auth",     tags=["Auth"])
app.include_router(products.router, prefix="/api/products", tags=["Products"])
app.include_router(orders.router,   prefix="/api/orders",   tags=["Orders"])
app.include_router(cart.router,     prefix="/api/cart",     tags=["Cart"])
app.include_router(sellers.router,  prefix="/api/sellers",  tags=["Sellers"])
app.include_router(search.router,   prefix="/api/search",   tags=["Search"])


@app.get("/api/health", tags=["Health"])
def health_check():
    return {"status": "ok", "service": "Tex & Co API", "version": "1.0.0"}


@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to Tex & Co API 🧶"}
