from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URI = "sqlite:///./remainders.db"

engine = create_engine(
    DATABASE_URI, connect_args={"check_same_thread": False}
)

sessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()