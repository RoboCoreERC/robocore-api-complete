import pytest
import asyncio

from robocore_api.client import RobotClient, _USE_ASYNC

@pytest.mark.asyncio
async def test_client_fallback(monkeypatch):
    """Ensure both async and sync fallbacks work."""
    # Dummy socket for both modes
    class Dummy:
        async def send(self, msg): self._msg = msg
        async def recv(self): return "OK"
        async def close(self): pass

    async def fake_async(uri):
        return Dummy()

    def fake_sync(uri):
        return Dummy()

    if _USE_ASYNC:
        monkeypatch.setattr('robocore_api.client._ws_connect', fake_async)
    else:
        monkeypatch.setattr('robocore_api.client._sync_connect', fake_sync)

    client = RobotClient("ws://test")
    await client.connect()
    await client.move_forward(0.7)
    data = await client.read_sensors()
    assert data == "OK"
    await client.disconnect()
