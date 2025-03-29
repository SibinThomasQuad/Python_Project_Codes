# FastAPI WebSocket Proxy

This project provides a WebSocket proxy service built with **FastAPI** that allows clients to interact with various HTTP APIs through WebSocket connections. The proxy receives a WebSocket message containing details of an HTTP request, sends the request to the specified endpoint, and returns the response via the WebSocket connection.

## What is a WebSocket Proxy?

A **WebSocket Proxy** allows WebSocket clients to send HTTP requests indirectly by communicating with a WebSocket server, which then forwards these requests to other HTTP servers. In this application, the proxy listens for WebSocket messages from clients, processes the requested HTTP operation (e.g., GET, POST, PUT, DELETE), and returns the result of the HTTP request back to the client in real-time.

This approach enables seamless communication between WebSocket clients and HTTP-based services, offering benefits like faster communication, reduced latency, and simplified interaction in scenarios where WebSockets are preferred over traditional REST API calls.

## Advantages of Using a WebSocket Proxy

### 1. **Real-time Communication**
   - WebSockets offer full-duplex communication channels, which means data can flow in both directions simultaneously. This results in lower latency and real-time interactions.
   - The client can instantly receive responses to its HTTP requests, making it suitable for applications that require immediate feedback, such as live dashboards or interactive web applications.

### 2. **Bidirectional Communication**
   - Unlike HTTP, which is unidirectional (client requests, server responds), WebSockets enable continuous bidirectional communication. Clients can send multiple HTTP requests and receive responses without needing to repeatedly establish connections.

### 3. **Efficient for Long-lived Connections**
   - WebSocket connections remain open, unlike HTTP, where a new connection is established for each request. This makes WebSockets more efficient when you need continuous data exchange over time, especially in scenarios like live notifications, chat systems, or monitoring applications.

### 4. **Centralized API Management**
   - The WebSocket proxy abstracts the complexity of managing different HTTP APIs by centralizing communication. Clients can send their HTTP request details (method, URL, data) to a single WebSocket endpoint, simplifying client-side code and ensuring easier maintenance.
   
### 5. **Bypassing CORS (Cross-Origin Resource Sharing) Issues**
   - WebSocket connections are not subject to the same CORS restrictions as HTTP requests, making it easier to interact with cross-origin APIs without facing CORS-related errors.

### 6. **Reduced Overhead for Frequent Requests**
   - Since WebSockets maintain an open connection, there is no need to repeatedly set up new HTTP connections. This can reduce network overhead and improve efficiency in applications that make frequent API calls.

## Features

- **WebSocket Proxy**: Accepts WebSocket connections at `/ws` and forwards HTTP requests (GET, POST, PUT, DELETE) to the target URL.
- **Supports Multiple HTTP Methods**: Supports `GET`, `POST`, `PUT`, and `DELETE` HTTP methods, making it versatile for a wide range of API interactions.
- **Real-time Responses**: Sends the HTTP response back to the client over the same WebSocket connection.
- **Error Handling**: Returns error messages when required data is missing or when the HTTP method is unsupported.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Requests

To install the necessary dependencies, use the following command:

```bash
pip install fastapi uvicorn requests
