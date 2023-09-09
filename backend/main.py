from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time
from fastapi import Request
from fastapi import HTTPException


app = FastAPI()

from database import (
    fetch_one_cart,
    fetch_all_cart,
    create_cart,
    update_cart,
    remove_cart,
)



app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/")
async def read_root():
    return {"Hello": "World"}

#cart 

@app.get("/api/cart")
async def get_cart():
    response = await fetch_all_cart()
    return response

@app.get("/api/cart{Item}")
async def get_cart_by_id(Item):
    response = await fetch_one_cart(Item)
    if response:
        return response
    raise HTTPException (404,f"There is no cart{Item}")

@app.post("/api/cart")
async def post_cart(cart):
    response = await create_cart(cart.Item)
    if response:
        return response
    raise HTTPException (404,"Something Wrong")

@app.put("/api/cart{Item}/")
async def put_cart(Item:str,Price:int,Quantity:int):
    response = await update_cart(Item,Price,Quantity)
    if response:
        return response
    raise HTTPException (404,"Opps Error{Item}")


@app.delete("/api/cart")
async def delete_cart(Item):
    response = await remove_cart(Item)
    if response:
        return "Done"
    raise HTTPException (404,"Try again")
