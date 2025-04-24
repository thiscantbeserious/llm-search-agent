import sys
import threading
import time

import asyncio
import click
import requests

from llm_search_agent.config import Config
from llm_search_agent.runners import commandline, rest_api, websocket
from llm_search_agent.runners.websocket import is_alive

cfg = Config()


@click.group(invoke_without_command=True)
@click.pass_context
def run(ctx):
    """
    LLM Search Agent Runner—subcommands: cmd, api, ws, all.
    If no subcommand is given, it will default to 'all'.
    """
    if ctx.invoked_subcommand is None:
        # forward to the `all` handler
        ctx.invoke(all)


@run.command()
def cmd():
    """Start continuous CLI REPL."""
    commandline.start()


@run.command()
@click.option("--host", default=None, help="API host override")
@click.option("--port", default=None, type=int, help="API port override")
def api(host, port):
    """Start FastAPI HTTP server."""
    # allow overriding via CLI flags if desired
    rest_api.start(host, port)


@run.command()
@click.option("--host", default=None, help="WS host override")
@click.option("--port", default=None, type=int, help="WS port override")
def ws(host, port):
    """Start WebSocket server."""
    websocket.start(host, port)


def wait_for_api(host: str, port: int, timeout: float = 10.0) -> bool:
    url = f"http://{host}:{port}/health"
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            r = requests.get(url, timeout=2)
            if r.status_code == 200 and r.json().get("status") == "ok":
                return True
        except requests.RequestException:
            pass
        time.sleep(0.1)
    return False


def wait_for_ws(host: str, port: int, timeout: float = 10.0) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        if asyncio.run(is_alive(host, port)):
            return True
        time.sleep(0.25)
    return False


@run.command()
@click.option("--api-host", default=None, help="API host override")
@click.option("--api-port", default=None, type=int, help="API port override")
@click.option("--ws-host", default=None, help="WS host override")
@click.option("--ws-port", default=None, type=int, help="WS port override")
def all(api_host, api_port, ws_host, ws_port):
    """
    Launch API and WS in background threads, then start the CLI REPL
    on the main thread.
    """

    api_host = api_host or cfg.api_host
    api_port = api_port or cfg.api_port
    ws_host = ws_host or cfg.socket_host
    ws_port = ws_port or cfg.socket_port

    # 1) Start API server in daemon thread
    t_api = threading.Thread(
        target=lambda: rest_api.start(api_host, api_port, reload=False),
        daemon=True
    )
    t_api.start()

    # 2) Start WebSocket server in daemon thread
    t_ws = threading.Thread(
        target=lambda: websocket.start(ws_host, ws_port),
        daemon=True
    )
    t_ws.start()

    # 4) Wait for readiness
    click.echo(f"⏳ Waiting for HTTP API at {api_host}:{api_port} …")
    if wait_for_api(api_host, api_port):
        click.echo(f"✅ HTTP API is up on {api_host}:{api_port}")
    else:
        click.echo(f"❌ Timeout waiting for HTTP API on {api_host}:{api_port}", err=True)

    click.echo(f"⏳ Waiting for WebSocket at {ws_host}:{ws_port} …")
    if wait_for_ws(ws_host, ws_port):
        click.echo(f"✅ WebSocket is up on {ws_host}:{ws_port}")
    else:
        click.echo(f"❌ Timeout waiting for WebSocket on {ws_host}:{ws_port}", err=True)

    click.echo("🚀 All services ready. Starting CLI REPL now.")
    # 5) Run REPL in main thread
    try:
        commandline.start()
    except (KeyboardInterrupt, EOFError):
        click.echo("\n🛑 Shutting down.")
        sys.exit(0)


if __name__ == "__main__":
    run()
