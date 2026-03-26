"""
seed.py — Populate DB with the same demo data used in frontend app.js
Run: python scripts/seed.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app.core.database import SessionLocal, engine, Base
from app.core.security import hash_password
from app.models.user import User, UserRole
from app.models.product import Product, FabricGrade
from app.models.order import Order, OrderItem, OrderStatus

# Create all tables first
Base.metadata.create_all(bind=engine)

db = SessionLocal()


def seed():
    print("🌱 Seeding Tex & Co database...")

    # ── SELLERS ──────────────────────────────────────────────
    sellers_data = [
        dict(name="Karthik Textiles",  phone="9876543210", city="Tiruppur",   initials="KT"),
        dict(name="Sri Selvi Exports", phone="9876543211", city="Tiruppur",   initials="SS"),
        dict(name="Raja Fabrics",      phone="9876543212", city="Erode",      initials="RF"),
        dict(name="Murugan Textiles",  phone="9876543213", city="Tiruppur",   initials="MT"),
        dict(name="Priya Knits",       phone="9876543214", city="Coimbatore", initials="PK"),
        dict(name="Vignesh Fab Co",    phone="9876543215", city="Tiruppur",   initials="VF"),
    ]

    sellers = {}
    for s in sellers_data:
        existing = db.query(User).filter(User.phone == s["phone"]).first()
        if not existing:
            user = User(
                name=s["name"],
                phone=s["phone"],
                city=s["city"],
                password=hash_password("seller123"),
                role=UserRole.seller,
            )
            db.add(user)
            db.flush()
            sellers[s["initials"]] = user
            print(f"  ✅ Seller: {user.name}")
        else:
            sellers[s["initials"]] = existing
            print(f"  ⏭  Seller already exists: {existing.name}")

    # ── PRODUCTS (mirrors frontend PRODUCTS array exactly) ────
    products_data = [
        dict(
            id="p1", name="Black Loopknit",   type="loopknit",  gsm=180, color="Jet Black",
            stock=420, price=82,  grade=FabricGrade.A,
            composition="100% Cotton",             seller_key="KT",
            rating=4.8, orders_count=132, city="Tiruppur",
            batch="TXK-2024-882", defect="Minor shade variation",
            emoji="🧶", bg="bg-green",
        ),
        dict(
            id="p2", name="Navy Rib Fabric",  type="rib",       gsm=220, color="Navy Blue",
            stock=180, price=95,  grade=FabricGrade.B,
            composition="95% Cotton 5% Spandex",   seller_key="SS",
            rating=4.5, orders_count=89,  city="Tiruppur",
            batch="TXR-2024-441", defect="Small holes",
            emoji="🔷", bg="bg-blue",
        ),
        dict(
            id="p3", name="Cream Fleece",     type="fleece",    gsm=300, color="Off-White",
            stock=92,  price=110, grade=FabricGrade.A,
            composition="100% Polyester",           seller_key="RF",
            rating=4.9, orders_count=204, city="Erode",
            batch="TXF-2024-207", defect="Premium seconds",
            emoji="✨", bg="bg-yellow",
        ),
        dict(
            id="p4", name="Red Interlock",    type="interlock", gsm=200, color="Fire Red",
            stock=310, price=88,  grade=FabricGrade.B,
            composition="100% Cotton",             seller_key="MT",
            rating=4.3, orders_count=67,  city="Tiruppur",
            batch="TXI-2024-663", defect="Color bleeding risk",
            emoji="❤️", bg="bg-red",
        ),
        dict(
            id="p5", name="White Jersey",     type="jersey",    gsm=160, color="White",
            stock=560, price=72,  grade=FabricGrade.A,
            composition="100% Cotton",             seller_key="PK",
            rating=4.7, orders_count=156, city="Coimbatore",
            batch="TXJ-2024-119", defect="Minor pilling",
            emoji="⬜", bg="bg-gray",
        ),
        dict(
            id="p6", name="Purple Interlock", type="interlock", gsm=210, color="Violet",
            stock=240, price=92,  grade=FabricGrade.A,
            composition="100% Cotton",             seller_key="VF",
            rating=4.6, orders_count=98,  city="Tiruppur",
            batch="TXI-2024-774", defect="Texture inconsistency",
            emoji="💜", bg="bg-purple",
        ),
    ]

    products = {}
    for pd in products_data:
        existing = db.query(Product).filter(Product.id == pd["id"]).first()
        if not existing:
            seller = sellers[pd.pop("seller_key")]
            pd.pop("city", None)
            product = Product(**pd, seller_id=seller.id)
            db.add(product)
            db.flush()
            products[product.id] = product
            print(f"  ✅ Product: {product.name}")
        else:
            products[existing.id] = existing
            print(f"  ⏭  Product already exists: {existing.name}")

    # ── DEMO BUYER ────────────────────────────────────────────
    buyer_phone = "9000000001"
    buyer = db.query(User).filter(User.phone == buyer_phone).first()
    if not buyer:
        buyer = User(
            name="Ravi Garments",
            phone=buyer_phone,
            city="Chennai",
            password=hash_password("buyer123"),
            role=UserRole.buyer,
        )
        db.add(buyer)
        db.flush()
        print(f"  ✅ Buyer: {buyer.name}")

    # ── DEMO ORDERS (mirrors frontend ORDERS array) ───────────
    orders_data = [
        dict(buyer=buyer, product_id="p1", qty=120, status=OrderStatus.transit),
        dict(buyer=buyer, product_id="p4", qty=80,  status=OrderStatus.placed),
        dict(buyer=buyer, product_id="p2", qty=60,  status=OrderStatus.delivered),
        dict(buyer=buyer, product_id="p3", qty=40,  status=OrderStatus.processing),
        dict(buyer=buyer, product_id="p5", qty=200, status=OrderStatus.delivered),
        dict(buyer=buyer, product_id="p6", qty=100, status=OrderStatus.transit),
    ]

    for od in orders_data:
        p        = products.get(od["product_id"])
        if not p:
            continue
        line     = od["qty"] * p.price
        gst      = round(line * 0.05, 2)
        total    = round(line + 850 + gst, 2)

        order = Order(
            buyer_id=od["buyer"].id,
            status=od["status"],
            subtotal=line,
            shipping_cost=850.0,
            gst_amount=gst,
            gst_rate=0.05,
            total=total,
        )
        db.add(order)
        db.flush()
        db.add(OrderItem(
            order_id=order.id,
            product_id=p.id,
            qty_kg=od["qty"],
            price_per_kg=p.price,
            total=line,
        ))
        print(f"  ✅ Order: {p.name} × {od['qty']}kg [{od['status']}]")

    db.commit()
    print("\n🎉 Seed complete! Database ready.")
    print("\nDemo credentials:")
    print("  Seller  → phone: 9876543210  password: seller123")
    print("  Buyer   → phone: 9000000001  password: buyer123")


if __name__ == "__main__":
    seed()
    db.close()
