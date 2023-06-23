
import streamlit as st
# Title: Personal Health Profile
import os
from backend.heath_llm import predict_health, predict_llm_health
from typing import Dict

def request_diabetes(age, gender, height, weight, smoking, glucose, blood_pressure_h, blood_pressure_l, heart_disease):
  bmi=weight/(height/100**2)
  bmi=round(bmi,2)
  hypertension=0
  if(blood_pressure_h>130):
    hypertension=1
  diabetes_endpoint="2830191308407046144"
  diabetes_instance={
   "gender" : gender,
   "age" : str(age),
   "smoking_history" : smoking,
   "bmi": str(bmi),
   "blood_glucose_level": str(glucose),
   "hypertension": str(hypertension),
   "heart_disease": str(heart_disease)
  }
  predictions = predict_health(project= "rick-vertex-ai", endpoint_id=diabetes_endpoint, instance_dict=diabetes_instance)
  for prediction in predictions:
    st.write(" prediction:", dict(prediction))
  question=st.text_input("Ask question:")
  ask_submitted = st.form_submit_button("Go")
  if(ask_submitted):
     health_instance={
       "gender" : gender,
       "age" : age,
       "height" : height,
       "weight" : weight,
       "smoking_history" : smoking,
       "blood_glucose_level": str(glucose),
       "blood_pressure_h": blood_pressure_h,
       "blood_pressure_l": blood_pressure_l,
       "heart_disease": heart_disease
        
     }
     response = predict_llm_health(project_id= "rick-vertex-ai", content=question, health_dict=health_instance)
    
     st.write(f"Response from Model: {response.text}")

def request_heart_disease(age, gender, height, weight, smoking, glucose, blood_pressure_h, blood_pressure_l):
  bmi=weight/(height/100**2)
  bmi=round(bmi,2)
  hypertension=0
  if(blood_pressure_h>130):
    hypertension=1
  heart_endpoint="2863405355658903552"
  heart_instance={
   "gender" : gender,
   "age" : str(age),
   "smoking_history" : smoking,
   "bmi": str(bmi),
   "blood_glucose_level": str(glucose),
   "hypertension": str(hypertension),
   "heart_disease": "0"
  }
  predictions = predict_health(project= "rick-vertex-ai", endpoint_id=heart_endpoint, instance_dict=heart_instance)
  for prediction in predictions:
    st.write(" prediction:", dict(prediction))



st.set_page_config(layout="wide")
st.title("Personal Health Profile")
# Create a form
with st.form("Health Profile Form"):

# Prompt for enter profile information
  yes_no_options=["no", "yes"]
  
  age = st.number_input("Age")
  gender = st.selectbox("Gender", ["male", "female"])
  height = st.number_input("Height (cm)")
  weight = st.number_input("Weight (kg)")
  drinking_option = st.selectbox("Drinking", yes_no_options)
  drinking=yes_no_options.index(drinking_option)
  smoking = st.selectbox("Smoking", ["former","No info","never","current","ever","not current"])
  
  heart_disease_option = st.selectbox("Heart Disease", yes_no_options)
  heart_disease=yes_no_options.index(heart_disease_option)

  alcohol_option = st.selectbox("Alcohol", yes_no_options)
  alcohol=yes_no_options.index(alcohol_option)  
  glucose = st.number_input("Glucose (mg/dL)")
  blood_pressure_h = st.number_input("Blood Pressure (H)")
  blood_pressure_l = st.number_input("Blood Pressure (L)")
  submitted = st.form_submit_button("Save")
  if submitted:
       request_diabetes(age, gender, height, weight, smoking,  glucose, blood_pressure_h, blood_pressure_l, heart_disease)


