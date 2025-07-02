"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

import os
from datetime import datetime

from extensions import socket
from flask import Response, jsonify


def handle_stop() -> Response:  # type: ignore
    """Handle the stop command"""
    try:
        with open("api/bot.pid", "r") as f:
            pid = int(f.read())
        os.kill(pid, 0)
        with open("api/bot.pid", "w") as f:
            f.write("")
        socket.emit("terminal_output", { # type: ignore
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": "INFO",
            "message": f"Bot stopped with PID {pid}"
        })
        return jsonify({"status": "STOPPING", "pid": pid})
    except Exception:
        socket.emit("terminal_output", { # type: ignore
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": "WARNING",
            "message": f"Bot is not running! No PID found."
        })
        return jsonify({"status": "NOT_RUNNING", "pid": None})
