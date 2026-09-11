import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Gracetic AI",
    page_icon="🤖",
    layout="centered"
)

# Load model
@st.cache_resource
def load_model():
    return joblib.load("gracetic_startup_funding_model.pkl")

try:
    model = load_model()
except FileNotFoundError:
    st.error("Model file not found.")
    st.stop()

# Header
st.title("🤖 Gracetic AI")
st.subheader("Intelligent Systems for the Future")
st.write("🌍 AI-powered global startup funding prediction system")
st.divider()

# Startup information
st.header("📋 Startup Information")

col1, col2 = st.columns(2)

with col1:
    valuation = st.number_input(
        "Valuation (USD Millions)",
        min_value=0.0,
        value=10.0,
        step=0.1
    )

    age = st.number_input(
        "Startup Age (Years)",
        min_value=0.0,
        value=5.0,
        step=0.5
    )

with col2:
    burn_rate = st.number_input(
        "Monthly Burn Rate (USD Millions)",
        min_value=0.0,
        value=1.0,
        step=0.1
    )

# Location and industry
st.header("🌍 Location & Industry")

col1, col2 = st.columns(2)

with col1:
    city = st.text_input(
        "City",
        placeholder="e.g. Kampala, Tokyo, Berlin"
    )

    country = st.text_input(
        "Country",
        placeholder="e.g. Uganda, Japan, Germany"
    )

with col2:
    domain = st.text_input(
        "Industry",
        placeholder="e.g. FinTech, AI, AgriTech"
    )

st.divider()

# Prediction
if st.button(
    "🚀 Predict Funding",
    use_container_width=True,
    type="primary"
):

    if not city or not country or not domain:
        st.warning("Please enter the city, country, and industry.")

    else:
        data = pd.DataFrame({
            "Valuation_USD_Millions": [valuation],
            "Startup_Age": [age],
            "Monthly_Burn_Rate_Millions": [burn_rate],
            "City": [city],
            "Country": [country],
            "Domain": [domain]
        })

        try:
            prediction = model.predict(data)[0]

            st.success("✅ Prediction completed!")

            st.metric(
                "💰 Predicted Total Funding",
                f"${prediction:,.2f}M"
            )

            with st.expander("📊 Startup Profile"):
                st.write(f"""
                **Location:** {city}, {country}

                **Industry:** {domain}

                **Valuation:** ${valuation}M

                **Age:** {age} years

                **Burn Rate:** ${burn_rate}M/month

                **Predicted Funding:** ${prediction:,.2f}M
                """)

            with st.expander("💡 Prediction Insights"):
                runway = (
                    valuation / burn_rate
                    if burn_rate > 0
                    else float("inf")
                )

                ratio = (
                    prediction / valuation
                    if valuation > 0
                    else 0
                )

                st.write(f"""
                **Runway:** {runway:.1f} months

                **Funding / Valuation:** {ratio:.2f}x
                """)

        except Exception as e:
            st.error(f"Prediction error: {e}")

st.divider()

st.caption(
    "Gracetic AI © 2026 — Intelligent Systems for Emerging Markets"
)

with st.expander("ℹ️ About This Model"):
    st.write("""
    **Gracetic AI Startup Funding Predictor**

    Predicts startup funding using:

    - Valuation
    - Startup age
    - Monthly burn rate
    - City
    - Country
    - Industry

    **Disclaimer:** This model is for prediction purposes only
    and is not investment advice.
    """)
