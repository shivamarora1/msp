from sentence_transformers import SentenceTransformer

transformer = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(data:list[str]):
    embeddings = transformer.encode(data)
    return [x for x in embeddings]