from fastapi import FastAPI

app = FastAPI()


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
