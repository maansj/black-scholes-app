import streamlit as st
from app.data import get_live_price, get_intraday_data
from app.plots import (
    intraday_plot,
    sensitivity_rate,
    sensitivity_volatility,
    sensitivity_maturity
)

st.title("Interactive Black-Scholes Option Pricing")

ticker = st.text_input("Ticker", "AAPL")
S = get_live_price(ticker)
st.write(f"Current price of {ticker}: {S:.2f}")

strike = st.number_input("Strike price", value=round(float(S)))
r = st.slider("Risk-free interest rate", 0.0, 0.1, 0.03, 0.001)
sigma = st.slider("Volatility", 0.01, 1.0, 0.2, 0.01)
T = st.slider("Time to Maturity (years)", 1, 20, 1)

intraday_data = get_intraday_data(ticker)
st.plotly_chart(intraday_plot(intraday_data, ticker), use_container_width=True)

st.plotly_chart(sensitivity_rate(S, strike, sigma, T, r), use_container_width=True)
st.plotly_chart(sensitivity_volatility(S, strike, r, T, sigma), use_container_width=True)
st.plotly_chart(sensitivity_maturity(S, strike, r, sigma, T), use_container_width=True)
