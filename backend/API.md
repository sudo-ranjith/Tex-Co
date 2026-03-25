# Backend API Routes

## Health Check
- **GET** `/api/health` - Check if server is running

## Products
- **GET** `/api/products` - Get all products
- **GET** `/api/products/:id` - Get specific product

## Orders
- **GET** `/api/orders` - Get all orders
- **POST** `/api/orders` - Create new order
  ```json
  {
    "company": "Company Name",
    "email": "email@example.com",
    "address": "Delivery Address",
    "total": 10000,
    "items": [{"id": "p1", "qty": 120}]
  }
  ```

## Cart
- **POST** `/api/cart/add` - Add item to cart
  ```json
  {
    "productId": "p1",
    "quantity": 50
  }
  ```
