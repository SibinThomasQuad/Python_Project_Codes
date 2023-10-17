Certainly, here's the full code for the Flask API with the custom MySQL query example included:

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/mydatabase'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

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

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_list.append({'id': user.id, 'username': user.username, 'email': user.email})
    return jsonify({'users': user_list})

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'})

# Custom MySQL query example
@app.route('/custom_query', methods=['GET'])
def custom_query():
    query_result = db.engine.execute("SELECT id, title FROM books WHERE author = 'AuthorName'")
    custom_result = [{'id': row.id, 'title': row.title} for row in query_result]
    return jsonify({'custom_query_result': custom_result})

if __name__ == '__main__':
    app.run()
```

This code includes the custom MySQL query endpoint, which allows you to retrieve data from the "Books" table where the author is 'AuthorName'. Remember to replace `'mysql://username:password@localhost/mydatabase'` with your actual MySQL database connection details, and customize the query as needed.
