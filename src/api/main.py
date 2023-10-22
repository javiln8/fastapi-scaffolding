from fastapi import FastAPI
from src.api.V1.routes import router as v1_router

app = FastAPI()

app.include_router(v1_router, prefix="/api/V1")
