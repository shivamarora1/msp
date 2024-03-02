import os
from pymilvus import (connections, Collection)

import utils

TOP_K = 10
COLLECTION_NAME = "movies_db"

connections.connect(host=os.getenv("MILVUS_HOST"),
                    post=os.getenv("MILVUS_PORT"))

collection = Collection(COLLECTION_NAME)
collection.load()


def search_data(data: list[str]):
    search_embeddings = utils.generate_embeddings(data)
    resp = collection.search(data=search_embeddings, anns_field="embedding", param={
                             'metric_type': 'L2', 'params': {'nprobe': 10}}, limit=TOP_K, output_fields=['title', 'image'])
    result = {}
    for i, hits in enumerate(resp):
        result[data[i]] = [{"title": hit.entity.get(
            'title'), "image": hit.entity.get(
            'image'), "match": hit.distance} for hit in hits]
    return result


def insert_data(data):
    embeddings = utils.generate_embeddings(data[1])
    ins = [
        data[0],
        embeddings,
        data[2],
    ]
    collection.insert(ins)
