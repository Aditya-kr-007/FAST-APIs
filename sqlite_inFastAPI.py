import sqlite3
from fastapi import FastAPI
app= FastAPI()

conn=sqlite3.connect("test.db",check_same_thread=False) #connecting to the database and creating a connection object
cursor=conn.cursor()    #creating a cursor object to execute SQL commands
     #executing SQL command to create a table if it doesn't exist
cursor.execute("""                         
CREATE TABLE IF NOT EXISTS todos(
     id INTEGER PRIMARY KEY,
     title TEXT,
     completed TEXT
    )
""")
conn.commit()  #committing the changes to the database
@app.get("/")
def home():
    return {
        "message":"SQLite connected successfully"
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("sqlite_inFastAPI:app", host="127.0.0.1", port=8002, reload=True)

