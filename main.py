from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    email:str

@app.get("/users") 
def get_user(name: str = None ):
    return {"Name":name}

@app.get("/products")
def get_user(limit: int = 10):
    return {"limit":limit}

@app.get("/items")
def get_user(name:str=None,price: int=0):
    return {
        "Name":name,
        "price":price
    }


@app.post("/create-user")
def create_user(user:User):
    return {
        "message":"user created",
        "data":user
        }
