Certainly! Below is a basic example of a FastAPI application that includes an endpoint to send notifications and a WebSocket endpoint to handle live notifications for a specific user. This example uses `websockets` for WebSocket support. Make sure to install the necessary packages:

```bash
pip install fastapi uvicorn websockets
```

Now, let's create a FastAPI application:

**Step 1: Create `main.py`**

```python
# main.py

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn
import asyncio

app = FastAPI()

# Store user WebSocket connections in a dictionary
user_connections = {}


@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await websocket.accept()
    user_connections[user_id] = websocket
    try:
        while True:
            # This is a basic example, you may want to implement more advanced logic here
            message = await websocket.receive_text()
            print(f"Received message for User {user_id}: {message}")

            # Send the received message back to the same user
            await websocket.send_text(f"Received your message: {message}")
    except asyncio.CancelledError:
        pass
    finally:
        del user_connections[user_id]


@app.get("/send_notification/{user_id}/{message}")
async def send_notification(user_id: int, message: str):
    if user_id in user_connections:
        # Send a notification to the specified user's WebSocket connection
        websocket = user_connections[user_id]
        await websocket.send_text(f"Notification: {message}")
        return {"status": "Notification sent"}
    else:
        return {"status": "User not connected"}


@app.get("/")
async def get():
    return HTMLResponse("<h1>WebSocket Notification Server</h1>")
```

**Step 2: Run the FastAPI application**

```bash
uvicorn main:app --reload
```

This will start the FastAPI application, and you can access it at `http://127.0.0.1:8000/`.

**Step 3: Test the WebSocket connection and notification**

- Open your browser and visit `http://127.0.0.1:8000/` to see a simple message.
- Open a WebSocket connection using JavaScript in the browser console:

  ```javascript
  const socket = new WebSocket('ws://127.0.0.1:8000/ws/1');
  
  socket.onopen = (event) => {
      console.log('WebSocket connection opened:', event);
  };

  socket.onmessage = (event) => {
      console.log('Received message:', event.data);
  };

  socket.onclose = (event) => {
      console.log('WebSocket connection closed:', event);
  };
  ```

- Open another browser tab and visit the URL `http://127.0.0.1:8000/send_notification/1/Hello%20User`.
- Observe the WebSocket connection tab to see the notification being received.

This example demonstrates a simple WebSocket server with FastAPI where you can send notifications to a specific user using a URL endpoint and handle WebSocket connections for live notifications. Customize the logic according to your requirements.
