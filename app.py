
import streamlit as st
# Title: Personal Health Profile
import os
from backend.heath_llm import predict_health, predict_llm_health
from typing import Dict
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header

#def get_text():
#    input_text = st.text_input("You", "", key="input-you")
#    if(input_text):
       
#    return input_text

if "health_instance" not in st.session_state:
     st.session_state["health_instance"] = ""
       #st.write("You may ask any health related question")
if "generated" not in st.session_state:
    st.session_state["generated"] = ["I'm health assistant, How may I help you?"]
if "past" not in st.session_state:
    st.session_state["past"] = ["Hi!"]
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

def generate_response(prompt, health_instance):
    response=predict_llm_health(project_id= "rick-vertex-ai",
                                prompt = prompt, health_instance = health_instance
    )
    #st.session_state['generated'].append(response.content)
    
    return response

def request_diabetes(age, gender, height, weight, smoking, glucose, blood_pressure_h, blood_pressure_l, heart_disease, alcohol,cholesterol):
  bmi=weight/((height/100)**2)
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
    #st.write("Diabetes model risks:", dict(prediction))
    diabetes_risk=round(dict(prediction)["scores"][1],4)
    if(diabetes_risk<0.2):
       st.markdown('<p class="big-font">Your diabetes risks level prediction: low</p>', unsafe_allow_html=True)
       #st.write("Diabetes risks level prediction: low")
    elif(diabetes_risk>=0.2 and diabetes_risk<0.5):
       st.markdown('<p class="big-font">Your diabetes risks level prediction: medium</p>', unsafe_allow_html=True)
       #st.write("Diabetes risks level prediction: medium")
    elif(diabetes_risk>=0.5 and diabetes_risk<0.75):
       st.markdown('<p class="big-font">Your diabetes risks level prediction: high</p>', unsafe_allow_html=True)
       #st.write("Diabetes risks level prediction: high")
    else:
       st.markdown('<p class="big-font">Your diabetes risks level prediction: vey high</p>', unsafe_allow_html=True)
       #st.write("Diabetes risks level prediction: high")
  health_instance={
       "gender" : gender,
       "age" : age,
       "height" : height,
       "weight" : weight,
       "smoking_history" : smoking,
       "blood_glucose_level": glucose,
       "blood_pressure_h": blood_pressure_h,
       "blood_pressure_l": blood_pressure_l,
       "heart_disease": heart_disease,
       "diabetes_risk": str(diabetes_risk),
       "alcohol": alcohol,
       "cholesterol": cholesterol
  }
  st.session_state["health_instance"]=health_instance


st.set_page_config(layout="wide")
st.title("My Health Assistant")
st.image(
            "https://www.cdc.gov/diabetes/images/managing/Social-heart-disease-image.jpg?_=22582",
            width=400, # Manually Adjust the width of the image as per requirement
        )
# Create a form
#health_form = st.form(key='my_form')
page_container=st.container()
with page_container:
  st.markdown("""
<style>
.big-font {
    font-size: 30px; 
    color: green;
}
</style>
""", unsafe_allow_html=True)
  st.markdown("""
<style>
.prompt-font {
    font-size: 30px; 
    color: navy;
}
</style>
""", unsafe_allow_html=True)
  st.markdown('<p class="prompt-font">I am your health assistant to answer health questions, please provide your information to start with:</p>', unsafe_allow_html=True)
  #st.write("I am your health assistant to answer health questions, please provide your information to start with:")
# Prompt for enter profile information
  col1,col2,col3=st.columns(3)
  yes_no_options=["no", "yes"]
  with col1: 
    age = st.number_input("Age", value=40, step=1)
    gender = st.selectbox("Gender", ["male", "female"])
    height = st.number_input("Height (cm)", value=170, step=1)
    weight = st.number_input("Weight (kg)",value=60, step=1)
  with col2:
    smoking = st.selectbox("Smoking", ["never","former","No info","current","ever","not current"])
    heart_disease_option = st.selectbox("Heart Disease", yes_no_options)
    heart_disease=yes_no_options.index(heart_disease_option)
    alcohol_option = st.selectbox("Alcohol", yes_no_options)
    alcohol=yes_no_options.index(alcohol_option)  
  with col3:
    glucose = st.number_input("Glucose (mg/dL)",value=80, step=1)
    cholesterol = st.number_input("Cholesterol (mg/dL)",value=180, step=1)
    blood_pressure_h = st.number_input("Blood Pressure (H)",value=120, step=1)
    blood_pressure_l = st.number_input("Blood Pressure (L)",value=70, step=1)
  #submitted = st.form_submit_button("Ask")
  submitted = st.button("Go")
  if submitted:
       request_diabetes(age, gender, height, weight, smoking,  glucose, blood_pressure_h, blood_pressure_l, heart_disease, alcohol,cholesterol)
  
  
  if(st.session_state['health_instance']):
    st.markdown('<p class="prompt-font">What can I help with any other health related question?</p>', unsafe_allow_html=True)
    input_container = st.container()
    colored_header(label='', description='', color_name='blue-30')
    response_container = st.container()
  ## Applying the user input box
    with input_container: 
       user_input = st.text_input("You", "", key="input-you")
    with response_container:
    
      if user_input:
       
        response = generate_response(user_input,st.session_state["health_instance"])
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response.content)
        #st.write(f"Response from Model: {response.text}")
        st.session_state["chat_history"].append((user_input, response.content))  
      if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
  
     #st.write(f"Response from Model: {response.text}")

 
