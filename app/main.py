from fastapi import FastAPI

app = FastAPI(title="BrokerLab API")


@app.get("/")
def root():
    return {"message": "BrokerLab API is running 🚀"}


@app.get("/health")
def health():
    return {"status": "ok"}

from fastapi import FastAPI
from app.core.database import engine, Base

app = FastAPI(title="BrokerLab API")


# cria o banco automaticamente
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "BrokerLab API is running 🚀"}


@app.get("/health")
def health():
    return {"status": "ok"}
