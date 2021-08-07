include .env
export $(shell sed 's/=.*//' .env)

run:
	flask run

ngrok: #bash
	./ngrok http 5000

freeze:
	pip freeze > requirements.txt
