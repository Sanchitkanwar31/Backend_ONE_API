from fastapi import APIRouter, Query, status
from typing import Optional
from app.models import ProductCreate
from app.database import products_collection
from bson import ObjectId

router = APIRouter()

#Create a product = <sample prodct>  
#------------------------------------------------------------------------------
@router.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    result = products_collection.insert_one(product.dict())
    return {"id": str(result.inserted_id)}



#Get Products based on filter ={nme,size}
#------------------------------------------------------------------------------
@router.get("/products")
def list_products(
    name: Optional[str] = Query(None),
    size: Optional[str] = Query(None),
    limit: int = 10,
    offset: int = 0
):
    query = {}
    # to find product with 'name' in any form of product(regex) OR size 
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes.size"] = size
    projection = {"sizes": 0}  

    cursor = products_collection.find(query, projection).skip(offset).limit(limit)

    data = [
        {"id": str(doc["_id"]), "name": doc["name"], "price": doc["price"]}
        for doc in cursor
    ]

    return {
        "data": data,
        "page": {
            "next": offset + limit,
            "limit": len(data),
            "previous":  offset - limit #max(0, offset - limit)
        }
    }

    