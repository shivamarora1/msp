**MSP**, or Movie Search by Plot, employs semantic-based search techniques to identify relevant movies. Unlike traditional search algorithms that rely on similarity measures, MSP understands the plot of a story, allowing users to find titles that match their actual interests.

Let's see some example:
```
Input: Adventure of scientist in his regular life
Result: The Creeping Flesh

Input: Horror love story
Result: Terror in the Aisles
```

### 👉 Live [Demo](https://movie-search-plot.streamlit.app/)

### Architecture
![msp_architecture](https://github.com/shivamarora1/msp/assets/28146775/9066f40a-09aa-49ea-9751-2dffbc03dfce)

[**Milvus**](https://milvus.io/): Vector database to store embedding vectors. Milvus free community cloud version also (available)[https://cloud.zilliz.com/]<br>
[**all-MiniLM-L6-v2**](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2): Sentence model used to map sentence and paragraphs in 384 dimensional vector space. This model converts normal sentence to vector embeddings.

### Steps to run project
1. Run `bash standalone_embed.sh start` to host Milvus database in local.
2. Set `MILVUS_URI`, `MILVUS_TOKEN` in `.env` file with appropriate value.
3. Movies dataset
```
Release Year | Title | Origin/Ethnicity | Director | Cast | Genre | Wiki Page | Plot | Image
```
You can download data set from [Hugging face](https://huggingface.co/datasets/Coder-Dragon/wikipedia-movies).

4. Set up virtual environment.
```
python3 -m venv .venv
source .venv/bin/activate
```
5. Install required dependencies
```
pip install -r requirements
```
6. Create and store movies plot embeddings
```
python create_embeddings.py
``` 
7. Run application
```
make run-streamlit-app
```
8. Streamlit app should be open in browser


### Demo
![recording](https://github.com/shivamarora1/msp/assets/28146775/128e700f-7243-450b-b70c-324fe2d49d5d)


Follow more such content 👉 : https://medium.com/@shivamarora1
