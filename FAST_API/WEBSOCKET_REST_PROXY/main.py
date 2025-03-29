import json
import requests
from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse
from fastapi.websockets import WebSocketDisconnect
from typing import Optional

app = FastAPI()

# WebSocket proxy endpoint
@app.websocket("/ws")
async def websocket_proxy(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Receive a message from the client
            message = await websocket.receive_text()
            try:
                # Parse the message as JSON
                data = json.loads(message)

                # Extract necessary information from the data
                url = data.get("url")
                method = data.get("method", "GET").upper()
                payload = data.get("data", None)

                if not url or not method:
                    # If URL or method is missing, send an error response
                    await websocket.send_text(json.dumps({"error": "Missing URL or method"}))
                    continue

                # Make the HTTP request based on the provided method
                if method == "GET":
                    response = requests.get(url, params=payload)
                elif method == "POST":
                    response = requests.post(url, json=payload)
                elif method == "PUT":
                    response = requests.put(url, json=payload)
                elif method == "DELETE":
                    response = requests.delete(url, json=payload)
                else:
                    await websocket.send_text(json.dumps({"error": f"Unsupported HTTP method: {method}"}))
                    continue

                # Send back the response from the HTTP request
                result = {
                    "status_code": response.status_code,
                    "headers": dict(response.headers),
                    "content": response.json() if response.status_code == 200 else response.text
                }
                await websocket.send_text(json.dumps(result))

            except Exception as e:
                await websocket.send_text(json.dumps({"error": f"Failed to process the request: {str(e)}"}))

    except WebSocketDisconnect:
        print("Client disconnected")


# Run the FastAPI app with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8765)
