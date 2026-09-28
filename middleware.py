from fastapi import FastAPI, Request
import time

app=FastAPI()

@app.middleware("http")
async def middleware_my(request:Request,call_next):   #async function is used to handle multiple requests processing at the same time
                                                      #call_next is a function that will call the next middleware or route handler in the chain
    start_time= time.time()                           #time before the request is processed
    response= await call_next(request)                #wait for the next middleware or route handler to process the request
    process_time=time.time()-start_time               #time taken to process the request
    print(f"Path:{request.url.path} | Time:{process_time}")  #print the path and processing time
    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("middleware:app", host="127.0.0.1", port=8003, reload=True)
