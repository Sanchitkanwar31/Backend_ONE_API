from fastapi import APIRouter, status, Query
from app.models import OrderItemOut,OrderOut
from app.database import orders_collection, products_collection
from bson import ObjectId
# from datetime import datetime

router = APIRouter()



#CREATE order using {product_Id=<Object_id>} of Sample Product 
#---------------------------------------------------------------------------
# @router.post("/orders", status_code=status.HTTP_201_CREATED)
# def create_order(order: OrderItemOut):
#     order_data = {
#         "userId": order.userId,
#         "items": [item.dict() for item in order.items],
#     }
#     result = orders_collection.insert_one(order_data)
#     return {"id": str(result.inserted_id)}

from datetime import datetime

router = APIRouter()
@router.post("/orders", status_code=status.HTTP_201_CREATED)
def create_or_update_order(order: OrderOut):
    new_items = [item.dict() for item in order.items]  # ← changed from order.products

    result = orders_collection.update_one(
        {"userId": order.user_id},
        {
            "$push": {"items": {"$each": new_items}},
            "$setOnInsert": {"created_at": datetime.now()}
        },
        upsert=True
    )

    updated_doc = orders_collection.find_one({"userId": order.user_id})
    return {"id": str(updated_doc["_id"])}


# #Get Order of product using <user_id>-----------------------------------------


@router.get("/orders/{user_id}")
def get_orders(
    user_id: str,
    limit: int = Query(10),
    offset: int = Query(0)
):
    query = {"userId": user_id}
    orders_cursor = orders_collection.find(query).skip(offset).limit(limit)

    response_data = []
    final_total = 0.0

    for order in orders_cursor:
        enriched_items = []
        total_price = 0.0

        for item in order.get("items", []):
            product_id = item.get("productId")
            quantity = item.get("qty", 0)

            product = products_collection.find_one({"_id": ObjectId(product_id)})
            if product:
                price = product.get("price", 0)
                total_price += price * quantity

                enriched_items.append({
                    "productDetails": {
                        "name": product["name"],
                        "id": str(product["_id"])
                    },
                    "qty": quantity
                })

        #  Only after order's items processed
        final_total += total_price

        response_data.append({
            "id": str(order["_id"]),
            "items": enriched_items,
        })

    return {
        "data": response_data,
        "total": round(final_total, 2),
        "page": {
            "next": offset + limit,
            "limit": len(enriched_items),
            "previous": offset - limit
        }
    }
