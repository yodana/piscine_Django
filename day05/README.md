# Installation de la bdd

## Postgresql
> sudo apt install postgresql postgresql-contrib
> sudo service postgresql start

## Creation d un user
> sudo -u postgres psql
> CREATE USER djangouser WITH PASSWORD 'secret';
> CREATE DATABASE formationdjango;

## Setting.py 

>'''DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "formationdjango",
        "USER": "djangouser",
        "PASSWORD": "secret",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}'''

## Check si la table ex00_movies existe
> psql -h 127.0.0.1 -U djangouser -d formationdjango
> \dt

## Faire command script avec manage.py

> python manage.py runscript load_people
