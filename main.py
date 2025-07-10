from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
import secrets

app = FastAPI()
security = HTTPBasic()

# Tạm lưu user/pw trong dict memory
users_db = {}

# Model cho đăng ký user
class UserRegister(BaseModel):
    username: str
    password: str

@app.post("/register")
def register_user(user: UserRegister):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    users_db[user.username] = user.password
    return {"message": "User registered successfully"}

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_password = users_db.get(credentials.username)
    if not correct_password or not secrets.compare_digest(credentials.password, correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/balance")
def get_balance(username: str = Depends(get_current_username)):
    # Luôn trả về 100 đô
    return {"username": username, "balance": 100}
