import socket
import threading

# Server configuration
HOST = 'localhost'
PORT = 5000

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print('Server listening on {}:{}'.format(HOST, PORT))

# Store client connections and names
clients = {}

def handle_client(client_socket, client_address):
    # Receive the client name
    client_name = client_socket.recv(1024).decode()
    print('Received client name:', client_name)

    # Store the client connection based on name
    clients[client_name] = client_socket

    while True:
        try:
            # Receive the message from the client
            message = client_socket.recv(1024).decode()
            if message:
                recipient_name, message_text = message.split(':', 1)
                recipient_socket = clients.get(recipient_name)
                if recipient_socket:
                    recipient_socket.send('{}: {}'.format(client_name, message_text).encode())
        except:
            break

    # Remove the client from the dictionary when the connection is closed
    if client_name in clients:
        del clients[client_name]

    client_socket.close()

def run_server():
    while True:
        # Accept client connections
        client_socket, client_address = server_socket.accept()
        print('Client connected:', client_address)

        # Handle the client in a separate thread
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# Example usage
if __name__ == '__main__':
    run_server()
