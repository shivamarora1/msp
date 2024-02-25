**MSP**, or Movie Search by Plot, employs semantic-based search techniques to identify relevant movies. Unlike traditional search algorithms that rely on similarity measures, MSP understands the plot of a story, allowing users to find titles that match their actual interests.

Let's see some example:
```
Input: Adventure of scientist in his regular life
Result: The Creeping Flesh

Input: Horror love story
Result: Terror in the Aisles
```

### Architecture
**Milvus**: Vector database to store embedding vectors. <br>
**all-MiniLM-L6-v2**: Sentence model used to map sentence and paragraphs in 384 dimensional vector space. This model converts normal sentence to vector embeddings.

<Diagram will go here>

### Steps to run
1. Run `bash standalone_embed.sh start` to host Milvus database in local.
2. Set `MILVUS_PORT`, `MILVUS_HOST` in `.env` file with appropriate value.
3. Movies dataset having 
```
Release Year | Title | Origin/Ethnicity | Director | Cast | Genre | Wiki Page | Plot
```
columns is stored in `data/plots.csv`.<br>
4. Set up virtual environment.
```
python3 -m venv .venv
source .venv/bin/activate
```
5. Install required dependencies
```
pip install -r requirements
```
6. Create and Store movies plot embeddings
```
python create_embeddings.py
``` 
7. Run application
```
make run-debug
```
8. Application running in http://127.0.0.1:3001


### Demo


Tech stack used.
Creating embeddings, searching embeddings
Write note of it.

vector field `embedding` used to search collection. `title` field is returned when search is complete.
max number of record returned `top_k` are 3 .

## Todo:
Check similarity algorithm.
Images not available

