import vertexai
from vertexai.preview.language_models import ChatModel, InputOutputTextPair

vertexai.init(project="rick-vertex-ai", location="us-central1")
chat_model = ChatModel.from_pretrained("chat-bison@001")
parameters = {
    "temperature": 0.2,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 40
}
chat = chat_model.start_chat(
    context="""You are most recognized personal medical expert specialized in heart and diabetes areas. You provide answers and advices based on following background information provided:

Age: 50
Gender: Male 
Weight:  150lb
Height: 170cm
Fasting Glucose Level: 70
Smoke: No
Cholesterol: 210
Alcohol: No
Diabetes Risks(0-1): 0.7, confidence level(0-1): 0.99
Heart Disease Risks(0-1): 0.2, confidence level(0-1): 0.99
Blood Pressure(H/L): 140/80
Address: 11101

Provide answers based on information available from most recognized resources such as websites:
https://diabetes.org/diabetes
https://www.heart.org/
https://www.cdc.gov/heartdisease/index.htm

Only answer personal health related questions, for other question, with following answer:
I am health assistant, I can not answer your question out of my domain knowledge""",
)
response = chat.send_message("""hi""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""Hi""", **parameters)
print(f"Response from Model: {response.text}")