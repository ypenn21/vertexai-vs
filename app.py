import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from backend.backend import run_g_llm
import os


def get_documents():
   if "documents" not in st.session_state:
      uploaded_file = st.file_uploader("Upload your file here...")
      if uploaded_file is not None:
        documents=uploaded_file.getvalue().decode('utf-8')
        st.session_state["documents"]=documents
        return documents
def get_text(instruction: str = "You: "):
    input_text = st.text_input(instruction, "", key=f"input-{instruction}")
    return input_text

def get_url():
   if "url" not in st.session_state:
      url = st.text_input(
          "Enter the URL of the file you want to upload",
          "https://www.google.com/",
          key="url",
      )
     
   return url
      
st.set_page_config(page_title="Talk2File - An LLM-powered File Search")
with st.sidebar:
    st.title("🤗💬 Talk2File")
    st.markdown(
        """
    ## About
    This Talk to File app is an LLM-powered chatbot built using:
    - [LangChain 🦜🔗](https://python.langchain.com/en/latest/index.html)
    - [Vector store FAISS](https://github.com/google-research/faiss)
    - [Palm2 LLM Model](https://ai.google/discover/palm2)   
    - [Streamlit](https://streamlit.io/)



    """
    )
    add_vertical_space(5)
    # api_key_container = st.container()
    # with api_key_container:
    #     palm_api_key = get_text(instruction="PALM2_API_KEY")
    #     if palm_api_key:
    #         os.environ["PALM_2_API_KEY"]

if "generated" not in st.session_state:
    st.session_state["generated"] = ["I'm ready, How may I help you?"]
if "past" not in st.session_state:
    st.session_state["past"] = ["Hi!"]
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []


input_container = st.container()
colored_header(label="", description="", color_name="blue-30")
response_container = st.container()


with input_container:
    choice = st.radio("Select your choice: ", ('upload', 'url'))
    if (choice == 'upload'):
      st.session_state["url"] = []
      get_documents()
    else:
      st.session_state["documents"] = []
      get_url()
    user_input = get_text(instruction="Ask: ")

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        with st.spinner("Generating response..."):
            response = run_g_llm(
                st.session_state["documents"], query=user_input, chat_history=st.session_state["chat_history"]
            )
            st.session_state.past.append(user_input)
            st.session_state.generated.append(response["answer"])
            st.session_state["chat_history"].append((user_input, response["answer"]))

    if st.session_state["generated"]:
        for i in range(len(st.session_state["generated"])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
            message(st.session_state["generated"][i], key=str(i))