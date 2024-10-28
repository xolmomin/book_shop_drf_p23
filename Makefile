mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

celery:
	celery -A root worker -l INFO --concurrency=4 -Q high_priority -n worker1
	celery -A root worker -l INFO --concurrency=1 -Q low_priority -n worker3

loaddata:
	python3 manage.py loaddata country

flush:
	python3 manage.py flush

user:
	python3 manage.py createsuperuser --email admin@gmail.com

data:
	python3 manage.py generate_data --user 5 --category 5

check:
	isort .
	flake8 .
