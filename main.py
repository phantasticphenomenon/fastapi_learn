import string
# Import FastAPI
from fastapi import FastAPI

# Create an instance of fastapi
app = FastAPI()

# Create an operational decorator
@app.get("/")
# Create an operational funtion
async def root():
    return {"message": "Hello World"}

# Create an operation decorator (url)
@app.get("/items/{item_id}")
# Create an operational function
async def read_item(item_id):
    return {"item_id": item_id}

