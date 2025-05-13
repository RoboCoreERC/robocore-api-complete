import asyncio

# Try primary async websockets implementation…
try:
    from websockets import connect as _ws_connect
    _USE_ASYNC = True
except ImportError:
    _USE_ASYNC = False
    # Fallback to sync websocket-client
    from websocket import create_connection as _sync_connect

class RobotClient:
    """Async client for RoboCore robot communication over WebSocket."""

    def __init__(self, uri: str):
        self.uri = uri
        self.ws  = None

    async def connect(self):
        """Establish a connection, async if possible, else in thread."""
        if _USE_ASYNC:
            self.ws = await _ws_connect(self.uri)
        else:
            loop = asyncio.get_running_loop()
            self.ws = await loop.run_in_executor(None, _sync_connect, self.uri)

    async def disconnect(self):
        """Close the connection."""
        if not self.ws:
            return
        if _USE_ASYNC:
            await self.ws.close()
        else:
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(None, self.ws.close)

    async def move_forward(self, speed: float):
        """Send a MOVE_FORWARD command."""
        cmd = f"MOVE_FORWARD {speed}"
        if _USE_ASYNC:
            await self.ws.send(cmd)
        else:
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(None, self.ws.send, cmd)

    async def read_sensors(self) -> str:
        """Request and return sensor data."""
        if _USE_ASYNC:
            await self.ws.send("READ_SENSORS")
            return await self.ws.recv()
        else:
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(None, self.ws.send, "READ_SENSORS")
            return await loop.run_in_executor(None, self.ws.recv)
