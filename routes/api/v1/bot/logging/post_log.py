"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

from flask import Response, request, jsonify

from datetime import datetime

from database.connection import connect_database
from extensions import socket

def handle_post_log() -> Response:
    """Post a log."""

    data = request.json
    if not data or "type" not in data or "message" not in data:
        return jsonify({"error": "Invalid request."})
    log_type: str = data["type"]
    message: str = data["message"]

    with connect_database() as db:
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO logs (type, message) VALUES (?, ?)",
            (log_type, message),
        )
        db.commit()
        cursor.close()
        
    socket.emit('terminal_output', {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'type': log_type, 'message': message}) # type: ignore
    return jsonify({"message": "OK"})
