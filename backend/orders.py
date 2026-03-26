from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.cart import CartItem
from app.models.order import Order, OrderItem, OrderStatus
from app.models.product import Product
from app.models.user import User
from app.schemas.schemas import CheckoutRequest, OrderOut, OrderItemOut

router = APIRouter()

SHIPPING = 850.0
GST_RATE = 0.05


def _order_to_out(order: Order) -> dict:
    items = []
    for oi in order.items:
        items.append(OrderItemOut(
            id=oi.id,
            product_id=oi.product_id,
            product_name=oi.product.name,
            emoji=oi.product.emoji,
            qty_kg=oi.qty_kg,
            price_per_kg=oi.price_per_kg,
            total=oi.total,
        ))
    return OrderOut(
        id=order.id,
        status=order.status,
        company_name=order.company_name,
        contact_email=order.contact_email,
        delivery_address=order.delivery_address,
        items=items,
        subtotal=order.subtotal,
        shipping_cost=order.shipping_cost,
        gst_amount=order.gst_amount,
        total=order.total,
        created_at=order.created_at,
    )


@router.post("/checkout", response_model=OrderOut, status_code=201)
def checkout(
    data:         CheckoutRequest,
    current_user: User    = Depends(get_current_user),
    db:           Session = Depends(get_db),
):
    """Convert current cart → Order. Clears cart on success."""
    cart_items = db.query(CartItem).filter(CartItem.user_id == current_user.id).all()
    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    subtotal = 0.0
    order_items = []

    for ci in cart_items:
        p = db.query(Product).filter(Product.id == ci.product_id, Product.is_active == True).first()
        if not p:
            raise HTTPException(status_code=400, detail=f"Product {ci.product_id} no longer available")
        if p.stock < ci.qty_kg:
            raise HTTPException(status_code=400, detail=f"Insufficient stock for {p.name}")

        line = round(ci.qty_kg * p.price, 2)
        subtotal += line
        order_items.append(OrderItem(
            product_id=p.id,
            qty_kg=ci.qty_kg,
            price_per_kg=p.price,
            total=line,
        ))
        # Deduct stock
        p.stock -= ci.qty_kg
        p.orders_count += 1

    gst   = round(subtotal * GST_RATE, 2)
    total = round(subtotal + SHIPPING + gst, 2)

    order = Order(
        buyer_id=current_user.id,
        company_name=data.company_name,
        contact_email=data.contact_email,
        delivery_address=data.delivery_address,
        subtotal=subtotal,
        shipping_cost=SHIPPING,
        gst_amount=gst,
        gst_rate=GST_RATE,
        total=total,
        items=order_items,
    )
    db.add(order)

    # Clear cart
    db.query(CartItem).filter(CartItem.user_id == current_user.id).delete()
    db.commit()
    db.refresh(order)

    return _order_to_out(order)


@router.get("/", response_model=List[OrderOut])
def list_my_orders(
    current_user: User    = Depends(get_current_user),
    db:           Session = Depends(get_db),
):
    orders = db.query(Order).filter(Order.buyer_id == current_user.id)\
               .order_by(Order.created_at.desc()).all()
    return [_order_to_out(o) for o in orders]


@router.get("/{order_id}", response_model=OrderOut)
def get_order(
    order_id:     str,
    current_user: User    = Depends(get_current_user),
    db:           Session = Depends(get_db),
):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if order.buyer_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not your order")
    return _order_to_out(order)


@router.put("/{order_id}/status")
def update_order_status(
    order_id:     str,
    status:       OrderStatus,
    current_user: User    = Depends(get_current_user),
    db:           Session = Depends(get_db),
):
    """Seller or admin can update order status."""
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if current_user.role not in ("seller", "admin"):
        raise HTTPException(status_code=403, detail="Not authorized")

    order.status = status
    db.commit()
    return {"message": f"Order status updated to {status}"}
