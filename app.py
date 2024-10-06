import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
import tempfile
import os
os.environ["OPENAI_API_KEY"] = "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"
# Initialize session state
if 'conversation' not in st.session_state:
    st.session_state.conversation = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

st.title("Document Chat Bot")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

if uploaded_file is not None:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    # Load and process the PDF
    loader = PyPDFLoader(tmp_file_path)
    documents = loader.load()
    
    # Split the documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    # Create embeddings and store in vectorstore
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(texts, embeddings)

    # Create conversation chain
    st.session_state.conversation = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(temperature=0.7, model_name='gpt-3.5-turbo'),
        retriever=vectorstore.as_retriever()
    )

    st.success("Document uploaded and processed successfully!")

# Chat interface
if st.session_state.conversation:
    user_question = st.text_input("Ask a question about the uploaded document:")
    if user_question:
        response = st.session_state.conversation({"question": user_question, "chat_history": st.session_state.chat_history})
        st.session_state.chat_history.append((user_question, response["answer"]))

        # Display chat history
        for i, (question, answer) in enumerate(st.session_state.chat_history):
            st.write(f"Human: {question}")
            st.write(f"AI: {answer}")
            if i < len(st.session_state.chat_history) - 1:
                st.write("---")
else:
    st.info("Please upload a document to start chatting.")