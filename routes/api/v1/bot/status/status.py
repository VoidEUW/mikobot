from flask import Response, jsonify


def handle_status() -> Response:  # type: ignore
    """Handle the stop command"""
    with open("api/bot.pid") as f:
        pid = f.read()
    if pid != "":
        return jsonify({"status": "RUNNING", "pid": pid})
    else:
        return jsonify({"status": "NOT_RUNNING", "pid": None})
