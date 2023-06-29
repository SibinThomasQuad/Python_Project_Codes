from flask import Flask, request, jsonify
import requests

class APIGateway:
    def __init__(self):
        self.app = Flask(__name__)
        self.api_domains = {}

    def register_api_domain(self, api_domain, api_url):
        self.api_domains[api_domain] = api_url

    def run(self):
        @self.app.route('/<api_domain>/<path:path>', methods=['GET', 'POST'])
        def proxy_request(api_domain, path):
            if api_domain not in self.api_domains:
                return jsonify({'error': 'Invalid API domain'})

            url = f"{self.api_domains[api_domain]}/{path}"
            headers = request.headers
            data = request.get_json() if request.method == 'POST' else None

            try:
                response = requests.request(request.method, url, headers=headers, json=data)
                return response.json(), response.status_code
            except requests.exceptions.RequestException as e:
                return jsonify({'error': str(e)}), 500

        self.app.run()

# Example usage
if __name__ == '__main__':
    gateway = APIGateway()
    gateway.register_api_domain('v1', 'http://ip-api.com/json/')
    gateway.register_api_domain('v2', 'http://ip-api.com/json/')
    # Add more API domains as needed

    gateway.run()
