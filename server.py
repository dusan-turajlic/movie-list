from os import getenv

from uvicorn import run

STAGE = getenv("STAGE")
DEFAULT_HOST = "0.0.0.0"

server_args = {}

if STAGE == "development":
    server_args = {
        "reload": True
    }
else:
    server_args = {
        "port": 80,
        "proxy_headers": True
    }

if __name__ == "__main__":
    run("app.main:app", host=DEFAULT_HOST, **server_args)
