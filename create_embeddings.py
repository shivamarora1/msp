from pymilvus import (connections, Collection)
from sentence_transformers import SentenceTransformer
import csv
from pymilvus import (
    utility, FieldSchema, CollectionSchema, DataType, Collection
)
from datasets import load_dataset
from dotenv import load_dotenv
import os

load_dotenv()


COLLECTION_NAME = "movies_db"

MILVUS_TOKEN = os.getenv("MILVUS_TOKEN")
MILVUS_URI = os.getenv("MILVUS_URI")
DIMENSION = 384


def csv_load(file):
    with open(file, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if '' in (row[1], row[7], row[8]):
                continue
            yield (row[1], row[7], row[8])


transformer = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(data: list[str]):
    embeddings = transformer.encode(data)
    return [x for x in embeddings]


connections.connect(uri=MILVUS_URI,
                    token=MILVUS_TOKEN)

if utility.has_collection(collection_name=COLLECTION_NAME):
    utility.drop_collection(collection_name=COLLECTION_NAME)

fields = [
    FieldSchema(name='id', dtype=DataType.INT64, is_primary=True,
                auto_id=True),  # id is auto=increment
    FieldSchema(name='title', dtype=DataType.VARCHAR, max_length=200),
    FieldSchema(name='embedding', dtype=DataType.FLOAT_VECTOR, dim=DIMENSION),
    FieldSchema(name='image', dtype=DataType.VARCHAR, max_length=500),
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


def insert_data(data):
    embeddings = generate_embeddings(data[1])
    ins = [
        data[0],
        embeddings,
        data[2],
    ]
    collection.insert(ins)


BATCH_SIZE = 128

data_batch = [[], [], []]

count = 0

for title, plot, image in csv_load('data/plots.csv'):
    data_batch[0].append(title)
    data_batch[1].append(plot)
    data_batch[2].append(image)
    if len(data_batch[0]) % BATCH_SIZE == 0:
        insert_data(data_batch)
        data_batch = [[], [], []]
        print(f"\ninserted... {count} movies")
    count += 1

if len(data_batch[0]) != 0:
    insert_data(data_batch)

collection.flush()
