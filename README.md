# RAG_LANGCHAIN_PROJECT (AI PDF Search & General Assistant)


# 📄 PDF-based Retrieval Augmented Generation (RAG) System

##  Project Overview

This project is a **PDF-based Retrieval Augmented Generation (RAG) system** that allows users to upload PDF documents and ask questions strictly based on the content of those documents. The system prevents hallucinations by ensuring that answers are generated **only from retrieved document context**.

An interactive **Streamlit UI** is integrated, enabling users to upload their own PDFs and query them in real time.

---

##  Features

* Upload and process PDF documents through a user-friendly UI
* Extract text from PDFs and split it into semantic chunks
* Generate embeddings for semantic understanding
* Store and retrieve embeddings using a vector database
* Perform similarity-based document retrieval
* Generate accurate answers strictly from retrieved content
* Prevent hallucinated responses using controlled prompt logic

---

##  How the RAG Pipeline Works

1. **PDF Upload**
   Users upload PDF files via the Streamlit interface.

2. **Text Extraction**
   Text is extracted from PDFs using **PyPDF2**.

3. **Text Chunking**
   Extracted text is split into meaningful semantic chunks to improve retrieval accuracy.

4. **Embedding Generation**
   Each chunk is converted into vector embeddings using the **Google Gemini Embedding API**.

5. **Vector Storage**
   Embeddings are stored in **ChromaDB**, a vector database optimized for similarity search.

6. **Similarity-Based Retrieval**
   When a user asks a question, the most relevant document chunks are retrieved using cosine similarity.

7. **Answer Generation**
   Retrieved content is passed to the **Google Gemini Flash Lite model**, which generates answers strictly from the provided context.

---

## User Interface (UI)

* Built using **Streamlit**
* Allows users to:

  * Upload their own PDF documents
  * Ask questions through a text input
  * Receive instant answers generated from the document

---

## Tech Stack

* **Programming Language:** Python
* **LLM:** Google Gemini Flash Lite
* **Embedding Model:** Google Gemini Embedding API
* **Vector Database:** ChromaDB
* **PDF Processing:** PyPDF2
* **Framework:** LangChain
* **UI:** Streamlit
* **Environment Management:** dotenv

---

## Project Structure

```
Rag_Langchain_Project/
│
├── app.py                # Main RAG pipeline logic
├── ui.py                 # Streamlit UI integration
├── requirements.txt      # Project dependencies
├── .env                  # Environment variables (API keys)
├── README.md             # Project documentation
└── data/                 # Uploaded PDF files
```

---

## Environment Setup

Create a `.env` file in the project root and add:

```
GOOGLE_API_KEY=your_google_gemini_api_key
```

>  Do not commit the `.env` file to GitHub.

---

##  How to Run the Project

### 1️ Install Dependencies

```
pip install -r requirements.txt
```

### 2️ Run the Streamlit App

```
streamlit run ui.py
```

### 3️ Use the Application

* Upload a PDF file
* Ask questions related to the document
* Get accurate answers based only on PDF content

---

## Example Use Case

* Academic notes Q&A
* Company policy document search
* Research paper understanding
* PDF-based chat assistant

---

##  Key Highlights

* Strict document-grounded answering (no hallucination)
* Modular and scalable RAG architecture
* Secure API key handling
* Clean and minimal UI

---

## Future Enhancements

* Support for multiple PDFs at once
* Chat history memory
* PDF preview in UI
* Deployment on cloud platforms

---

Author

**Kunika Pandey**

---


