freeze-deps:
	pip freeze > requirements.txt

run-debug:
	flask --app application run -p 3001 --debug

generate-embeddings:
	python create_embeddings.py	