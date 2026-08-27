from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

# Define the database URL and create the SQLAlchemy engine
DATABASE_URL = "sqlite:///./tests.db"

# Create the SQLAlchemy engine and session
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
# Create a local session factory
SessionLocal = sessionmaker(bind=engine)

# Create the base class for the ORM models
Base = declarative_base()

# Define the Todo model
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# DATABASE CONNECTION TEST
@app.get("/")
def home(db: Session = Depends(get_db)):
    return {
        "message": "DB connected fine"
    }

# CREATE
@app.post("/todos")
def create_todo(title: str, db: Session = Depends(get_db)):
    todo = Todo(title=title, completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message": "Todo Created",
        "data": todo
    }
# READ
@app.get("/todos")
def get_todos(db:Session=Depends(get_db)):
    all_todo = db.query(Todo).all()
    return {
        "total":len(all_todo),
        "data":all_todo
    }
# READ THROUGH PATH
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(
            status_code=404,
            detail="not found"
        )
    return todo
# UPDATE
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, title: str, db: Session= Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first() 
    if not todo:
        raise HTTPException(
            status_code=404,
            detail="NOT FOUND"
        )
    todo.title=title
    db.commit()
    db.refresh(todo)
    return {
        "message":"Todo Updated",
        "data":todo
    }
  # DELETE
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int, db: Session=Depends(get_db)):     
    todo=db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo:
        raise HTTPException(
            status_code=404,
            detail="NOT FOUND"
        )
    db.delete(todo)
    db.commit()
    return {
        "message":"Todo Deleted"
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("sqlalchemyCRUD:app", host="127.0.0.1", port=8001, reload=True)
