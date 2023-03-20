**python version - 3.11.0**



#### Requirements

- django
- stripe
- python-dotenv


Steps to run 

### Docker

- `git clone https://github.com/hamidullaorifov/StripeApiTask`
- `cd StripeApiTask`
- `docker-compose up -d`
- `docker-compose exec web python manage.py migrate`


### Without docker

- `git clone https://github.com/hamidullaorifov/StripeApiTask`
- `cd StripeApiTask`
- create `.env` file and write Environment variables
- create virtual environment (optional) `python -m venv env`
- if created virtual invironment activate virtual environment `env\Scripts\activate` (for windows)
- `pip install -r requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate` 
- `python manage.py runserver`





