from fastapi import FastAPI
from app.core.database import engine, Base
from app.models.user import User  # 👈 ESSA LINHA É O SEGREDO

app = FastAPI(title="BrokerLab API")

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "BrokerLab API is running 🚀"}


@app.get("/health")
def health():
    return {"status": "ok"}

from app.api.user import router as user_router

app.include_router(user_router)
