
import streamlit as st
# Title: Personal Health Profile
import os
from backend.heath_llm import predict_health, predict_llm_health
from typing import Dict
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header

def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

def generate_response(prompt, health_instance):
    response=predict_llm_health(project_id= "rick-vertex-ai",
                                prompt = prompt, health_instance = health_instance
    )
    st.session_state['generated'].append(response)
    
    return response

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

  if "generated" not in st.session_state:
    st.session_state["generated"] = ["I'm health assistant, How may I help you?"]
  if "past" not in st.session_state:
    st.session_state["past"] = ["Hi!"]
  if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

  input_container = st.container()
  colored_header(label='', description='', color_name='blue-30')
  response_container = st.container()
  ## Applying the user input box
  with input_container: 
    user_input = get_text()
  with response_container:
    if user_input:
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
        response = generate_response(user_input,health_instance)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response.content)
        #st.write(f"Response from Model: {response.text}")
        st.session_state["chat_history"].append((user_input, response.content))
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
  
     #st.write(f"Response from Model: {response.text}")

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
  
  age = st.number_input("Age", value=30, step=1)
  gender = st.selectbox("Gender", ["male", "female"])
  height = st.number_input("Height (cm)", value=160, step=1)
  weight = st.number_input("Weight (kg)",value=50, step=1)
  drinking_option = st.selectbox("Drinking", yes_no_options)
  drinking=yes_no_options.index(drinking_option)
  smoking = st.selectbox("Smoking", ["never","former","No info","current","ever","not current"])
  
  heart_disease_option = st.selectbox("Heart Disease", yes_no_options)
  heart_disease=yes_no_options.index(heart_disease_option)

  alcohol_option = st.selectbox("Alcohol", yes_no_options)
  alcohol=yes_no_options.index(alcohol_option)  
  glucose = st.number_input("Glucose (mg/dL)",value=80, step=1)
  blood_pressure_h = st.number_input("Blood Pressure (H)",value=100, step=1)
  blood_pressure_l = st.number_input("Blood Pressure (L)",value=70, step=1)
  submitted = st.form_submit_button("Save")
  if submitted:
       request_diabetes(age, gender, height, weight, smoking,  glucose, blood_pressure_h, blood_pressure_l, heart_disease)


