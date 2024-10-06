# Document-Chat-Bot
Financial Document Chatbot
```markdown
# Document Chat Bot

This Streamlit app allows you to upload a PDF document and chat with it using a large language model (LLM).  It uses Langchain to manage the interaction, OpenAI embeddings for semantic search, and FAISS for efficient vector storage.

## Features

* **PDF Upload:** Upload your PDF document through a simple file uploader.
* **Chat Interface:**  Ask questions about the document content in a conversational manner.
* **Contextual Answers:** The chatbot leverages the entire document content to provide relevant and accurate responses.
* **Chat History:** Keeps track of the conversation history for easy reference.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git 
   cd your-repo-name
   ```
2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```
   Create a `requirements.txt` file with the following content:
   ```
   streamlit
   langchain
   langchain_community
   faiss-cpu
   openai
   ```
3. **Set your OpenAI API key:**
   - Create a `.env` file in the root directory of the project.
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=your_actual_openai_api_key
     ```
   - Install the `python-dotenv` package:  `pip install python-dotenv`


## Usage

1. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
2. **Upload a PDF document:** Use the file uploader to select your PDF.
3. **Ask questions:** Type your question in the text input and press Enter.
4. **Review the answers:** The chatbot's response and the conversation history will be displayed below.

## How it Works

1. **Document Loading and Processing:** The uploaded PDF is loaded using `PyPDFLoader` and split into smaller chunks using `CharacterTextSplitter`.
2. **Embeddings and Vectorstore:** OpenAI embeddings are generated for each text chunk and stored in a FAISS vectorstore for efficient similarity search.
3. **Conversational Retrieval Chain:** A `ConversationalRetrievalChain` is created using the OpenAI LLM and the FAISS vectorstore.  This chain manages the conversation and retrieves relevant information from the document based on the user's questions.
4. **Chat Interface:** The Streamlit interface allows the user to input questions and displays the chatbot's responses along with the chat history.
