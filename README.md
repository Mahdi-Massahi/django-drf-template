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
```
```psql
CREATE DATABASE "db.django-drf-template";
``` 
3. create `backend.env` file based on `backend.env.example` in `deploy/environments/` directory.
4. migrate the database
```bash
python manage.py makemigrations
python manage.py migrate
```
5. create a superuser
```bash
python manage.py custom_createsuperuser
```
6. run django server
```bash
python manage.py runserver 8000
```
now the app should be accessible on http://localhost:8000

## On Local with Docker

0. you should have `Docker` installed on your machine  

1. create self-signed ssl certification
```bash
openssl req -x509 -newkey rsa:4096 -keyout deploy/config/ssl/privkey.pem -out deploy/config/ssl/fullchain.pem -days 365 -nodes
```
2. build and run
```bash
docker-compose up --build -d
```
now the app should be accessible on https://localhost
Note: ignore the certification error on the browser