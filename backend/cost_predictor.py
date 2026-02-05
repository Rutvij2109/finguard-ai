INSTANCE_PRICES = {
    "t3.micro": 0.01,
    "t3.large": 0.08,
    "g5.xlarge": 1.2,
    "g5.2xlarge": 2.3
}

def predict_monthly_cost(instance_type: str):
    hourly_price = INSTANCE_PRICES.get(instance_type, 0.1)
    monthly_cost = hourly_price * 24 * 30
    return round(monthly_cost, 2)
