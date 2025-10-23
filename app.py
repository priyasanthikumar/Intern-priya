# app.py
import streamlit as st
import pandas as pd
import joblib
import os

# -------------------------------
# File paths
# -------------------------------
MODEL_FILE = 'bangalore_house_price_model.pkl'
DATA_FILE = 'Bengaluru_House_Data.csv'

# -------------------------------
# Load model
# -------------------------------
if not os.path.exists(MODEL_FILE):
    st.warning("Model not found. Please run model_training.py first!")
else:
    pipeline = joblib.load(MODEL_FILE)
    st.success("✅ Model loaded successfully!")

# -------------------------------
# Helper function for BHK
# -------------------------------
def extract_bhk(size_str):
    try:
        return int(size_str.split()[0])
    except:
        return 0

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🏠 House Price Prediction")
st.write("Enter house details to predict the price:")

# Numeric inputs
total_sqft = st.number_input("Total Area (sqft)", min_value=100.0, value=1000.0, step=10.0)
bath = st.number_input("Bathrooms", min_value=0, value=2, step=1)
balcony = st.number_input("Balconies", min_value=0, value=1, step=1)
size = st.text_input("Size (e.g., 2 BHK)", value="2 BHK")
bhk = extract_bhk(size)

# Load dataset for dynamic dropdowns
df = pd.read_csv(DATA_FILE)
area_type = st.selectbox("Area Type", df['area_type'].unique())
availability = st.selectbox("Availability", df['availability'].unique())
location = st.selectbox("Location", df['location'].unique())
society = st.text_input("Society Name", value="Unknown")

# Prepare input
input_df = pd.DataFrame([{
    'total_sqft': total_sqft,
    'bath': bath,
    'balcony': balcony,
    'bhk': bhk,
    'area_type': area_type,
    'availability': availability,
    'location': location,
    'society': society
}])

# Prediction
if st.button("Predict Price"):
    prediction = pipeline.predict(input_df)[0]

    # Convert from lakhs to INR
    price_in_inr = prediction * 5000

    if price_in_inr >= 1e7:
        st.success(f"🏠 Predicted Price: ₹{price_in_inr/1e7:.2f} Crores")
    else:
        st.success(f"🏠 Predicted Price: ₹{price_in_inr/1e5:.2f} Lakhs")
