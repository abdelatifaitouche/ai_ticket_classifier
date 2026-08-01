from fastapi import FastAPI
from src.api.routes import router as api

app = FastAPI()

app.include_router(api)


@app.get("/health")
def health():
    return "healthing"
