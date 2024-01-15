To add logging to your FastAPI WebSocket application, you can use the built-in `logging` module. Below is an updated version of your `main.py` with logging added:

```python
import logging
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn
import asyncio

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Store user WebSocket connections in a dictionary
user_connections = {}


@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    logger.info(f"WebSocket connection opened for User {user_id}")
    await websocket.accept()
    user_connections[user_id] = websocket
    try:
        while True:
            # This is a basic example, you may want to implement more advanced logic here
            message = await websocket.receive_text()
            logger.info(f"Received message for User {user_id}: {message}")

            # Send the received message back to the same user
            await websocket.send_text(f"Received your message: {message}")
    except asyncio.CancelledError:
        pass
    finally:
        del user_connections[user_id]
        logger.info(f"WebSocket connection closed for User {user_id}")


@app.get("/send_notification/{user_id}/{message}")
async def send_notification(user_id: int, message: str):
    if user_id in user_connections:
        # Send a notification to the specified user's WebSocket connection
        websocket = user_connections[user_id]
        await websocket.send_text(f"Notification: {message}")
        logger.info(f"Notification sent to User {user_id}: {message}")
        return {"status": "Notification sent"}
    else:
        logger.warning(f"Attempted to send notification to User {user_id}, but user is not connected")
        return {"status": "User not connected"}


@app.get("/")
async def get():
    return HTMLResponse("<h1>WebSocket Notification Server</h1>")
```

In this modification:

- The `logging` module is imported, and a logger named `__name__` is created.
- Logging statements (`logger.info` and `logger.warning`) are added at different points in the WebSocket logic and notification sending logic.

This allows you to log relevant information about WebSocket connections, received messages, and notifications sent. You can adjust the logging level and format based on your preferences and requirements.
