from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos=[]

class Todo(BaseModel):
    id: int
    task: str
    completed: bool

@app.post("/TODO")
def create_todo(todo: Todo):
    todos.append(todo)
    return {
        "message": "todo added",
        "data": todo
    }

@app.get("/TODO")
def get_todo():
    return todos

@app.get("/TODO/{todo_id}")
def get_todos(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            return todo
    return {"ERROR":"Todo not found"}

@app.put("/TODO/{todo_id}")
def update_todo(todo_id:int ,updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos[index]=updated_todo
            return {"message":"UPDATED"}
    return {"ERROR":"todo not found"}

@app.delete("/TODO/{todo_id}")
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos.pop(index)
            return {"message":"DELETED"}
    return {"ERROR":"todo not found"}
