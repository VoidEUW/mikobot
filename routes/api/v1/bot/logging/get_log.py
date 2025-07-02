"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

from flask import Response, jsonify

from database.connection import connect_database


def handle_get_log() -> Response:
    """Get the log."""

    db = connect_database()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM logs ORDER BY created DESC LIMIT 10")
    log_entries = cursor.fetchall()

    return jsonify(
        {
            "message": "Log retrieved successfully.",
            "entries": [dict(entry) for entry in log_entries],
        }
    )
