import sqlite3
from fastapi import FastAPI
app= FastAPI()

conn=sqlite3.connect("test.db",check_same_thread=False)
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS todos(
     id INTEGER PRIMARY KEY,
     title TEXT,
     completed TEXT
    )
""")
conn.commit()
@app.get("/")
def home():
    return {
        "message":"SQLite connected successfully"
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("sqlite_inFastAPI:app", host="127.0.0.1", port=8002, reload=True)

