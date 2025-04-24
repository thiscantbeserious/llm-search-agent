# llm_search_agent/runners/websocket.py

import sys
import json
import asyncio
from http import HTTPStatus

import websockets
from websockets import ServerConnection, Request, Response

from llm_search_agent.config import Config
from llm_search_agent.orchestrator import run_pipeline

cfg = Config()


async def is_alive(
        host: str | None = None,
        port: int | None = None,
        timeout: float = 3.0
) -> bool:
    """
    Connects to ws://host:port, sends '__health__', and expects '__ok__'.
    Returns True if successful within `timeout` seconds.
    """
    uri = f"ws://{host or cfg.socket_host}:{port or cfg.socket_port}"
    try:
        # Use a short-lived connection just for health
        async with websockets.connect(uri, ping_timeout=timeout) as ws:
            pong = await ws.ping()
            await asyncio.wait_for(pong, timeout)
            return True
    except Exception:
        return False


async def ws_handler(ws: ServerConnection) -> None:
    """
    Handler gets a ServerConnection (asyncio) instance.
    Use ws.send()/ws.recv() or `async for msg in ws:` to talk.
    """
    # If you need the path:
    #   path = ws.request.path

    async for message in ws:
        try:
            data = json.loads(message)
            query = data.get("query", "").strip()
            if not query:
                await ws.send(json.dumps({"error": "Empty query"}))
                continue

            state = run_pipeline(query)
            await ws.send(state.json())
        except Exception as e:
            await ws.send(json.dumps({"error": str(e)}))


def start(host: str | None = None, port: int | None = None) -> None:
    """
    Start the WebSocket server by:
      1) Creating a new event loop for this thread
      2) Scheduling the serve() call as a task
      3) Running the loop forever
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    async def _serve() -> None:
        # Now serve() is awaited inside a truly running loop
        server = await websockets.serve(
            ws_handler,
            host or cfg.socket_host,
            port or cfg.socket_port,
        )
        print(f"WebSocket server listening on ws://{cfg.socket_host}:{cfg.socket_port}")
        # The server stays alive until loop.stop() is called
        await server.wait_closed()

    # Schedule the server startup as soon as the loop runs
    loop.create_task(_serve())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print("\nShutting down WebSocket server")
    finally:
        # Stop accepting new tasks and clean up
        loop.stop()
        loop.close()
        sys.exit(0)


if __name__ == "__main__":
    start()
