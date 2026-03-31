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
