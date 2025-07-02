"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

import sqlite3

from flask import Flask

from config import USERNAME, PASSWORD, EMAIL, SECRET_KEY, PATH_DATABASE

from routes.api.v1.bot.status.blueprint import status_bp
from routes.api.v1.users.blueprint import users_bp
from routes.pages.blueprint import pages_bp
from routes.pages.auth.blueprint import pages_auth_bp
from routes.pages.dashboard.blueprint import pages_dashboard_bp
from routes.api.v1.bot.logging.blueprint import logging_bp
from routes.api.v1.bot.commands.games.blueprint import games_bp

def create_app() -> Flask:
    """Create the Flask app and register the blueprints."""
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    
    # API v1
    # PAGES
    app.register_blueprint(pages_bp)
    app.register_blueprint(pages_auth_bp)
    app.register_blueprint(pages_dashboard_bp)
    # API
    app.register_blueprint(users_bp)
    app.register_blueprint(status_bp)
    app.register_blueprint(logging_bp)
    app.register_blueprint(games_bp)
    return app


def cleanup():
    with open("api/bot.pid", "w") as f:
      f.write("")
      

def create_database():
    db = sqlite3.connect(PATH_DATABASE)
    
    with open('database/schema.sql') as f:
        db.executescript(f.read())
        
    db.commit()
    db.close()
    
def first_setup() -> tuple[str, str]:
    """Initial setup for the database."""
    db = sqlite3.connect(PATH_DATABASE)
    cursor = db.cursor()
    
    username = USERNAME
    password = PASSWORD
    email = EMAIL
    cursor.execute("""
        INSERT INTO users (username, email, password)
        VALUES (?, ?, ?)
    """, (username, email, password)
    )
    
    with open('database/data-setup.sql') as f:
        db.executescript(f.read())

    db.commit()
    db.close()

    return username, password