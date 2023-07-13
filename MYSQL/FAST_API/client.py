import requests

# Base URL
base_url = 'http://localhost:5000/users'

# GET Request
def get_user(user_id):
    url = f'{base_url}/{user_id}'
    response = requests.get(url)
    print(response.json())

# POST Request
def create_user(name, email):
    url = base_url
    data = {'name': name, 'email': email}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    print(response.json())

# PUT Request
def update_user(user_id, name, email):
    url = f'{base_url}/{user_id}'
    data = {'name': name, 'email': email}
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, json=data, headers=headers)
    print(response.json())

# DELETE Request
def delete_user(user_id):
    url = f'{base_url}/{user_id}'
    response = requests.delete(url)
    print(response.json())

# Examples
get_user(1)  # Get user with ID 1
create_user('Mt', 'johndoe@example.com')  # Create a new user
update_user(1, 'Mt2', 'johnsmith@example.com')  # Update user with ID 1
delete_user(1)  # Delete user with ID 1
