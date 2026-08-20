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