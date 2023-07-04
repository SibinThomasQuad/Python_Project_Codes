#!/bin/bash

# Install Django
pip install django

# Create a Django project
django-admin startproject myproject

# Change to the project directory
cd myproject

# Create a Django app
python manage.py startapp myapp

# Create a templates folder
mkdir myapp/templates

# Create a static folder
mkdir myapp/static

# Update settings.py to include the templates directory
echo "
import os

# ...

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'myapp/templates')],
        # ...
    },
]

# ..." >> myproject/settings.py

# Output success message
echo "Django project, app, templates folder, and static folder created successfully!"
