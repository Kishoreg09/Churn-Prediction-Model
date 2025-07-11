import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('Models/random_forest_model.pkl')

st.title("🔍 Customer Churn Prediction App")
st.markdown("Provide the following details to predict if the customer will exit.")

# Collect inputs
credit_score = st.number_input("Credit Score", min_value=300, max_value=900)
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=18, max_value=100)
tenure = st.number_input("Tenure (years with bank)", min_value=0, max_value=10)
balance = st.number_input("Account Balance", min_value=0.0,)
num_products = st.number_input("Number of Products", min_value=1, max_value=4)
has_crcard = st.selectbox("Has Credit Card?", ["Yes", "No"])
is_active = st.selectbox("Is Active Member?", ["Yes", "No"])
salary = st.number_input("Estimated Salary", min_value=0.0)
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])

# Derived Features
balance_salary_ratio = balance / (salary + 1)  # Avoid divide by 0
age_tenure_ratio = age / (tenure + 1)

# Encode categorical variables
gender_val = 1 if gender == "Male" else 0
has_crcard_val = 1 if has_crcard == "Yes" else 0
is_active_val = 1 if is_active == "Yes" else 0
geo_germany = 1 if geography == "Germany" else 0
geo_spain = 1 if geography == "Spain" else 0

# Final feature vector (13 features)
input_data = np.array([[credit_score, gender_val, age, tenure, balance, num_products,
                        has_crcard_val, is_active_val, salary,
                        geo_germany, geo_spain, balance_salary_ratio, age_tenure_ratio]])

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ The customer is likely to EXIT the bank.")
    else:
        st.success("✅ The customer is likely to STAY with the bank.")
