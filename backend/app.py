from fastapi import FastAPI
from pydantic import BaseModel
from cost_predictor import predict_monthly_cost
from policy import evaluate_policy

app = FastAPI()
@app.get("/")
def home():
    return {"message": "FinGuard AI backend running"}

class Event(BaseModel):
    resource_type: str
    instance_type: str
    region: str

@app.post("/event")
def receive_event(event: Event):
    cost = predict_monthly_cost(event.instance_type)
    decision = evaluate_policy(cost)

    return {
        "status": "event received",
        "predicted_monthly_cost": cost,
        "decision": decision
    }