import asyncio
import websockets

async def websocket_client():
    uri = "ws://192.168.2.93:8000/ws/81"

    async with websockets.connect(uri) as websocket:
        print("WebSocket connection opened")

        while True:
            try:
                message = await websocket.recv()
                print(f"Received message: {message}")
            except websockets.ConnectionClosed:
                print("WebSocket connection closed")
                break

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(websocket_client())
