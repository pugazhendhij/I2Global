from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    user_name: str
    user_email: EmailStr
    password: str

class UserOut(BaseModel):
    user_id: str
    user_name: str
    user_email: EmailStr
    created_on: datetime
    last_update: datetime
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    user_email: EmailStr
    password: str

class NoteCreate(BaseModel):
    note_title: str
    note_content: str

class NoteOut(BaseModel):
    note_id: str
    note_title: str
    note_content: str
    created_on: datetime
    last_update: datetime
    class Config:
        orm_mode = True
