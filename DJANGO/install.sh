#!/bin/bash

# Install Django
pip install django

# Create a Django project
django-admin startproject myproject

# Change to the project directory
cd myproject

# Create a Django app
python manage.py startapp myapp

# Output success message
echo "Django project and app created successfully!"
