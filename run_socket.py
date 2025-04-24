import asyncio
import json
import websockets

from llm_search_agent.config import Config
from llm_search_agent.orchestrator import run_pipeline

cfg = Config()


async def handler(ws):
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


async def runner():
    server = await websockets.serve(
        handler,
        cfg.socket_host,
        cfg.socket_port,
    )
    print(f"WebSocket server listening on ws://{cfg.socket_host}:{cfg.socket_port}")
    # Run until cancelled
    await server.wait_closed()


def main():
    try:
        asyncio.run(runner())
    except KeyboardInterrupt:
        print("Shutting down WebSocket server")


if __name__ == "__main__":
    main()
