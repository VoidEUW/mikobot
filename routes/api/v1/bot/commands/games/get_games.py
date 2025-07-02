"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

from flask import Response, jsonify

from database.connection import connect_database


def handle_get_games() -> Response:
    """Handle GET request for games."""
    with connect_database() as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM games")
        games = cursor.fetchall()
        games = [dict(game) for game in games]
    return jsonify({"games": games})
