from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from core.database import engine, Base, SessionLocal
from routers import products, orders, cart, sellers, auth, search


def run_seed():
    """Seed demo data on first startup — skips if already seeded."""
    try:
        from core.security import hash_password
        from models.user import User, UserRole
        from models.product import Product, FabricGrade
        from models.order import Order, OrderItem, OrderStatus

        db = SessionLocal()

        # Skip if already seeded
        if db.query(User).count() > 0:
            db.close()
            return

        print("🌱 Seeding demo data...")

        sellers_data = [
            ("Karthik Textiles",  "9876543210", "Tiruppur",   "KT"),
            ("Sri Selvi Exports", "9876543211", "Tiruppur",   "SS"),
            ("Raja Fabrics",      "9876543212", "Erode",      "RF"),
            ("Murugan Textiles",  "9876543213", "Tiruppur",   "MT"),
            ("Priya Knits",       "9876543214", "Coimbatore", "PK"),
            ("Vignesh Fab Co",    "9876543215", "Tiruppur",   "VF"),
        ]
        sellers = {}
        for name, phone, city, key in sellers_data:
            u = User(name=name, phone=phone, city=city,
                     password=hash_password("seller123"), role=UserRole.seller)
            db.add(u)
            db.flush()
            sellers[key] = u

        products_data = [
            ("p1","Black Loopknit","loopknit",180,"Jet Black",420,82,FabricGrade.A,"100% Cotton","KT",4.8,132,"TXK-2024-882","Minor shade variation","🧶","bg-green"),
            ("p2","Navy Rib Fabric","rib",220,"Navy Blue",180,95,FabricGrade.B,"95% Cotton 5% Spandex","SS",4.5,89,"TXR-2024-441","Small holes","🔷","bg-blue"),
            ("p3","Cream Fleece","fleece",300,"Off-White",92,110,FabricGrade.A,"100% Polyester","RF",4.9,204,"TXF-2024-207","Premium seconds","✨","bg-yellow"),
            ("p4","Red Interlock","interlock",200,"Fire Red",310,88,FabricGrade.B,"100% Cotton","MT",4.3,67,"TXI-2024-663","Color bleeding risk","❤️","bg-red"),
            ("p5","White Jersey","jersey",160,"White",560,72,FabricGrade.A,"100% Cotton","PK",4.7,156,"TXJ-2024-119","Minor pilling","⬜","bg-gray"),
            ("p6","Purple Interlock","interlock",210,"Violet",240,92,FabricGrade.A,"100% Cotton","VF",4.6,98,"TXI-2024-774","Texture inconsistency","💜","bg-purple"),
        ]
        prods = {}
        for pid,name,ptype,gsm,color,stock,price,grade,comp,skey,rating,oc,batch,defect,emoji,bg in products_data:
            p = Product(id=pid, name=name, type=ptype, gsm=gsm, color=color,
                        stock=stock, price=price, grade=grade, composition=comp,
                        batch=batch, defect=defect, emoji=emoji, bg=bg,
                        rating=rating, orders_count=oc, seller_id=sellers[skey].id)
            db.add(p)
            db.flush()
            prods[pid] = p

        buyer = User(name="Ravi Garments", phone="9000000001", city="Chennai",
                     password=hash_password("buyer123"), role=UserRole.buyer)
        db.add(buyer)
        db.flush()

        demo_orders = [
            ("p1", 120, OrderStatus.transit),
            ("p4", 80,  OrderStatus.placed),
            ("p2", 60,  OrderStatus.delivered),
            ("p3", 40,  OrderStatus.processing),
            ("p5", 200, OrderStatus.delivered),
            ("p6", 100, OrderStatus.transit),
        ]
        for pid, qty, status in demo_orders:
            p    = prods[pid]
            line = qty * p.price
            gst  = round(line * 0.05, 2)
            o = Order(buyer_id=buyer.id, status=status, subtotal=line,
                      shipping_cost=850.0, gst_amount=gst, gst_rate=0.05,
                      total=round(line + 850 + gst, 2))
            db.add(o)
            db.flush()
            db.add(OrderItem(order_id=o.id, product_id=p.id,
                             qty_kg=qty, price_per_kg=p.price, total=line))

        db.commit()
        db.close()
        print("✅ Seed complete!")

    except Exception as e:
        print(f"⚠️ Seed skipped: {e}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create tables then seed
    Base.metadata.create_all(bind=engine)
    run_seed()
    yield


app = FastAPI(
    title="Tex & Co API",
    description="Textile Marketplace Backend — Tex & Co",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
