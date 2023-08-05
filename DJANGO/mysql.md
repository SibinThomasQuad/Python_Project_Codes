markdown

# Connecting Django to MySQL Database

In Django, you can connect to MySQL as the database backend for your web application. Follow these steps to configure your Django project to use MySQL:

## Step 1: Install MySQL Database Driver

Make sure you have the MySQL database driver installed in your Python environment. You can install it using pip:

```bash
pip install mysqlclient

Step 2: Update Django Settings

Open your Django project's settings.py file and update the DATABASES configuration to use MySQL:

python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',  # Or your MySQL server host
        'PORT': '3306',      # Or your MySQL server port
    }
}

Replace 'your_database_name', 'your_mysql_username', and 'your_mysql_password' with your actual MySQL database name, username, and password.
Step 3: Run Migrations

After configuring the MySQL settings, apply the database migrations to create the necessary tables:

bash

python manage.py migrate

Step 4: Test the Connection

You can now run your Django development server and test the MySQL database connection:

bash

python manage.py runserver

If everything is set up correctly, your Django application will now use MySQL as the database backend.

Remember to install the correct database driver for MySQL, and ensure that the database credentials in the settings.py file are accurate. With these steps, your Django project will be connected to the MySQL database. Happy coding!

css


You can use this README.md content to guide users on how to connect Django to a MySQL database in your GitHub repository.

