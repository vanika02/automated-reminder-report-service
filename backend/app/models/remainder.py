from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.db.database import Base

class Remainder(Base):
    __tablename__ = "remainders"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    remind_at = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow())

