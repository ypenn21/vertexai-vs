
import streamlit as st
from backend.health_llm import predict_llm_health, predict_health
# Title: Personal Health Profile
st.title("Personal Health Profile")

# Prompt for enter profile information
age = st.number_input("Age")
gender = st.selectbox("Gender", ["male", "female"])
height = st.number_input("Height (cm)")
weight = st.number_input("Weight (kg)")
smoking = st.selectbox("Smoking", ["yes", "no"])
drinking = st.selectbox("Drinking", ["yes", "no"])
education = st.selectbox("Education", ["high school", "college", "graduate school"])
smoking = st.selectbox("Smoking", ["yes", "no"])
alcohol = st.selectbox("Alcohol", ["yes", "no"])
glucose = st.number_input("Glucose (mg/dL)")
blood_pressure_h = st.number_input("Blood Pressure (H)")
blood_pressure_l = st.number_input("Blood Pressure (L)")

# Predict health
bmi=weight/(height**2)
bmi=round(bmi, 2)

diabetest_endpoint=2830191308407046144
diabetes_instance={
 gender: 0.0,
 age: 0.0,
 bmi: 0.0,
 blood_pressure_h: 0.0,
 blood_pressure_l: 0.0,
 drinking: 0.0,
 height: 0.0,
 weight: 0.0,
 smoking: 0.0,
}
heart_disease_endpoint=2863405355658903552	
heart_disease_instance={
  	
}


health = predict_health(age, gender, height, weight, smoking, drinking, education, smoking, alcohol, glucose, blood_pressure
