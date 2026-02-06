from app.db.database import engine
from app.models.remainder import Remainder

Remainder.metadata.create_all(bind=engine)