Certainly, if you want to execute raw MySQL queries using SQLAlchemy, here are examples of how to perform CRUD (Create, Read, Update, Delete) operations using raw SQL queries:

```python
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application (you can use Flask or any other framework)
# For simplicity, we're not setting up a complete Flask app in this example.

app = Flask(__name)

# Configure the MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/mydatabase'
db = SQLAlchemy(app)

# Insert a new book using a raw SQL query
insert_query = "INSERT INTO books (title, author) VALUES ('Sample Book', 'Sample Author');"
db.session.execute(insert_query)
db.session.commit()

# Update a book using a raw SQL query
update_query = "UPDATE books SET author = 'Updated Author' WHERE title = 'Sample Book';"
db.session.execute(update_query)
db.session.commit()

# Read all books using a raw SQL query
select_query = "SELECT * FROM books;"
result = db.session.execute(select_query)
books = result.fetchall()
for book in books:
    print(f"Book ID: {book.id}, Title: {book.title}, Author: {book.author}")

# Delete a book using a raw SQL query
delete_query = "DELETE FROM books WHERE title = 'Sample Book';"
db.session.execute(delete_query)
db.session.commit()
```

In this example, we use raw SQL queries to perform the following operations:

1. Insert a new book.
2. Update the author of a book.
3. Retrieve all books.
4. Delete a book from the database.

Remember to replace `'mysql://username:password@localhost/mydatabase'` with your actual MySQL database connection details, and customize the SQL queries as needed for your specific use case.
