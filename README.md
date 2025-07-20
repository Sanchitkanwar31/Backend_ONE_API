# 🛒 HROne E‑Commerce Backend API

This project is a sample backend service for an e-commerce platform like Flipkart/Amazon. It allows for creating and retrieving products and managing orders using FastAPI and MongoDB.

---

##  Tech Stack

* **Language**: Python 3.10+
* **Framework**: FastAPI
* **Database**: MongoDB Atlas (M0 free cluster)
* **ODM/Driver**: PyMongo
* **Deployment**: Render (Can take 1 min to run bcz of free tier)

---

##  Project Structure

```
app/
├── __init__.py
├── main.py              # FastAPI app entry point
├── database.py          # MongoDB connection setup
├── models.py            # Pydantic models
└── routes/
    ├── products.py      # /products routes
    └── orders.py        # /orders routes

.env                    # MongoDB URI
requirements.txt        # Dependencies
README.md               # Project documentation
```

---

##  API Endpoints

###  Product APIs

####  Create Product

* **Endpoint**: `POST /products`
* **Request Body**:

```json
{
  "name": "T-Shirt",
  "price": 499.0,
  "sizes": [
    { "size": "M", "quantity": 10 },
    { "size": "L", "quantity": 5 }
  ]
}
```

* **Response**: `{ "id": "<product_id>" }`
* **Status**: `201 CREATED`

####  List Products

* **Endpoint**: `GET /products`
* **Query Params**: `name`, `size`, `limit`, `offset`
* **Response**:

```json
{
  "data": [
    { "id": "...", "name": "...", "price": 499.0 }
  ],
  "page": {
    "next": 10,
    "limit": 5,
    "previous": 0
  }
}
```

---

###  Order APIs

####  Create Order

* **Endpoint**: `POST /orders`
* **Request Body**:

```json
{
  "user_id": "user_3",
  "items": [
    { "productId": "<product_id>", "qty": 2 },
    { "productId": "<product_id>", "qty": 1 }
  ]
}
```

* **Response**: `{ "id": "<order_id>" }`
* **Status**: `201 CREATED`

####  Get Orders by User

* **Endpoint**: `GET /orders/{user_id}`
* **Query Params**: `limit`, `offset`
* **Response**:

```json
{
  "data": [
    {
      "id": "<order_id>",
      "items": [
        {
          "productDetails": { "name": "T-Shirt", "id": "..." },
          "qty": 2
        }
      ]
    }
  ],
  "total": 1497.0,
  "page": {
    "next": 10,
    "limit": 5,
    "previous": 0
  }
}
```

---

##  Setup Instructions

1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Set your `.env` file:

   ```env
   MONGO_URL=mongodb+srv://<username>:<password>@cluster.mongodb.net/hrone_db
   ```
5. Run the app:

   ```bash
   uvicorn app.main:app 
   ```
6. Visit: `http://localhost:8000/docs`

---

##  Deployment

Deploy your app to **Render** or **Railway** using a free plan. Share only the base URL (e.g., `https://backend-hrone-api.onrender.com/`).

---

##  Checklist for Submission

* [x] All endpoints work and follow spec
* [x] MongoDB optimized queries and pagination
* [x] Clean, structured code
* [x] Public GitHub repo with README
* [x] `.env` excluded via `.gitignore`

---

>  Built by \[Sanchit Kanwar] for HROne Backend Task 
