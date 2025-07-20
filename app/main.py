from fastapi import FastAPI
from app.routes import products, orders

app = FastAPI(
    title="HROne Backend Intern API",
    version="1.0.0"
)

# Register routes
app.include_router(products.router)
app.include_router(orders.router)

# health status route
@app.get("/status")
def root():
    return {"message": "HROne API is up and running!"}
