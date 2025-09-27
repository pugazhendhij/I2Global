from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from database import Base

def now():
    return datetime.utcnow()

class User(Base):
    __tablename__ = "users"

    user_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_name = Column(String(100), nullable=False)
    user_email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_on = Column(DateTime, default=now)
    last_update = Column(DateTime, default=now, onupdate=now)

    notes = relationship("Note", back_populates="owner")

class Note(Base):
    __tablename__ = "notes"

    note_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    note_title = Column(String(200), nullable=False)
    note_content = Column(Text, nullable=False)
    created_on = Column(DateTime, default=now)
    last_update = Column(DateTime, default=now, onupdate=now)
    owner_id = Column(String(36), ForeignKey("users.user_id"))

    owner = relationship("User", back_populates="notes")
