import streamlit as st
import pandas as pd
import numpy as np

st.title("🏠 House Price Prediction System")
st.write("IBM SkillsBuild Data Analytics with AI Internship Project")

# Input fields
area = st.number_input("Enter Property Area (in sq ft):", min_value=500, max_value=10000, value=1500)
rooms = st.number_input("Enter Number of Bedrooms:", min_value=1, max_value=6, value=3)

if st.button("Predict Price"):
    # Simple linear estimation logic based on our model
    estimated_price = (area * 120) + (rooms * 25000) + 50000
    st.success(f"Estimated Property Price: ${estimated_price:,.2f}")
