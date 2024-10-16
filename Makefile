mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

celery:
	celery -A root worker -l INFO

loaddata:
	python3 manage.py loaddata country

flush:
	python3 manage.py flush

user:
	python3 manage.py createsuperuser --email admin@gmail.com

check:
	isort .
	flake8 .
