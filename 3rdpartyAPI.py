from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

#GET all data
@app.get("/posts")
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Error fetching posts")

#GET data by ID
@app.get("/posts/{post_id}")    
def get_post_by_id(post_id: int):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(
            status_code=404, 
            detail="Post not found"
     )