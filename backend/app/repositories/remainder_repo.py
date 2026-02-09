from sqlalchemy.orm import Session
from app.models.remainder import Remainder
from sqlalchemy import func
from datetime import date

def create_remainder(db:Session, remainder: Remainder):
    db.add(remainder)
    db.commit()
    db.refresh(remainder)
    return remainder

def get_reminders(db: Session):
    return db.query(Remainder).all()