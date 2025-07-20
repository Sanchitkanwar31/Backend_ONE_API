from pymongo import MongoClient, errors
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

try:
    client = MongoClient(MONGO_URL)
    client.server_info()  
    print("MongoDB connected")

    db = client["hrone_db"]
    products_collection = db["products"]
    orders_collection = db["orders"]

except Exception:
    print("Mongo Connection failed",Exception)
