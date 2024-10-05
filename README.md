- make sure pip is installed `pip3 list`
- make venv `python3 -m venv djangoenv`
	- l`ls`
- Start django env`source djangoenv/bin/activate`
- Install django inside env`pip install django`
- `$ django-admin --version`
	- 5.1.1
- `brew update`
- `brew install postgresql`
- `django-admin startproject locallibrary`
- `python3 manage.py startapp catalog`
- Create app called catalog`manage.py startapp catalog`
- Add this line to INSTALLED APPS: `'catalog.apps.CatalogConfig',`
- start the postgresql service `brew services start postgresql`
- access shell `psql postgres`
- create the db: `# create database test_db;`
- `create user admin with password 'password';`
- `grant all privileges on database test_db to admin;`
- list all db's `\l`
- install psycopg2 `pip install psycopg2`
- edit settings.py DATABASES:
``` Python
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'test_db',
		'USER': 'admin',
		'PASSWORD': 'password',
		'HOST': 'localhost',
		'PORT':'5432',
	}

}
```
- `python manage.py migrate`
- `python manage.py runserver`