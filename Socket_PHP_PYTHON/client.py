import socket
import threading

# Server configuration
HOST = 'localhost'
PORT = 5000

def receive_messages(client_socket):
    while True:
        try:
            # Receive messages from the server
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
# Prompt the client for a name
client_name = input('Enter your name: ')
client_socket.send(client_name.encode())
# Start separate threads for receiving and sending messages
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

