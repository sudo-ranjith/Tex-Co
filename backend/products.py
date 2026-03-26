from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.core.database import get_db
from app.core.security import get_current_user, get_current_user_optional
from app.models.product import Product
from app.models.user import User
from app.schemas.schemas import ProductCreate, ProductUpdate, ProductOut

router = APIRouter()


def _product_to_out(p: Product) -> dict:
    return {
        "id":           p.id,
        "name":         p.name,
        "type":         p.type,
        "gsm":          p.gsm,
        "color":        p.color,
        "stock":        p.stock,
        "price":        p.price,
        "grade":        p.grade,
        "composition":  p.composition,
        "batch":        p.batch,
        "defect":       p.defect,
        "emoji":        p.emoji,
        "bg":           p.bg,
        "rating":       p.rating,
        "orders_count": p.orders_count,
        "seller": {
            "id":   p.seller.id,
            "name": p.seller.name,
            "city": p.seller.city,
        },
        "created_at": p.created_at,
    }


@router.get("/", response_model=List[ProductOut])
def list_products(
    type:    Optional[str]   = Query(None, description="Filter by fabric type"),
    grade:   Optional[str]   = Query(None, description="Filter by grade A/B/C"),
    min_gsm: Optional[int]   = Query(None),
    max_gsm: Optional[int]   = Query(None),
    min_price: Optional[float] = Query(None),
    max_price: Optional[float] = Query(None),
    city:    Optional[str]   = Query(None),
    db:      Session          = Depends(get_db),
):
    q = db.query(Product).filter(Product.is_active == True)

    if type:      q = q.filter(Product.type.ilike(f"%{type}%"))
    if grade:     q = q.filter(Product.grade == grade.upper())
    if min_gsm:   q = q.filter(Product.gsm >= min_gsm)
    if max_gsm:   q = q.filter(Product.gsm <= max_gsm)
    if min_price: q = q.filter(Product.price >= min_price)
    if max_price: q = q.filter(Product.price <= max_price)
    if city:
        q = q.join(User).filter(User.city.ilike(f"%{city}%"))

    products = q.order_by(Product.created_at.desc()).all()
    return [_product_to_out(p) for p in products]


@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: str, db: Session = Depends(get_db)):
    p = db.query(Product).filter(Product.id == product_id, Product.is_active == True).first()
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")
    return _product_to_out(p)


@router.post("/", response_model=ProductOut, status_code=201)
def create_product(
    data:         ProductCreate,
    current_user: User    = Depends(get_current_user),
    db:           Session = Depends(get_db),
):
    if current_user.role not in ("seller", "admin"):
        raise HTTPException(status_code=403, detail="Only sellers can list products")

    product = Product(**data.model_dump(), seller_id=current_user.id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return _product_to_out(product)


@router.put("/{product_id}", response_model=ProductOut)
def update_product(
    product_id:   str,
    data:         ProductUpdate,
    current_user: User    = Depends(get_current_user),
    db:           Session = Depends(get_db),
):
    p = db.query(Product).filter(Product.id == product_id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")
    if p.seller_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not your listing")

    for field, val in data.model_dump(exclude_none=True).items():
        setattr(p, field, val)

    db.commit()
    db.refresh(p)
    return _product_to_out(p)


@router.delete("/{product_id}", status_code=204)
def delete_product(
    product_id:   str,
    current_user: User    = Depends(get_current_user),
    db:           Session = Depends(get_db),
):
    p = db.query(Product).filter(Product.id == product_id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")
    if p.seller_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not your listing")

    p.is_active = False  # Soft delete
    db.commit()
