from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/api/<path:path>', methods=['GET', 'POST'])
def proxy(path):
    # Define the base URL of the target API
    base_url = 'http://ip-api.com/json/'
    
    # Construct the target URL
    target_url = base_url + '/' + path
    
    # Forward the request to the target API
    if request.method == 'GET':
        response = requests.get(target_url, params=request.args)
    elif request.method == 'POST':
        response = requests.post(target_url, data=request.form)
    
    # Return the response from the target API
    return response.content, response.status_code, response.headers.items()

if __name__ == '__main__':
    app.run()
