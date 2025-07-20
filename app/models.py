from typing import List
from pydantic import BaseModel, Field

# --- Product Models ---

class SizeQ(BaseModel):
    size: str
    quantity: int

class ProductCreate(BaseModel):
    name: str
    price: float = Field(100.0)
    sizes: List[SizeQ]

class ProductOut(BaseModel):
    id: str
    name: str
    price: float


# --- Order Models ---

class ProductDetails(BaseModel):
    productId: str
    qty: int = Field(3)

class OrderItemOut(BaseModel):
    userId: str 
    items: List[ProductDetails]
    

class OrderOut(BaseModel):
    user_id: str
    items: List[ProductDetails]
