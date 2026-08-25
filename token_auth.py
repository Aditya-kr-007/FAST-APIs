from fastapi import FastAPI, Depends, Header, HTTPException

app=FastAPI()

def verify_token(token:str=Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(
            status_code= 401,
            detail="Unauthorized"
        )
    return {
        "user":"Authenticated"
    }

@app.get("/secure")
def secure_data(user=Depends(verify_token)):
    return{
        "msg":"Secure data accessed",
        "user":user
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("token_auth:app", host="127.0.0.1", port=8004, reload=True)
