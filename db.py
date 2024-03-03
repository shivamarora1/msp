from sentence_transformers import SentenceTransformer
import os
from pymilvus import (connections, Collection)

TOP_K = 10
COLLECTION_NAME = "movies_db"

connections.connect(host=os.getenv("MILVUS_HOST"),
                    post=os.getenv("MILVUS_PORT"))

collection = Collection(COLLECTION_NAME)
collection.load()


transformer = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(data: list[str]):
    embeddings = transformer.encode(data)
    return [x for x in embeddings]


def insert_data(data):
    embeddings = generate_embeddings(data[1])
    ins = [
        data[0],
        embeddings,
        data[2],
    ]
    collection.insert(ins)
