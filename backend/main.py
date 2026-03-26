from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(title="Tex & Co Backend", version="1.0.0")

# Port configuration
PORT = int(os.getenv("PORT", 8000))

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================== Data Models ====================
class Product(BaseModel):
    id: str
    name: str
    type: str
    gsm: int
    color: str
    stock: int
    price: int
    grade: str
    comp: str
    seller: str
    sellerAv: str
    rating: str
    orders: int
    city: str
    batch: str
    defect: str
    emoji: str
    bg: str

class Order(BaseModel):
    id: Optional[str] = None
    company: str
    email: str
    address: str
    total: str
    items: List[dict]
    status: Optional[str] = "placed"
    createdAt: Optional[str] = None

class CartItem(BaseModel):
    productId: str
    quantity: int
    price: Optional[int] = None

# ==================== Data ====================
PRODUCTS = [
    Product(
        id="p1", name="Black Loopknit", type="loopknit", gsm=180, color="Jet Black",
        stock=420, price=82, grade="A", comp="100% Cotton", seller="Karthik Textiles",
        sellerAv="KT", rating="4.8", orders=132, city="Tiruppur", batch="TXK-2024-882",
        defect="Minor shade variation in 8% of rolls.", emoji="🧶", bg="bg-green"
    ),
    Product(
        id="p2", name="Navy Rib Fabric", type="rib", gsm=220, color="Navy Blue",
        stock=180, price=95, grade="B", comp="95% Cotton 5% Spandex", seller="Sri Selvi Exports",
        sellerAv="SS", rating="4.5", orders=89, city="Tiruppur", batch="TXR-2024-441",
        defect="Small holes in 3 rolls (~2% of stock).", emoji="🔷", bg="bg-blue"
    ),
    Product(
        id="p3", name="Cream Fleece", type="fleece", gsm=300, color="Off-White",
        stock=92, price=110, grade="A", comp="100% Polyester", seller="Raja Fabrics",
        sellerAv="RF", rating="4.9", orders=204, city="Erode", batch="TXF-2024-207",
        defect="Premium seconds. Slight lint variation in edges.", emoji="✨", bg="bg-yellow"
    ),
    Product(
        id="p4", name="Red Interlock", type="interlock", gsm=200, color="Fire Red",
        stock=310, price=88, grade="B", comp="100% Cotton", seller="Murugan Textiles",
        sellerAv="MT", rating="4.3", orders=67, city="Tiruppur", batch="TXI-2024-663",
        defect="Color bleeding risk when washing.", emoji="❤️", bg="bg-red"
    ),
    Product(
        id="p5", name="White Jersey", type="jersey", gsm=160, color="White",
        stock=560, price=72, grade="A", comp="100% Cotton", seller="Priya Knits",
        sellerAv="PK", rating="4.7", orders=156, city="Coimbatore", batch="TXJ-2024-119",
        defect="Minor pilling on 5% of fabric surface.", emoji="⬜", bg="bg-gray"
    ),
    Product(
        id="p6", name="Purple Interlock", type="interlock", gsm=210, color="Violet",
        stock=240, price=92, grade="A", comp="100% Cotton", seller="Vignesh Fab Co",
        sellerAv="VF", rating="4.6", orders=98, city="Tiruppur", batch="TXI-2024-774",
        defect="Slight texture inconsistency in 10% of rolls.", emoji="💜", bg="bg-purple"
    ),
]

ORDERS = [
    {
        "id": "o1", "buyer": "Ravi Garments", "product": "Black Loopknit", "qty": "120 kg",
        "amt": "₹9,840", "status": "transit", "emoji": "🧶", "bg": "bg-green"
    },
    {
        "id": "o2", "buyer": "Sri Selvi Exports", "product": "Red Interlock", "qty": "80 kg",
        "amt": "₹7,040", "status": "placed", "emoji": "❤️", "bg": "bg-red"
    },
    {
        "id": "o3", "buyer": "Murugan Fab", "product": "Navy Rib Fabric", "qty": "60 kg",
        "amt": "₹5,700", "status": "delivered", "emoji": "🔷", "bg": "bg-blue"
    },
    {
        "id": "o4", "buyer": "Priya Knits", "product": "Cream Fleece", "qty": "40 kg",
        "amt": "₹4,400", "status": "processing", "emoji": "✨", "bg": "bg-yellow"
    },
    {
        "id": "o5", "buyer": "Senthil & Co", "product": "White Jersey", "qty": "200 kg",
        "amt": "₹14,400", "status": "delivered", "emoji": "⬜", "bg": "bg-gray"
    },
    {
        "id": "o6", "buyer": "ABCTextiles", "product": "Purple Interlock", "qty": "100 kg",
        "amt": "₹9,200", "status": "transit", "emoji": "💜", "bg": "bg-purple"
    },
]

# ==================== Endpoints ====================

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "OK",
        "timestamp": datetime.utcnow().isoformat(),
        "message": "Tex & Co Backend Running"
    }

@app.get("/api/products", response_model=List[Product])
async def get_products():
    """Get all products"""
    return PRODUCTS

@app.get("/api/products/{product_id}", response_model=Product)
async def get_product(product_id: str):
    """Get a specific product by ID"""
    product = next((p for p in PRODUCTS if p.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.get("/api/orders")
async def get_orders():
    """Get all orders"""
    return ORDERS

@app.post("/api/orders")
async def create_order(order: Order):
    """Create a new order"""
    if not order.company or not order.email or not order.address or not order.items:
        raise HTTPException(status_code=400, detail="Missing required fields")
    
    new_order = {
        "id": "o" + str(int(datetime.utcnow().timestamp() * 1000)),
        "company": order.company,
        "email": order.email,
        "address": order.address,
        "total": order.total,
        "items": order.items,
        "status": "placed",
        "createdAt": datetime.utcnow().isoformat()
    }
    
    ORDERS.append(new_order)
    return {
        "message": "Order created successfully",
        "order": new_order
    }

@app.post("/api/cart/add")
async def add_to_cart(item: CartItem):
    """Add item to cart"""
    if not item.productId or not item.quantity:
        raise HTTPException(status_code=400, detail="Invalid product or quantity")
    
    return {
        "message": "Item added to cart",
        "productId": item.productId,
        "quantity": item.quantity,
        "addedAt": datetime.utcnow().isoformat()
    }

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Tex & Co - Textile Marketplace Backend",
        "version": "1.0.0",
        "docs": "/docs"
    }

# ==================== Error Handlers ====================

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {
        "error": exc.detail,
        "status_code": exc.status_code
    }

# ==================== Main ====================

if __name__ == "__main__":
    import uvicorn
    print(f"🚀 Backend server running on port {PORT}")
    print(f"📚 API documentation available at http://localhost:{PORT}/docs")
    uvicorn.run(app, host="0.0.0.0", port=PORT)
