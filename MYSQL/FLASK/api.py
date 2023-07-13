from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# MySQL connection details
app = Flask(__name__)
password = ""
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:'+password+'@localhost/ms'
db = SQLAlchemy(app)

# Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __init__(self, name, email):
        self.name = name
        self.email = email

# Create tables if they don't exist
db.create_all()

# Routes
@app.route('/users', methods=['POST'])
def create_user():
    name = request.json['name']
    email = request.json['email']

    new_user = User(name, email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created'})

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)

    if user:
        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email
        }
        return jsonify(user_data)

    return jsonify({'message': 'User not found'})

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)

    if user:
        user.name = request.json['name']
        user.email = request.json['email']
        db.session.commit()

        return jsonify({'message': 'User updated'})

    return jsonify({'message': 'User not found'})

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()

        return jsonify({'message': 'User deleted'})

    return jsonify({'message': 'User not found'})

if __name__ == '__main__':
    app.run(debug=True)
