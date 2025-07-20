import faiss
import pickle

index = faiss.read_index("vector_store/index.faiss")
print("FAISS vectors stored:", index.ntotal)

with open("vector_store/meta.pkl", "rb") as f:
    meta = pickle.load(f)
print("Metadata entries:", len(meta))
