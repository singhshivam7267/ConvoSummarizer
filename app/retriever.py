from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Store for documents
documents = []  # The actual text
index = None     # FAISS index

def build_knowledge_base(text_chunks: list):
    global index, documents
    documents = text_chunks
    embeddings = embedding_model.encode(text_chunks, convert_to_numpy=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

def retrieve_context(query: str, top_k: int = 3):
    if not index:
        return ""
    query_embedding = embedding_model.encode([query])
    D, I = index.search(np.array(query_embedding), top_k)
    retrieved = [documents[i] for i in I[0]]
    return "\n".join(retrieved)
