from fastapi import FastAPI
from app.api.v1.routes import remainders, analytics
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Remainder Service")

app.include_router(remainders.router, prefix="/api/v1")
app.include_router(analytics.router, prefix="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)