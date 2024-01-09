# Budget Management Backend

## On Local without Docker

0. you should have the following requirements installed on your machine
- python3.11
- postgresql

1. create a python virtual environment and activate
```bash
python3 -m venv .venv
source ./venv/bin/activate
```
2. create the postgres database
```bash
psql -U postgres
CREATE DATABASE "db.django-drf-template";
``` 
3. create `.env` file based on `sample.env` in `deploy/` directory.
4. migrate the database
```bash
python manage.py makemigrations
python manage.py migrate
```
5. run django server
```bash
python manage.py runserver
```