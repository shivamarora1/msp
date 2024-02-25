import db
import time
import csv
from pymilvus import (
    connections, utility, FieldSchema, CollectionSchema, DataType, Collection
)
from dotenv import load_dotenv
import os
load_dotenv()


def csv_load(file):
    with open(file, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if '' in (row[1], row[7]):
                continue
            yield (row[1], row[7])


MILVUS_PORT = os.getenv("MILVUS_PORT")
MILVUS_HOST = os.getenv("MILVUS_HOST")

connections.connect(host=MILVUS_HOST, port=MILVUS_PORT)

COLLECTION_NAME = "movies_db"
DIMENSION = 384

fields = [
    FieldSchema(name='id', dtype=DataType.INT64, is_primary=True,
                auto_id=True),  # id is auto=increment
    FieldSchema(name='title', dtype=DataType.VARCHAR, max_length=200),
    FieldSchema(name='embedding', dtype=DataType.FLOAT_VECTOR, dim=DIMENSION)
]
schema = CollectionSchema(fields=fields)
collection = Collection(name=COLLECTION_NAME, schema=schema)

index_params = {
    'metric_type': 'L2',
    'index_type': "IVF_FLAT",
    'params': {'nlist': 1536}
}
collection.create_index(field_name="embedding", index_params=index_params)
collection.load()

BATCH_SIZE = 128

data_batch = [[], []]

count = 0

for title, plot in csv_load('plots.csv'):
    data_batch[0].append(title)
    data_batch[1].append(plot)
    if len(data_batch[0]) % BATCH_SIZE == 0:
        db.insert_data(data_batch)
        data_batch = [[], []]
        print(f"\ninserted... {count} movies")
    count += 1

if len(data_batch[0]) != 0:
    db.insert_data(data_batch)

collection.flush()
