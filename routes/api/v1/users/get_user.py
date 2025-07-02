"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

import os
import json
import sqlite3

from flask import send_file, jsonify, Response

from database.connection import connect_database


def handle_get_user(username: str) -> Response:
    """Handle get user request"""

    db: sqlite3.Connection = connect_database()

    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    db.close()

    if user:
        return jsonify(
            {
                "status": "success",
                "data": dict(user),  # type: ignore
            }
        )
    return jsonify({"status": "failed", "data": None})


def handle_get_user_avatar(username: str) -> dict[str, str]:
    """Handle get user avatar request"""
    user_data = get_user_data(username)
    for user in user_data:
        if user["username"] == username:
            # FIXME: This is a temporary fix
            avatar_path = os.path.abspath(
                f"{os.path.dirname(__file__).rsplit('/', 3)[0]}/api/assets/{username}.jpg"
            )  # type: ignore
            print(avatar_path)
            if avatar_path and os.path.exists(avatar_path):
                return send_file(avatar_path, mimetype="image/jpg")  # type: ignore
            else:
                return {"status": "error", "message": "Avatar not found"}
    return {"status": "error", "message": "User not found"}


def get_user_data(username: str) -> list[dict[str, str]]:
    """Get user data from the database"""
    with open("api/users.json", "r") as f:
        users_data = json.load(f)
    return users_data
