### search.py
import faiss
import numpy as np
import pickle
import os
from query_embedder import QueryEmbedder

INDEX_PATH = "vector_store/index.faiss"
META_PATH = "vector_store/meta.pkl"

embedder = QueryEmbedder()

def load_faiss_index():
    if os.path.exists(INDEX_PATH):
        print("📦 Loading FAISS index...")
        return faiss.read_index(INDEX_PATH)
    else:
        raise FileNotFoundError(f"FAISS index not found at {INDEX_PATH}")


def load_metadata():
    if os.path.exists(META_PATH):
        with open(META_PATH, "rb") as f:
            return pickle.load(f)
    else:
        raise FileNotFoundError(f"Metadata not found at {META_PATH}")


def search_documents(query: str, top_k: int = 5):
    print(f"🔍 Searching for: '{query}'")
    query_vector = embedder.embed_query(query).astype("float32")

    index = load_faiss_index()
    metadata = load_metadata()

    if index.ntotal == 0:
        raise Exception("FAISS index is empty. Run the indexer first.")

    if len(metadata) == 0:
        raise Exception("Metadata is empty. Run the indexer first.")

    if index.ntotal != len(metadata):
        raise Exception(f"Index and metadata size mismatch: index.ntotal={index.ntotal}, metadata={len(metadata)}")

    distances, indices = index.search(query_vector, top_k)

    results = []
    for idx in indices[0]:
        if idx != -1 and idx < len(metadata):
            print(f"✅ Match index {idx}: {metadata[idx]}")
            results.append(metadata[idx])
    return results