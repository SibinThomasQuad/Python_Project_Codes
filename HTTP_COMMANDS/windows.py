import subprocess
import urllib.parse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class CommandCenterHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the query parameters
        parsed_url = urllib.parse.urlparse(self.path)
        command = urllib.parse.parse_qs(parsed_url.query).get('command', [None])[0]
        
        if command:
            try:
                # Windows command execution requires running through cmd.exe
                if os.name == 'nt':  # Check if we're on Windows
                    # Use cmd.exe to execute the command on Windows
                    command = f'cmd.exe /c {command}'
                else:
                    # On non-Windows (Linux/macOS), we can directly execute the command
                    command = command

                # Execute the command using subprocess
                result = subprocess.run(command, shell=True, capture_output=True, text=True)

                # Check if the command executed successfully
                if result.returncode == 0:
                    output = result.stdout
                else:
                    output = result.stderr

                # Escape the output for JSON and ensure no invalid control characters
                output = output.replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t')

            except Exception as e:
                output = str(e)

            # Send the response
            response = {
                "status": "success",
                "output": output
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            # If no command is provided, send an error response
            response = {
                "status": "error",
                "message": "No command provided"
            }
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=CommandCenterHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
