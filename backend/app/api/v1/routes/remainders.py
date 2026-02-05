from fastapi import FastAPI

router = APIRouter(prefix="/remainders", tags=["remainders"])

@router.get("/ping")
def ping():
    return {"message": "Remainder service is up now!"}