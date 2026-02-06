from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.remainder import RemainderCreate, RemainderResponse
from app.services import remainder_service


router = APIRouter(prefix="/remainders", tags=["remainders"])

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()