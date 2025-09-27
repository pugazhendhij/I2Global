from fastapi import APIRouter, Depends, HTTPException,Query
from sqlalchemy.orm import Session
from models import Note, User
from schemas import NoteCreate, NoteOut
from database import get_db
from auth.authentication import get_current_user
from datetime import datetime
from typing import List

router = APIRouter(
    prefix="/api", 
    tags=["notes"]
)

@router.get("/list_notes",response_model=List[NoteOut])
def list_notes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
    ):
    return db.query(Note).filter(Note.owner_id == current_user.user_id).all()

@router.post("/create_note",response_model=NoteOut)
def create_note(payload: NoteCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note = Note(
        note_title=payload.note_title,
        note_content=payload.note_content,
        owner_id=current_user.user_id
    )
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


@router.get("/get", response_model=NoteOut)
def get_note(
    note_id: str = Query(..., description="ID of the note to fetch"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    note = db.query(Note).filter(Note.note_id == note_id, Note.owner_id == current_user.user_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.put("/update/{note_id}", response_model=NoteOut)
def update_note(note_id: str, payload: NoteCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note = db.query(Note).filter(Note.note_id == note_id, Note.owner_id == current_user.user_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    note.note_title = payload.note_title
    note.note_content = payload.note_content
    note.last_update = datetime.utcnow()
    db.commit()
    db.refresh(note)
    return note

@router.delete("/delete/{note_id}")
def delete_note(note_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note = db.query(Note).filter(Note.note_id == note_id, Note.owner_id == current_user.user_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return {"success": True,"message":"Note has been deleted successfully"}
