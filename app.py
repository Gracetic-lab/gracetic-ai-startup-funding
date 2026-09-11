import streamlit as st
import pandas as pd
import joblib

# ==========================================
# GRACETIC AI
# Intelligent Systems for the Future
# ==========================================

model = joblib.load("gracetic_startup_funding_model.pkl")

st.set_page_config(
    page_title="Gracetic AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Gracetic AI")
st.subheader("Intelligent Systems for the Future")
st.write("🌍 AI-powered global startup funding prediction system.")

st.divider()

st.header("Startup Information")

valuation = st.number_input(
    "Startup Valuation (USD Millions)",
    min_value=0.0,
    value=10.0,
    step=0.1
)

age = st.number_input(
    "Startup Age (Years)",
    min_value=0.0,
    value=5.0,
    step=1.0
)

burn_rate = st.number_input(
    "Monthly Burn Rate (USD Millions)",
    min_value=0.0,
    value=1.0,
    step=0.1
)

city = st.text_input(
    "Startup City",
    placeholder="e.g. Kampala, Tokyo, Berlin, São Paulo"
)

domain = st.text_input(
    "Startup Domain",
    placeholder="e.g. FinTech, AgriTech, AI, Biotech"
)

country = st.text_input(
    "Country",
    placeholder="e.g. Uganda, Japan, Germany, Brazil"
)

st.divider()

if st.button("🚀 Predict Funding", use_container_width=True):

    if not city or not domain or not country:
        st.warning("Please enter the city, domain, and country.")
    else:
        user_data = pd.DataFrame({
            "Valuation_USD_Millions": [valuation],
            "Startup_Age": [age],
            "Monthly_Burn_Rate_Millions": [burn_rate],
            "City": [city],
            "Domain": [domain],
            "Country": [country]
        })

        try:
            prediction = model.predict(user_data)
            predicted_funding = prediction[0]

            st.success("✅ Prediction completed!")

            st.metric(
                label="Predicted Total Funding",
                value=f"${predicted_funding:,.2f} Million"
            )

            st.info(
                f"**Startup Profile:** {domain} startup in {city}, {country} | "
                f"Valuation: ${valuation}M | Age: {age} years | Burn rate: ${burn_rate}M/month"
            )

        except Exception as e:
            st.error(f"Prediction error: {str(e)}")

st.divider()

st.caption(
    "Gracetic AI © 2026 — Intelligent Systems for the Future"
)
