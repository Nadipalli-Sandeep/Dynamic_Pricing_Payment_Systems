# app.py

import streamlit as st
from model import dynamic_pricing

st.title("Dynamic Pricing App")

# User input fields
transaction_amount = st.number_input("Transaction Amount", min_value=50, max_value=1000)
payment_method = st.selectbox("Payment Method", ['Credit Card', 'UPI', 'Wallet'])
hour_of_day = st.number_input("Hour of Day", min_value=0, max_value=23)
day_of_week = st.number_input("Day of Week", min_value=0, max_value=6)
competitor_fee = st.number_input("Competitor Fee", min_value=0.5, max_value=3.0)
customer_segment = st.selectbox("Customer Segment", ['Regular', 'Premium'])

if st.button("Calculate Dynamic Fee"):
    predicted_fee = dynamic_pricing(transaction_amount, payment_method, hour_of_day, day_of_week, competitor_fee, customer_segment)
    st.success(f"Predicted Dynamic Transaction Fee: ${predicted_fee:.2f}")
