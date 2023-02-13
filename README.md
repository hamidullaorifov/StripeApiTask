My python version is 3.11.0


#### Requirements

- django
- stripe
- python-dotenv


Steps to run 

### Docker

- `git clone https://github.com/hamidullaorifov/StripeApiTask`
- `cd StripeApiTask`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `docker-compose up`


### Without docker

- `git clone https://github.com/hamidullaorifov/StripeApiTask`
- `cd StripeApiTask`
- create `.env` file and write Environment variables
- `python -m requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate` 
- `python manage.py runserver`





