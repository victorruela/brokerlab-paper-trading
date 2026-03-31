from fastapi import FastAPI
from app.core.database import engine, Base
from app.models.user import User  # IMPORTANTE

app = FastAPI(title="BrokerLab API")

Base.metadata.create_all(bind=engine)
