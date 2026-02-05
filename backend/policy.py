TEAM_MONTHLY_BUDGET = 500  # example budget


def evaluate_policy(predicted_cost: float):
    if predicted_cost > TEAM_MONTHLY_BUDGET:
        return "BLOCK"
    else:
        return "ALLOW"
