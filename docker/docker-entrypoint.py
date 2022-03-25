#!/usr/bin/env python

import os
import subprocess

STAGE = os.getenv("STAGE")
print(STAGE)
DEFAULT_HOST = "0.0.0.0"

startup_cmd = ["uvicorn", "app.main:app", "--host", DEFAULT_HOST]
pip_install_cmd = ["pip", "install", "-r", "requirements.txt"]

if STAGE == "development":
    startup_cmd.append("--reload")
else:
    startup_cmd.append("--port")
    startup_cmd.append("80")

print("installing dependencies")
subprocess.call(pip_install_cmd)
print("starting server")
subprocess.call(startup_cmd)
