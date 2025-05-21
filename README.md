# DjangoStore

# 🛍️ DjangoStore — E-commerce API with Django REST Framework

**DjangoStore** is a RESTful API backend for an e-commerce platform, built with Django and Django REST Framework. It provides core functionalities for managing products, users, carts, and orders — ideal as a backend for web or mobile shopping applications.

---

## 🚀 Features

- 🔐 User registration, login, and JWT-based authentication
- 🛒 Product listing, creation, editing, and deletion
- 🗂️ Category management
- 🧺 Cart operations (add, remove, update items)
- 📦 Order creation and history tracking
- 🛠️ Admin interface for full control via Django admin

---

## 🧰 Tech Stack

- **Backend Framework:** Django, Django REST Framework
- **Authentication:** JWT (via `djangorestframework-simplejwt`)
- **Database:** SQLite (default) or PostgreSQL
- **Testing & Debugging:** DRF browsable API, Postman

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

````

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/djangostore.git
cd djangostore
````

### 2. Create a Virtual Environment and Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Apply Migrations

```bash
python manage.py migrate
```

### 4. Create Superuser

```bash
python manage.py createsuperuser
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

---

## 🔌 Sample API Endpoints

| Method | Endpoint              | Description         |
| ------ | --------------------- | ------------------- |
| POST   | `/api/register/`      | Register a new user |
| POST   | `/api/token/`         | Obtain JWT token    |
| GET    | `/api/products/`      | List all products   |
| POST   | `/api/cart/add/`      | Add item to cart    |
| POST   | `/api/orders/create/` | Place a new order   |

---

## ✅ Roadmap / Future Features

* [ ] Product image uploads
* [ ] Product reviews and star ratings
* [ ] Stripe/PayPal payment integration
* [ ] Wishlist support
* [ ] Inventory tracking and stock management

