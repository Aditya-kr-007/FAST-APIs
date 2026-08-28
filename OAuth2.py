from datetime import datetime, timedelta, timezone
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

app = FastAPI()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Oauth setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

#Hash Password
def hash_password(password: str):
    return pwd_context.hash(password)

#Verify Password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


#Dummy user data for demonstration purposes
fake_users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": hash_password("1234")
    }
}

#Create Token
def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

#Login API to generate a token
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=400,
            detail="Invalid username or password"
        )

    access_token = create_token({"sub": form_data.username})
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

#TOKEN VERIFICATION
def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )
        return username
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    
@app.get("/protected")
def protected_route(username: str = Depends(verify_token)):
    return {
        "message": "You have access to this protected route.",
        "user": username
    }

