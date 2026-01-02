from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

def create_rag_chain(retriever):
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        temperature=0.2
    )

    prompt = ChatPromptTemplate.from_template("""
    Answer the question using only the context below.
    If the answer is not in the context, say you don't know.

    Context:
    {context}

    Question:
    {input}
    """)

    document_chain = create_stuff_documents_chain(llm, prompt)

    return create_retrieval_chain(retriever, document_chain)
