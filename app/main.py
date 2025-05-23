from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from pymongo import MongoClient
from bson.objectid import ObjectId

app = FastAPI()

# MongoDB connection
client = MongoClient("mongodb+srv://annamammedowkowus:kowus123@cluster0.hhs5lqc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["infomatrix"]
products_col = db["products"]

class ProductAdd(BaseModel):
    name: str
    price: int
    quantity: int

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None
    quantity: Optional[int] = None

@app.get("/")
def read_root():
    return {"message": "nonesense"}

@app.get("/get-product/{product_id}")
def get_product(product_id: str):
    product = products_col.find_one({"_id": ObjectId(product_id)})
    if not product:
        raise HTTPException(status_code=404, detail="Id not exists")
    return {"price": product["price"]}

@app.get("/get-by-name")
def get_by_name(name: str):
    product = products_col.find_one({"name": name})
    if not product:
        raise HTTPException(status_code=404, detail="Data not found")
    return {"price": product["price"]}

@app.post("/add-product/")
def add_product(product: ProductAdd):
    existing = products_col.find_one({"name": product.name})
    if existing:
        raise HTTPException(status_code=400, detail="Name already exists")
    result = products_col.insert_one(product.dict())
    return {"_id": str(result.inserted_id), **product.dict()}

@app.put("/update-product/{product_id}")
def update_product(product_id: str, product: ProductUpdate):
    update_data = {k: v for k, v in product.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No data to update")
    result = products_col.update_one({"_id": ObjectId(product_id)}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Id not exists")
    updated = products_col.find_one({"_id": ObjectId(product_id)})
    return {"_id": product_id, **{k: updated[k] for k in ["name", "price", "quantity"]}}

@app.delete("/delete-product/{product_id}")
def delete_product(product_id: str):
    result = products_col.delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Id doesn't exist")
    return {"deleted": product_id}