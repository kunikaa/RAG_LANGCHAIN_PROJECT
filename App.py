import os
from dotenv import load_dotenv
import streamlit as st
from google import genai
import PyPDF2

# Load environment variables
load_dotenv()

# Initialize Google Gemini client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to extract text from uploaded PDF
def load_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text

# Function to get answer from Gemini model
def get_answer(question_text):
    response = client.models.generate_content(
        model="models/gemini-flash-lite-latest",
        contents=question_text
    )
    return response.text

# ----------------- STREAMLIT UI -----------------
st.set_page_config(page_title="PDF Q&A RAG System", layout="wide")
st.title("📄 PDF-based Q&A System")
st.write("Upload your PDF and ask questions. Answers are generated strictly from your document using Google Gemini.")

# PDF Upload
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file:
    st.success(f"PDF uploaded: {uploaded_file.name}")

    # Extract text from PDF
    with st.spinner("Reading PDF..."):
        pdf_text = load_pdf(uploaded_file)
    st.info(f"PDF contains approx. {len(pdf_text)//1000}k characters of text.")

    # Input question
    user_question = st.text_input("Enter your question:")

    # Button to generate answer
    if st.button("Get Answer") and user_question:
        with st.spinner("Generating answer..."):
            # Here you can combine PDF context with user question
            # For simplicity, we append the PDF text to question
            combined_input = f"Context: {pdf_text}\nQuestion: {user_question}"
            answer = get_answer(combined_input)

        st.subheader("🤖 Answer:")
        st.write(answer)
