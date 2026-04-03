from fastapi import FastAPI
from app.core.database import engine, Base
from app.models.user import User
from app.api.user import router as user_router

app = FastAPI(title="BrokerLab API")

Base.metadata.create_all(bind=engine)

app.include_router(user_router)


@app.get("/")
def root():
    return {"message": "BrokerLab API is running 🚀"}


@app.get("/health")
def health():
    return {"status": "ok"}
