---------------------------------------------------------------SET UP
to see if python is installed

```bash
python3 --version
```

install pipenv

```bash
pip3 install pipenv
```

creates a virtual environment for our project

```bash
pipenv shell
```

Next we install several packages
We need to install django, djangorestframework, and django-rest-knox.
Django Rest Knox has to do with token authentication

```bash
pipenv install django djangorestframework django-rest-knox
```

---------------------------------------------------------------Create Django Project

```bash
django-admin startproject project_name
```

in the project folder you will have access to manage.py
If using VS code make sure you select the right interpreter with the project folder name and pipenv

----------------------------------------------------------------Generate a Django App

```bash
python manage,py startapp app_name
```

whenever you create a new app go into the settings.py and add any apps you create
if you area using the rest framework then make sure to add rest_framework as well
Setting is also where you specify what kind of database you want to use
Check django dox for more

----------------------------------------------------------------Create a Migration
In order to add the models to the database you need to make a migration
python manage.py makemigrations app_name
Now we migrate that to the database

```bash
python manage.py migrate
```

this will perform all migrations

afterwards we need to contruct our serializers.py that will help convert python to json
then we need to make our api.py
then we need to create our URLS
first edit the urls.py in the project folder
then we create the url.py in the app folder
THATS IT after that we should have a basic crud api

Start the server with

```bash
python manage.py runserver
```

Test with Post Man recomended
make sure you have the postman desktop agent installed
