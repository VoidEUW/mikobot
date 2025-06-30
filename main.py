"""Mikotools Bot (c) 2024-2025 by Void"""

import os

from flask_cors import CORS
from waitress import serve

from config import HOST, PORT, DEBUG 
from extensions import socket
from init import create_app
from init import create_database
from init import cleanup
from init import first_setup

app = create_app()
socket.init_app(app, cors_allowed_origins="*")  # type: ignore
CORS(app)


if __name__ == "__main__":
    cleanup()
    create_database()
    if os.getenv("FIRST_SETUP", "false") == "true":
        print("INFO - Running first setup...")
        username, password = first_setup()
        print(f"INFO - Setup completed:   Username: {username} Password: {password}")
        os.environ["FIRST_SETUP"] = "false"
    print(f"INFO - Running on {HOST}:{PORT} in {os.getenv('DEPLOYMENT', 'development')} mode")
    if os.getenv("DEPLOYMENT", "development") == "production":
        serve(app, host=HOST, port=PORT, debug=DEBUG)  # type: ignore
    else:
        socket.run(app=app, host=HOST, port=PORT, debug=DEBUG)  # type: ignore