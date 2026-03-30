from fastapi import FastAPI

app = FastAPI(title="BrokerLab API")


@app.get("/")
def root():
    return {"message": "BrokerLab API is running 🚀"}


@app.get("/health")
def health():
    return {"status": "ok"}
