"""Mikotools (c) 2024-2025 by Void"""

from flask import Blueprint, redirect, url_for, session, render_template

from config import API_TOKEN
from database.connection import connect_database

pages_dashboard_bp = Blueprint("pages_dashboard", __name__)

@pages_dashboard_bp.route("/dashboard")
def dashboard():
    """Dashboard page"""
    if "username" not in session:
        return redirect(url_for("pages_auth.login_page"))

    db = connect_database()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (session["username"],))
    user_data = cursor.fetchone()
    db.close()

    return render_template(
        "dashboard.html.jinja",
        user=user_data,
        logs=get_logs(),
        token=API_TOKEN
    )
    
def get_logs():
    """Fetch logs from the database"""
    db = connect_database()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM logs ORDER BY created DESC")
    logs = cursor.fetchmany(10)
    db.close()
    return logs

@pages_dashboard_bp.route("/dashboard/users")
def dashboard_users():
    """Users management page"""
    if "username" not in session:
        return redirect(url_for("pages_auth.login_page"))

    db = connect_database()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    db.close()
    
    db = connect_database()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (session["username"],))
    user_data = cursor.fetchone()
    db.close()

    return render_template(
        "dashboard.users.html.jinja", 
        user=user_data, 
        users=users
    )

@pages_dashboard_bp.route("/dashboard/tokens")
def dashboard_tokens():
    """Tokens management page"""
    if "username" not in session:
        return redirect(url_for("pages_auth.login_page"))

    db = connect_database()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tokens")
    tokens = cursor.fetchall()
    db.close()

    db = connect_database()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (session["username"],))
    user_data = cursor.fetchone()
    db.close()

    return render_template(
        "dashboard.tokens.html.jinja", 
        user=user_data, 
        tokens=tokens
    )