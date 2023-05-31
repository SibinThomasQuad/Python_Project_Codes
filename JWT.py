import base64
import hmac
import json

class JWT:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def create_token(self, payload):
        header = {
            'typ': 'JWT',
            'alg': 'HS256'
        }

        base64_url_header = self.base64_url_encode(json.dumps(header).encode('utf-8'))
        base64_url_payload = self.base64_url_encode(json.dumps(payload).encode('utf-8'))

        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            (base64_url_header + '.' + base64_url_payload).encode('utf-8'),
            digestmod='sha256'
        ).digest()

        base64_url_signature = self.base64_url_encode(signature)

        token = base64_url_header + '.' + base64_url_payload + '.' + base64_url_signature
        return token

    def verify_token(self, token):
        parts = token.split('.')

        header = parts[0]
        payload = parts[1]
        signature = parts[2]

        base64_url_header = self.base64_url_decode(header)
        base64_url_payload = self.base64_url_decode(payload)

        new_signature = hmac.new(
            self.secret_key.encode('utf-8'),
            (header + '.' + payload).encode('utf-8'),
            digestmod='sha256'
        ).digest()

        base64_url_new_signature = self.base64_url_encode(new_signature)

        if signature == base64_url_new_signature:
            return json.loads(base64_url_payload)

        return False

    def base64_url_encode(self, data):
        base64_data = base64.urlsafe_b64encode(data).rstrip(b'=')
        base64_url_data = base64_data.decode('utf-8')
        return base64_url_data

    def base64_url_decode(self, data):
        base64_url_data = data + '=' * (4 - (len(data) % 4))
        base64_data = base64.urlsafe_b64decode(base64_url_data)
        return base64_data.decode('utf-8')

# Example usage
secret_key = 'your_secret_key'
jwt = JWT(secret_key)

# Create JWT token
payload = {
    'user_id': 123,
    'username': 'john_doe'
}
token = jwt.create_token(payload)
print('Token:', token)

# Verify and retrieve data from JWT token
decoded_payload = jwt.verify_token(token)
if decoded_payload:
    print('Decoded Payload:', decoded_payload)
else:
    print('Invalid token.')
