freeze-deps:
	pip freeze > requirements.txt

run-streamlit-app:
	streamlit run app.py

generate-embeddings:
	python create_embeddings.py	