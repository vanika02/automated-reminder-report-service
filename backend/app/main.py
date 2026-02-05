from fastapi import FastAPI
from app.api.v1.routes import remainders


app = FastAPI(title="Remainder Service")

app.include_router(remainders.router, prefix="/api/v1")