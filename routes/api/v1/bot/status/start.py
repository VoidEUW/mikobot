"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

import subprocess
import threading
from datetime import datetime

from config import BOT_TOKEN, API_TOKEN, PORT

from extensions import socket

from flask import Response, jsonify

# FIXME: bot can run 2 times!
def handle_start(
    bot_process: subprocess.Popen | None, lock: threading.Lock # type: ignore
) -> Response:
    """Handle the start command"""
    with lock:
        if (bot_process is None) or (bot_process.poll() is not None):
            bot_process = subprocess.Popen(["poetry", "run", "python", "-m", "bot", BOT_TOKEN, API_TOKEN, str(PORT)])
            with open("api/bot.pid", "w") as f:
                f.write(str(bot_process.pid))
            socket.emit("terminal_output", { # type: ignore
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "type": "info",
                "message": f"Bot started with PID {bot_process.pid}"
            })
            return jsonify({"status": "STARTING", "pid": bot_process.pid})
        else:
            socket.emit("terminal_output", { # type: ignore
                "type": "warn",
                "message": f"Bot already running (PID {bot_process.pid})"
            })
            return jsonify({"status": "ALREADY_RUNNING", "pid": bot_process.pid})