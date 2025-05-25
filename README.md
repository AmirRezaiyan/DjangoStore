# 🛍️ DjangoStore — E-commerce API with Django REST Framework

**DjangoStore** is a RESTful API backend for an e-commerce platform, built with Django and Django REST Framework. It provides core functionalities for managing products, users, carts, and orders — ideal as a backend for web or mobile shopping applications.

---

## 🚀 Features

* 🔐 User registration, login, and JWT-based authentication
* 🛒 Product listing, creation, editing, and deletion
* 🗂️ Category management
* 🧺 Cart operations (add, remove, update items)
* 📦 Order creation and history tracking
* 🛠️ Admin interface for full control via Django admin

---

## 🧰 Tech Stack

* **Backend Framework:** Django 5.x, Django REST Framework
* **Language:** Python 3.13
* **Authentication:** JWT (via `djangorestframework-simplejwt`)
* **Database:** SQLite (default) or PostgreSQL
* **Testing:** Postman (for all endpoints)
* **Deployment (Planned):** Railway + Cloudflare

---

## 📁 Project Structure

```
djangostore/
├── djangostore/       # Project configuration and settings
├── users/             # Authentication and user management
├── products/          # Product and category logic
├── cart/              # Shopping cart functionality
├── orders/            # Order processing
├── manage.py
```

---

## ⚙️ Getting Started

```bash
git clone https://github.com/your-username/djangostore.git
cd djangostore
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🛠️ Admin Panel

Visit: `http://localhost:8000/admin/`

Use Django Admin to manage:

* Products
* Categories
* Cart & Cart Items
* Orders & Order Items

---

## 🔐 Authentication Endpoints

| Method | Endpoint         | Description         |
| ------ | ---------------- | ------------------- |
| POST   | `/api/register/` | Register a new user |
| POST   | `/api/token/`    | Get JWT auth token  |

### 🧪 Example Requests

#### Register

```http
POST /api/register/
Content-Type: application/json

{
  "email": "test@example.com",
  "username": "testuser",
  "password": "securepassword"
}
```

#### Get Token

```http
POST /api/token/
Content-Type: application/json

{
  "email": "test@example.com",
  "password": "securepassword"
}
```

**Use Token in Headers:**

```http
Authorization: Token your-auth-token
```

---

## 🛒 Cart Endpoints

### 📥 Add to Cart

```http
POST /api/cart/
Authorization: Token <your-token>
Content-Type: application/json

{
  "product_id": 3,
  "quantity": 4
}
```

### 🔄 Update Quantity

```http
PATCH /api/cart/update/2/
Authorization: Token <your-token>
Content-Type: application/json

{
  "quantity": 2
}
```

### ❌ Remove from Cart

```http
DELETE /api/cart/remove/2/
Authorization: Token <your-token>
```

### 📃 View Cart

```http
GET /api/cart/
Authorization: Token <your-token>
```

#### Example Response:

```json
{
  "id": 1,
  "user": 1,
  "items": [
    {
      "id": 2,
      "product": 3,
      "product_name": "iPhone 14 Pro Max",
      "quantity": 4
    },
    {
      "id": 3,
      "product": 4,
      "product_name": "iPhone 13 Pro Max",
      "quantity": 3
    }
  ]
}
```

---

## 📦 Orders Endpoints

### 🧾 Create Order

```http
POST /api/orders/
Authorization: Token <your-token>
```

#### Example Response:

```json
{
  "id": 1,
  "created_at": "2025-05-25T07:50:55.969834Z",
  "is_paid": false,
  "items": [
    {
      "id": 1,
      "product": 3,
      "product_name": "iPhone 14 Pro Max",
      "quantity": 4
    },
    {
      "id": 2,
      "product": 4,
      "product_name": "iPhone 13 Pro Max",
      "quantity": 3
    }
  ],
  "total_items": 7
}
```

### 📄 List Orders

```http
GET /api/orders/
Authorization: Token <your-token>
```

---

## ✅ Feature Summary

* 👤 User Register & Login (JWT Auth)
* 🛒 Cart: Add / Update / Remove Items
* 📦 Orders: Create and Track Orders
* 🛠️ Admin Panel: Full control via Django Admin
* 🧪 API Fully tested via Postman

---

## 🌍 Deployment Plan (Upcoming)

* ✅ Finalize all local tests
* 🔐 Optional: JWT enhancements
* ☁️ Deploy to Railway
* 🌐 Connect domain and secure with Cloudflare
