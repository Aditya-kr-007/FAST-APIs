from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "title": "Sony Software",
        "body": "Amazing SW environment",
        "content": "FastAPI framework is really easy to use and super",
        "date_posted": "April 21, 2025",
    },
    {
        "id": 2,
        "title": "Demo Post",
        "body": "Welcome to great for web development",
        "content": "FastAPI is a great framework for web development",
        "date_posted": "April 22, 2025",
    },
]


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"

@app.get("/api/posts")
def get_posts():
    return posts