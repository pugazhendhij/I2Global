from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from notes_app.router import router as notes_routes
from auth.authentication import router as auth_routes
from database import Base, engine


app = FastAPI(title="Notes API - MySQL")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_routes)
app.include_router(notes_routes)

@app.get("/")
def root():
    return {"message": "Application is Running"}
