# Django-setup
This repository contains a Django MVC setup for learning purposes

This is a Django project following the tutorial:
https://docs.djangoproject.com/en/3.0/intro/tutorial01/

Project Structure:
manage​.​py
djangosetup​/
init​.​py
settings​.​py
urls​.​py
wsgi​.​py

These files are:

● The outer ​ djangosetup/ ​ ​root directory​ is just a container for your project. Its name doesn’t
matter to Django; you can rename it to anything you like.

● manage.py ​: A ​command-line utility​ that lets you interact with this Django project in
various ways.

● The ​inner ​ djangosetup/ ​ directory is the actual Python package for your project.

● djangosetup/init.py ​: An empty file that tells Python that this directory should be
considered a Python package.

● djangosetup/settings.py ​: Settings/​configuration​ for this Django project.

● djangosetup/urls.py ​: The ​URL declarations​ for this Django project; a “table of contents” of
your Django-powered site.

● djangosetup/wsgi.py ​: An entry-point for WSGI-compatible web servers to serve your
project.

Commands:

**django-admin startproject projname** ​→ create project
Focus on writing code rather than creating directories.

**python manage.py runserver (0:​8080)** ​→ listen on all available public IPs

**python manage.py startapp polls** ​→ create app

Db:

**python manage.py migrate**​ → create the tables in the database before we can use them
( looks at the INSTALLED_APPS setting and creates any necessary database tables
according to the database settings in your mysite/settings.py file and the database
migrations shipped with the app).

**python manage.py makemigrations polls** ​→ store changes to the models as a
migration.

**python manage.py sqlmigrate polls ​ 0001 **​→ take migration names and returns
their SQL. Doesn’t actually run the migration on your database - it just prints it to the
screen so that you can see what SQL Django thinks is required. It’s useful for checking
what Django is going to do or if you have database administrators who require SQL
scripts for changes.

**python manage.py migrate** ​→ run the migration on your database. Take all the
migrations that haven’t been applied (Django tracks which ones are applied using a
special table in your database called django_migrations) and runs them against the
database - essentially, synchronizing the changes to the models with the schema in the
database.

**python manage.py createsuperuser** → ​create superuser (username: ict4d,
pass: kasadaka)

**python manage.py test polls**​ → running tests

Django test client ​ - Django provides a test Client to simulate a user interacting with the
code at the view level.

Observations:

● Project vs App: A project can contain multiple apps. An app can be in multiple
projects.

● Default db SQLite (included in Python)
