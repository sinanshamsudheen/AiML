from fastapi import FastAPI
from enum import Enum
app=FastAPI()

# Benifits over flaskAPI,
# 1- Offers inbuilt data validation
# 2- Inbuilt documentation; url+/docs or url+redoc
# 3- As fast as Node.js
# 4- easy and compact codes
# 5- easy to debug

# HTTPS REST PROTOCOL KEYWORDS.,
# GET- to read data ; show me iphone covers
# POST - to create data; create new order
# PUT - update data; update an order
# DELETE - delete data; delete an order

food_items={
    "indian":['samosa','dosa'],
    "american":['falooda','burger'],
    'italian':['pasta','custard']
}
valid_cuisines=food_items.keys()

class AvailableCuisines(str, Enum):
    indian="indian"
    american="american"
    italian="italian"

coupon_codes={
    1:"10%",
    2:"20%",
    3:"30%"
}
@app.get("/get_items/{cuisine}")
# async def Hello(name):
#     return f"Welcome To FastAPI {name}"

#for flask we have to do it like this,
# async def get_items(cuisine):
#     if cuisine not in valid_cuisines:
#         return f"Only supported options are {valid_cuisines}!!"
#     return food_items.get(cuisine)

#but for fastAPI, we can easily..
async def get_items(cuisine: AvailableCuisines):
    return food_items.get(cuisine)

@app.get("/get_coupon/{code}")
async def get_coupon(code: int):
    return coupon_codes.get(code)
