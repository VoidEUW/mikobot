from flask_httpauth import HTTPTokenAuth  # type: ignore

from database.connection import connect_database


token_auth = HTTPTokenAuth(scheme="Bearer")


@token_auth.verify_token  # type: ignore
def verify_token(token: str) -> str | None:
    db = connect_database()
    cursor = db.cursor()
    cursor.execute("SELECT token FROM tokens WHERE token = ?", (token,))
    result = cursor.fetchone()
    db.close()

    if result is None:
        return None

    return result["token"]
