import os
from typing import Any, Dict, List
from langchain.llms import VertexAI
from langchain.chat_models import ChatGooglePalm
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import VertexAIEmbeddings

from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import FAISS


def run_g_llm(documents:str, query: str, chat_history: List[Dict[str, Any]] = []):
    embeddings = VertexAIEmbeddings()  # Dimention 768
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=50)
    texts=text_splitter.create_documents([documents])
    #texts = text_splitter.split_documents(documents)
    vectorstore = FAISS.from_documents(texts, embeddings)
    chat = ChatGooglePalm(
        verbose=True,
        temperature=0,
    )
    
    qa = ConversationalRetrievalChain.from_llm(
        llm=chat, retriever=vectorstore.as_retriever(), return_source_documents=True
    )
    return qa({"question": query, "chat_history": chat_history})
