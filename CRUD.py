from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos=[]

class Todo(BaseModel):   #table structure for todo
    id: int
    task: str
    completed: bool

@app.post("/TODO")            #using post method to create a todo
def create_todo(todo: Todo):  #getting todo from request body
    todos.append(todo)        #appending the todo to the list
    return {
        "message": "todo added",
        "data": todo
    }

@app.get("/TODO") #getting all todos
def get_todo():
    return todos

@app.get("/TODO/{todo_id}") #getting todo by id
def get_todos(todo_id:int):
    for todo in todos:        #iterating through the list of todos
        if todo.id==todo_id:  #if todo id matches the requested id, return the todo
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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("CRUD:app", host="127.0.0.1", port=8000, reload=True)
