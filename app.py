import streamlit as st
import random
from sentence_transformers import SentenceTransformer
from pymilvus import (connections, Collection)
import math
import os

MILVUS_TOKEN = os.getenv("MILVUS_TOKEN")
MILVUS_URI = os.getenv("MILVUS_URI")


COLLECTION_NAME = "movies_db"

# * backend functions for fetching data


@st.cache_resource
def load_collection():
    connections.connect(uri=MILVUS_URI,
                        token=MILVUS_TOKEN)
    collection = Collection(COLLECTION_NAME)
    collection.load()
    return collection


@st.cache_resource
def load_transformer_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


@st.cache_data
def generate_embeddings(data: list[str]):
    transformer = load_transformer_model()
    embeddings = transformer.encode(data)
    return [x for x in embeddings]


@st.cache_data
def search_data(data: list[str]):
    top_k = random.randint(10, 40)
    search_embeddings = generate_embeddings(data)
    collection = load_collection()
    resp = collection.search(data=search_embeddings, anns_field="embedding", param={
                             'metric_type': 'L2', 'params': {'nprobe': 10}}, limit=top_k,
                             output_fields=['title', 'image'])
    result = {}
    for i, hits in enumerate(resp):
        result[data[i]] = [{"title": hit.entity.get(
            'title'), "image": hit.entity.get(
            'image'), "match": hit.distance} for hit in hits]
    return result
## ** ##


# * UI code
if 'show_query_error' not in st.session_state:
    st.session_state.show_query_error = False

if 'movie_search_result' not in st.session_state:
    st.session_state.movie_search_result = []

st.set_page_config(layout="wide")

# * search bar and text input
col1, col2 = st.columns([0.9, 0.1])
with col1:
    query = st.text_input(
        label="query", key='query', label_visibility="collapsed", placeholder="Search plot of movie")

with col2:
    if st.button(label="Search"):
        if query:
            st.session_state.show_query_error = False
            query = query.strip()
            result = search_data([query])
            st.session_state.movie_search_result = result
        else:
            st.session_state.show_query_error = True
            st.session_state.movie_search_result = []

if st.session_state.show_query_error:
    st.error("Pls enter movie plot to search..")

# * rendering images based on results
if st.session_state.movie_search_result:
    result = st.session_state.movie_search_result
    query = st.session_state.query

    if query in result:
        items = result[query]
        NUM_COLS = 5
        rows_count = math.ceil(len(items)/NUM_COLS)
        for row in range(rows_count):
            st_cols = st.columns(NUM_COLS)
            start = row * NUM_COLS
            end = min(start+NUM_COLS, len(items))
            i = start
            for cols in st_cols:
                if i == end:
                    break

                with cols:
                    with st.container(border=True):
                        st.markdown(f"**{items[i]['title']}**")
                        st.image(f"https://{items[i]['image']}")
                i = i+1
    else:
        st.error(f"No result found for {query}")
