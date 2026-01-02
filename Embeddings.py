from sentence_transformers import SentenceTransformer

# Load model once
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(texts):
    return embedding_model.encode(texts).tolist()
