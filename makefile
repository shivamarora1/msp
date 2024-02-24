freeze-deps:
	pip freeze > requirements.txt

run-debug:
	flask --app application run -p 3001 --debug