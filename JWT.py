from fastapi import FastAPI, Depends, HTTPException, Header
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone

app = FastAPI()

#define the secret key and algorithm to use for encoding and decoding the JWT
#JWT configuration
SECRET_KEY ="mysecretkey"
ALGORITHM = "HS256"

def create_token(data: dict):
    #create a copy of the data to encode
    to_encode = data.copy()
    #set the expiration time for the token
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    #update the data to encode with the expiration time
    to_encode.update({"exp": expire})
    #encode the data using the secret key and algorithm
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

#login API to generate a token
@app.post("/login")
def login(username: str, password: str):
    #check if the username and password are correct
    if username == "admin" and password == "1234":
        #create a token with the username as the subject
        access_token = create_token( {"sub": username} )
        return {
            "access_token": access_token
        }
    else:
        raise HTTPException(
                status_code=401, 
                detail="Invalid username or password"
        )

#TOKEN VERIFICATION
def verify_token(token: str = Header(None)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=401, 
            detail="Invalid token"
        )

#PROTECTED ROUTE
@app.get("/protected")
#here we use the verify_token function as a dependency to check if the user has a valid token before accessing the protected route
def protected_route(user=Depends(verify_token)):
    return {"message": "you have access to this protected route.",
            "user": user
    }
