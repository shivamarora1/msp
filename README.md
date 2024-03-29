**MSP**, or Movie Search by Plot, employs semantic-based search techniques to identify relevant movies. Unlike traditional search algorithms that rely on similarity measures, MSP understands the plot of a story, allowing users to find titles that match their actual interests.

Let's see some example:
```
Input: Adventure of scientist in his regular life
Result: The Creeping Flesh

Input: Horror love story
Result: Terror in the Aisles
```

### 👉 Live [Demo](https://movie-search-plot.streamlit.app/)
![recording](https://github.com/shivamarora1/msp/assets/28146775/2062628c-834d-4c07-af0b-090be4d2d8c0)

### Architecture
![msp_architecture drawio (1)](https://github.com/shivamarora1/msp/assets/28146775/51f3ea59-7849-4766-94b2-b39dac4fc2c7)

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

Follow more such content 👉 : https://medium.com/@shivamarora1
