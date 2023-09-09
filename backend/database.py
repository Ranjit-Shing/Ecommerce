
import motor.motor_asyncio
from model import AddToCart


client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

database = client.AddToCart

collection= database.create_collection

async def fetch_one_cart(Items):
    document = await collection.find_one({"Items":Items})
    return document

async def fetch_all_cart():
    cart= []
    cursor = collection.find({})
    async for document in cursor:
        cart.append (cart(**document))
    return cart

async def create_cart(cart):
    document = cart
    result = await collection.insert_one(document)
    return result

async def update_cart(Item,Price,Quantity):
    await collection.update_one({Item:Item},{"$set":{"Price":Price,"Quantity":Quantity}})
    document = await collection.find_one({"Item":Item})
    return document

async def remove_cart(Item):
    await collection.delete_one({"Item":Item})
    return True
