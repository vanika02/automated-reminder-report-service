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

# Total Remainders count
def count_all(db: Session):
    return db.query(func.count()).select_from(Remainder).scalar()

# Total Active Reminders 
def count_active(db: Session):
    return db.query(func.count()).filter(Remainder.is_active == True).scalar()

# Total In-Active Reminders 
def count_active(db: Session):
    return db.query(func.count()).filter(Remainder.is_active == False).scalar()


# Today Reminders 
def count_today(db: Session):
    return (db.query(func.count()).filter(func.date(Remainder.created_at) == date.today()).scalar())