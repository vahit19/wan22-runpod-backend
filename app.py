from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "wan22 runpod backend base is alive",
    }

@app.get("/ping")
def ping():
    return {"status": "ok"}