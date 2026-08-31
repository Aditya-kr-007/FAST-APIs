from fastapi import FastAPI, Query

app = FastAPI()

# Example data.
# Imagine these are records coming from a database.
posts = [
    {"id": 1, "title": "Post 1"},
    {"id": 2, "title": "Post 2"},
    {"id": 3, "title": "Post 3"},
    {"id": 4, "title": "Post 4"},
    {"id": 5, "title": "Post 5"},
    {"id": 6, "title": "Post 6"},
    {"id": 7, "title": "Post 7"},
    {"id": 8, "title": "Post 8"},
    {"id": 9, "title": "Post 9"},
    {"id": 10, "title": "Post 10"},
    {"id": 11, "title": "Post 11"},
    {"id": 12, "title": "Post 12"},
]


@app.get("/posts")
def get_posts(
    # page means which page number you want.
    # ge=1 means page cannot be less than 1.
    page: int = Query(1, ge=1),

    # limit means how many items you want per page.
    # ge=1 means minimum 1 item.
    # le=100 means maximum 100 items.
    limit: int = Query(5, ge=1, le=100),
):
    # Count total posts.
    total_posts = len(posts)

    # Calculate total pages.
    # Example: 12 posts / 5 limit = 3 pages.
    total_pages = (total_posts + limit - 1) // limit

    # Calculate starting index.
    # page=1, limit=5 -> start_index = 0
    # page=2, limit=5 -> start_index = 5
    # page=3, limit=5 -> start_index = 10
    start_index = (page - 1) * limit

    # Calculate ending index.
    # page=1, limit=5 -> end_index = 5
    # page=2, limit=5 -> end_index = 10
    # page=3, limit=5 -> end_index = 15
    end_index = start_index + limit

    # Slice the list.
    # Python returns only items between start_index and end_index.
    paginated_posts = posts[start_index:end_index]

    return {
        "page": page,
        "limit": limit,
        "total_posts": total_posts,
        "total_pages": total_pages,
        "data": paginated_posts,
    }


# Run with:
# uvicorn pagination:app --reload
#
# Try these URLs:
# http://127.0.0.1:8000/posts
# http://127.0.0.1:8000/posts?page=1&limit=5
# http://127.0.0.1:8000/posts?page=2&limit=5
# http://127.0.0.1:8000/posts?page=3&limit=5
