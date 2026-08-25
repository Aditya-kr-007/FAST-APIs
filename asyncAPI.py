import time
import asyncio
from fastapi import FastAPI

app= FastAPI()

@app.get("/")
async def long_running_task():
    await asyncio.sleep(5)  # Simulate a long-running task
    return {"message": "Task completed"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("asyncAPI:app", host="127.0.0.1", port=8005, reload=True)
