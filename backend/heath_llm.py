import vertexai
from vertexai.preview.language_models import ChatModel, InputOutputTextPair
from typing import Dict

from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value

def predict_llm_health(
    project_id: str,
    content: str,
    health_instance
    ) :
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
    response = chat.send_message(content=content, parameters=parameters)
    #print("response")
    #print(" deployed_model_id:", response.deployed_model_id)
    # See gs://google-cloud-aiplatform/schema/predict/prediction/tabular_classification
    return response

def predict_health(
    project: str,
    endpoint_id: str,
    instance_dict: Dict,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
    # for more info on the instance schema, please use get_model_sample.py
    # and look at the yaml found in instance_schema_uri
    instance = json_format.ParseDict(instance_dict, Value())
    instances = [instance]
    parameters_dict = {}
    parameters = json_format.ParseDict(parameters_dict, Value())
    endpoint = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id
    )
    response = client.predict(
        endpoint=endpoint, instances=instances, parameters=parameters
    )
    print("response")
    print(" deployed_model_id:", response.deployed_model_id)
    # See gs://google-cloud-aiplatform/schema/predict/prediction/tabular_classification_1.0.0.yaml for the format of the predictions.
    predictions = response.predictions
    return predictions
    #for prediction in predictions:
    #    print(" prediction:", dict(prediction))
