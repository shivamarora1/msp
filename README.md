# MSP
Movie Search by Persona

### Version: 0.01
Backend to validate concept.
1. Set up vector DB
2. Generate embeddings and store it in vector DB
3. Fetch result from that DB. Similarity Search.
## Completed...

### Version: 0.02
API integration.
1. Flask api to fetch and store data.
2. Minimum frontend framework to visualize the results.

### Version: 0.03
1. Finetune frontend for better results.


## How to start MilVus:
`bash standalone_embed.sh start`

## How to stop MilVus:
`bash standalone_embed.sh stop`

Frontend:
1. A search bar to search for plot of movie.
2. Result view that displays result of that search.

Backend:
1. Api to search movie. No auth needed for now. that will return the list of movies. 

Follow format mentioned in https://flask.palletsprojects.com/en/3.0.x/tutorial/layout/