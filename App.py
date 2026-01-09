import streamlit as st
from google import genai
import PyPDF2

# ----------------- GOOGLE GEMINI CLIENT -----------------
api_key = st.secrets["GOOGLE_API_KEY"]

client = genai.Client(api_key=api_key)

# ----------------- FUNCTIONS -----------------
def load_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text


def get_answer(question_text):
    response = client.models.generate_content(
        model="models/gemini-flash-lite-latest",
        contents=question_text
    )
    return response.text


# ----------------- STREAMLIT UI -----------------
st.set_page_config(page_title="PDF Q&A RAG System", layout="wide")

st.title("📄 PDF-based Q&A System")
st.write(
    "Upload your PDF and ask questions. "
    "Answers are generated strictly from your document using Google Gemini."
)

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file:
    st.success(f"PDF uploaded: {uploaded_file.name}")

    with st.spinner("Reading PDF..."):
        pdf_text = load_pdf(uploaded_file)

    st.info(f"PDF contains approx. {len(pdf_text)//1000}k characters of text.")

    user_question = st.text_input("Enter your question:")

    if st.button("Get Answer") and user_question:
        with st.spinner("Generating answer..."):
            combined_input = f"""
            Answer the question ONLY using the context below.
            If answer is not present, say "Answer not found in document".

            Context:
            {pdf_text}

            Question:
            {user_question}
            """

            answer = get_answer(combined_input)

        st.subheader("🤖 Answer:")
        st.write(answer)
