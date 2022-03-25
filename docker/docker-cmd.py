#!/usr/bin/env python

import os
import subprocess

STAGE = os.getenv("STAGE")
print(STAGE)
DEFAULT_HOST = "0.0.0.0"

startup_cmd = ["uvicorn", "app.main:app", "--host", DEFAULT_HOST]

if STAGE == "development":
    startup_cmd.append("--reload")
else:
    startup_cmd.append("--port")
    startup_cmd.append("80")
    startup_cmd.append("--proxy-headers")

print("starting server")
subprocess.call(startup_cmd)
