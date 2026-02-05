import streamlit as st
import requests

# ---------- PAGE HEADER ----------
st.title("🚨 FinGuard AI")
st.subheader("Real-Time Cloud Cost Protection")

st.caption("FinGuard AI intercepts risky cloud deployments before cost damage occurs.")

st.write("Simulate a cloud deployment and evaluate its financial risk instantly.")

# ---------- INPUT ----------
instance_type = st.selectbox(
    "Choose Instance Type",
    ["t3.micro", "t3.large", "g5.xlarge", "g5.2xlarge"]
)

# ---------- ACTION ----------
if st.button("Simulate Deployment"):

    event = {
        "resource_type": "EC2",
        "instance_type": instance_type,
        "region": "ap-south-1"
    }

    response = requests.post(
        "http://127.0.0.1:8000/event",
        json=event
    )

    data = response.json()

    cost = data["predicted_monthly_cost"]
    decision = data["decision"]
    reason = data.get("reason", "Policy threshold exceeded.")

    # ==============================
    # 🔥 DECISION FIRST (Authority UI)
    # ==============================

    if decision == "BLOCK":
        st.error("⛔ DEPLOYMENT BLOCKED")

    else:
        st.success("✅ DEPLOYMENT APPROVED")

    # ==============================
    # Risk AFTER decision
    # ==============================

    if cost > 1500:
        risk = "CRITICAL"
    elif cost > 700:
        risk = "HIGH"
    else:
        risk = "SAFE"

    st.markdown(f"### Risk Level: **{risk}**")

    # ==============================
    # Cost
    # ==============================

    st.markdown(f"### 💰 Predicted Monthly Cost: **${cost}**")

    # ==============================
    # Reason
    # ==============================

    st.write(f"**Reason:** {reason}")
