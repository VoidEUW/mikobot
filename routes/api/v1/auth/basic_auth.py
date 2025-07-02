"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

from flask_httpauth import HTTPBasicAuth  # type: ignore

from database.connection import connect_database


basic_auth = HTTPBasicAuth()


@basic_auth.verify_password  # type: ignore
def verify_password(username: str, password: str) -> str | None:
    db = connect_database()
    cursor = db.cursor()
    cursor.execute(
        "SELECT username, password FROM users WHERE username = ?", (username,)
    )
    result = cursor.fetchone()
    db.close()

    if result is None:
        return None

    if result["password"] == password:
        return username
