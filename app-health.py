
import streamlit as st

# Title, Health Survey and consultant
st.title("Health Survey")
st.write("Consultant: Dr. Smith")

# Prompt for input survey
st.write("Please enter your information below:")

# Age Textbox
age = st.number_input("Age")

# Gender Textbox
gender = st.selectbox("Gender", ["Male", "Female"])

# Height Textbox
height = st.number_input("Height (in inches)")

# Weight Textbox
weight = st.number_input("Weight (in pounds)")

# Smoking Textbox
smoking = st.selectbox("Smoking", ["Yes", "No"])

# Drinking Textbox
drinking = st.selectbox("Drinking", ["Yes", "No"])

# Education Textbox
education = st.selectbox("Education", ["High School", "College", "Graduate School"])

# Display the results
st.write("Your results:")
st.write("Age:", age)
st.write("Gender:", gender)
st.write("Height:", height)
st.write("Weight:", weight)
st.write("Smoking:", smoking)
st.write("Drinking:", drinking)
st.write("Education:", education)
#write streamlit page with following features:
#1. Title, Health Survey and consultant
#2. Prompt for input survey
#2.1 Age Textbox
#2.2 Gender Textbox
#2.3 Height Textbox
#2.4 Weight Textbox
#2.5 Smoking Textbox
#2.6 Drinking Textbox
#2.7 Education Textbox
#2.8 Smoking Textbox
#2.9 Drinking Textbox
#2.10 Education Textbox