from fastapi import APIRouter, Depends, BackgroundTasks
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

@router.post("/", response_model=RemainderResponse)
def create(remainder: RemainderCreate, db: Session = Depends(get_db)):
    return remainder_service.create_remainder(db, remainder.dict())

@router.get("/", response_model=list[RemainderResponse])
def list_all(db: Session = Depends(get_db)):
    return remainder_service.list_remainders(db)

@router.post("/", response_model=RemainderResponse)
async def create(remainder: RemainderCreate, db: Session = Depends(get_db), backgorund_tasks = BackgroundTasks):
    result = remainder_service.create_remainder(db, remainder.dict())

    backgorund_tasks.add_task(
        remainder_service.log_remainder_created,
        result.id
    )
    return result