import vertexai
from vertexai.preview.language_models import ChatModel, InputOutputTextPair

vertexai.init(project="rick-vertex-ai", location="us-central1")
chat_model = ChatModel.from_pretrained("chat-bison@001")
parameters = {
    "temperature": 0.8,
    "max_output_tokens": 1024,
    "top_p": 0.8,
    "top_k": 33
}
chat = chat_model.start_chat(
    context="""You are real estate agent, you need to write and publish property listing on behalf property seller. Please rewrite the description based on information provided. The new description should be very impressive, based on facts, comply to laws&regulations, while can draw more interests from potential buyers""",
)
response = chat.send_message("""Seize the opportunity to buy a legal two family in the transforming and developing Dutch Kills/Long Island city area.  Situated between Astoria and Hunters Point , Dutch Kills is a unique & trendy pocket of the NYC/LIC area. Dutch Kills has been touted as one of the borough\'s best kept secrets , it has established itself as a practical residential enclave with incredible access to Manhattan as well as a diverse array of culture and quick access to other parts of Queens.  The top floor of this two family consists 2 bedrooms, 2 kitchens/living room, and two full bathrooms. First floor has 2 bedrooms, living room/ kitchen, full bathroom, and access to private backyard.  The buyer of this home will appreciate its close proximity to Manhattan, it\'s low property taxes, and the ability to buy into the evolving Long Island city area at a reasonable price.  With 2 two family\'s for sale next to each other, this could be a good option for a 1031 buyer.""", **parameters)
print(f"Response from Model: {response.text}")