from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define API endpoints for different domains
API_DOMAINS = {
    'v1': 'http://ip-api.com/json/',
    'v2': 'http://ip-api.com/json/',
    # Add more API domains as needed
}

@app.route('/<api_domain>/<path:path>', methods=['GET', 'POST'])
def proxy_request(api_domain, path):
    if api_domain not in API_DOMAINS:
        return jsonify({'error': 'Invalid API domain'})

    url = f"{API_DOMAINS[api_domain]}/{path}"
    headers = request.headers
    data = request.get_json() if request.method == 'POST' else None

    try:
        response = requests.request(request.method, url, headers=headers, json=data)
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
