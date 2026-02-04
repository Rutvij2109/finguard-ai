from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Event(BaseModel):
    resource_type: str
    instance_type: str
    region: str

@app.get("/")
def home():
    return {"message": "FinGuard AI backend running"}

@app.post("/event")
def receive_event(event: Event):
    print("Received event:", event)
    return {"status": "event received"}
