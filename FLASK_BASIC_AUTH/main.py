from flask import Flask, request
from flask_basicauth import BasicAuth

app = Flask(__name__)

# Configure basic authentication
app.config['BASIC_AUTH_USERNAME'] = 'username'  # Change to your desired username
app.config['BASIC_AUTH_PASSWORD'] = 'password'  # Change to your desired password
basic_auth = BasicAuth(app)

# Define a protected route that requires basic authentication
@app.route('/protected')
@basic_auth.required
def protected_resource():
    return "This is a protected resource."

if __name__ == '__main__':
    app.run(debug=True)


#pip install Flask Flask-BasicAuth
