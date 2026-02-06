from pydantic import BaseModel
from datetime import datetime

class RemainderCreate(BaseModel):
    title: str
    description: str | None = None
    remind_at: datetime

class RemainderResponse(BaseModel):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True