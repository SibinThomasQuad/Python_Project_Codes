import requests

def get_data(url):
    response = requests.get(url)
    return response.json()

def post_data(url, data):
    response = requests.post(url, json=data)
    return response.json()

def put_data(url, data):
    response = requests.put(url, json=data)
    return response.json()
