import streamlit as st
import PyPDF2
from App import get_answer   # use app if renamed to app.py

st.set_page_config(page_title="AI PDF Search & Assistant", layout="wide")

# ================= MAIN TITLE =================
st.title("📄 AI PDF Search & General Assistant")
st.caption("Search inside your PDF or ask general AI questions")

# ================= PDF SEARCH SECTION =================
st.subheader("📘 Search Inside PDF")

uploaded_file = st.file_uploader(
    "Upload your PDF document",
    type=["pdf"]
)

pdf_question = st.text_input(
    "🔍 Ask a question from the PDF",
    placeholder="Search only inside the uploaded PDF..."
)

def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

if st.button("Search PDF"):
    if not uploaded_file:
        st.warning("⚠️ Please upload a PDF first.")
    elif not pdf_question:
        st.warning("⚠️ Please enter a PDF-related question.")
    else:
        with st.spinner("Searching inside the PDF..."):
            pdf_text = read_pdf(uploaded_file)

            prompt = f"""
You are a document-based assistant.
Answer ONLY from the given context.
If the answer is not present, say "Not found in the document."

Context:
{pdf_text}

Question:
{pdf_question}
"""

            answer = get_answer(prompt)

        st.success("Answer from PDF")
        st.write(answer)

# ================= DIVIDER =================
st.markdown("---")

# ================= GENERAL AI SECTION =================
st.subheader("💬 General AI Question")

general_question = st.text_input(
    "Ask anything ",
    placeholder="Ask a general question..."
)

if st.button("Ask AI"):
    if not general_question:
        st.warning("⚠️ Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            answer = get_answer(general_question)

        st.success("AI Answer")
        st.write(answer)
