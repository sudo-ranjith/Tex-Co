from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.cart import CartItem
from app.models.product import Product
from app.models.user import User
from app.schemas.schemas import CartAddRequest, CartUpdateRequest, CartSummary, CartItemOut

router = APIRouter()

SHIPPING = 850.0
GST_RATE = 0.05


def _build_summary(items, db) -> CartSummary:
    out_items = []
    subtotal  = 0.0

    for item in items:
        p         = item.product
        line      = round(item.qty_kg * p.price, 2)
        subtotal += line
        out_items.append(CartItemOut(
            id=item.id,
            product_id=p.id,
            name=p.name,
            emoji=p.emoji,
            bg=p.bg,
            price=p.price,
            qty_kg=item.qty_kg,
            line_total=line,
        ))

    gst   = round(subtotal * GST_RATE, 2)
    total = round(subtotal + SHIPPING + gst, 2)

    return CartSummary(
        items=out_items,
        item_count=len(out_items),
        subtotal=subtotal,
        shipping=SHIPPING,
        gst_amount=gst,
        total=total,
    )


@router.get("/", response_model=CartSummary)
def get_cart(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    items = db.query(CartItem).filter(CartItem.user_id == current_user.id).all()
    return _build_summary(items, db)


@router.post("/add", response_model=CartSummary, status_code=201)
def add_to_cart(
    data:         CartAddRequest,
    current_user: User    = Depends(get_current_user),
    db:           Session = Depends(get_db),
):
    product = db.query(Product).filter(Product.id == data.product_id, Product.is_active == True).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    existing = db.query(CartItem).filter(
        CartItem.user_id == current_user.id,
        CartItem.product_id == data.product_id,
    ).first()

    if existing:
        existing.qty_kg += data.qty_kg
    else:
        item = CartItem(user_id=current_user.id, product_id=data.product_id, qty_kg=data.qty_kg)
        db.add(item)

    db.commit()

    items = db.query(CartItem).filter(CartItem.user_id == current_user.id).all()
    return _build_summary(items, db)


@router.put("/{item_id}", response_model=CartSummary)
def update_cart_item(
    item_id:      str,
    data:         CartUpdateRequest,
    current_user: User    = Depends(get_current_user),
    db:           Session = Depends(get_db),
):
    item = db.query(CartItem).filter(
        CartItem.id == item_id,
        CartItem.user_id == current_user.id,
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    item.qty_kg = data.qty_kg
    db.commit()

    items = db.query(CartItem).filter(CartItem.user_id == current_user.id).all()
    return _build_summary(items, db)


@router.delete("/{item_id}", response_model=CartSummary)
def remove_cart_item(
    item_id:      str,
    current_user: User    = Depends(get_current_user),
    db:           Session = Depends(get_db),
):
    item = db.query(CartItem).filter(
        CartItem.id == item_id,
        CartItem.user_id == current_user.id,
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    db.delete(item)
    db.commit()

    items = db.query(CartItem).filter(CartItem.user_id == current_user.id).all()
    return _build_summary(items, db)


@router.delete("/", status_code=204)
def clear_cart(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db.query(CartItem).filter(CartItem.user_id == current_user.id).delete()
    db.commit()
