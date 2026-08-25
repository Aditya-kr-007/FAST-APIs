from fastapi import FastAPI, Request
import time

app=FastAPI()

@app.middleware("http")
async def middleware_my(request:Request,call_next):
    start_time= time.time()
    responce= await call_next(request)
    process_time=time.time()-start_time
    print(f"Path:{request.url.path} | Time:{process_time}")
    return responce


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("middleware:app", host="127.0.0.1", port=8003, reload=True)
