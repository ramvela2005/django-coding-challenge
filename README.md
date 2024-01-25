#Django Coding Challenge

**Problem Statement:**

Your company has a Django application that stores product information. Each product has a name, price, and quantity available. Your task is to create two API endpoints:

1. `GET /api/products/`: This endpoint should return a list of all products, with each product's name, price, and quantity available.

2. `POST /api/order/`: This endpoint should accept a list of products and quantities, calculate the total cost of the order, and return it. If a product doesn't exist or there isn't enough quantity available, it should return an appropriate error message.

