from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
import hashlib
import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from pathlib import Path

ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
JWT_SECRET = quote_plus(os.getenv("JWT_SECRET"))


dotenv_path = Path(__file__).resolve().parent / ".env"
if dotenv_path.exists():
    load_dotenv(dotenv_path)

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)

def preprocess(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def hash_password(password: str) -> str:
    return pwd_context.hash(preprocess(password[:72]))


def verify_password(plain, hashed) -> bool:
    return pwd_context.verify(preprocess(plain[:72]), hashed)

def create_access_token(subject: str):
    expire = datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode = {"sub": subject, "exp": expire}
    return jwt.encode(to_encode, JWT_SECRET, algorithm="HS256")

def decode_token(token: str):
    return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
