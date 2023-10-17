Creating a simple Flask API to manage books with MySQL and migration files requires several steps. You'll need to set up your Flask application, create database models, set up routes for various operations (insert, delete, get, update), and use a tool like Flask-Migrate to handle database migrations. Here's a step-by-step guide with example code:

**Step 1: Set Up Your Flask Application**

First, you need to set up your Flask application and initialize necessary extensions.

```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

```python
# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/mydatabase'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
```

**Step 2: Create a Model for Books**

Define a model to represent books in your database.

```python
# models.py
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
```

**Step 3: Create Migration Files**

Generate migration files to create the database schema.

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

**Step 4: Create API Endpoints**

Set up API endpoints for managing books (insert, delete, get, update).

```python
# routes.py
from app import app, db
from flask import request, jsonify
from models import Book

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    book_list = []
    for book in books:
        book_list.append({'id': book.id, 'title': book.title, 'author': book.author})
    return jsonify({'books': book_list})

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author=data['author'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'})

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted successfully'})
    return jsonify({'message': 'Book not found'})

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = Book.query.get(id)
    if book:
        book.title = data['title']
        book.author = data['author']
        db.session.commit()
        return jsonify({'message': 'Book updated successfully'})
    return jsonify({'message': 'Book not found'})
```

**Step 5: Run the Application**

Run your Flask application to start the API server.

```bash
flask run
```

Your API is now accessible at `http://localhost:5000`. You can use tools like `curl` or Postman to make requests to your API endpoints:

- `GET /books`: Get a list of all books.
- `POST /books`: Insert a new book.
- `DELETE /books/<id>`: Delete a book by its ID.
- `PUT /books/<id>`: Update a book by its ID.

Make sure to replace `'mysql://username:password@localhost/mydatabase'` with your MySQL database connection information.
