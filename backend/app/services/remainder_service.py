from sqlalchemy.orm import Session
from app.models.remainder import Remainder
from app.repositories import remainder_repo

def create_remainder(db: Session, data):
    remainder = Remainder(**data)
    return remainder_repo.create_remainder(db, remainder)

def list_remainders(db: Session):
    return remainder_repo.get_reminders(db)

def log_remainder_created(remainder_id: int):
    print(f"Remainder created with id: {remainder_id}")

# Reminder analytics
def get_analytics(db: Session):
    return {
        "total": remainder_repo.count_all(db),
        "active": remainder_repo.count_active(db),
        "inactive": remainder_repo.count_all
    }