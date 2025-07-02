"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

from flask import Blueprint, request, render_template, redirect, url_for, session

from database.connection import connect_database

pages_auth_bp = Blueprint("pages_auth", __name__)

@pages_auth_bp.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        
        if not username or not password:
            return render_template("login.html.jinja", error="Username and password are required")
        
        db = connect_database()
        cursor = db.cursor()
        cursor.execute(
            "SELECT username, password FROM users WHERE username = ?", (username,)
        )
        result = cursor.fetchone()
        db.close()
        
        if result is None:
            return render_template("login.html.jinja", error="Invalid credentials")
        if result["password"] == password:
            session["username"] = username
            return redirect(url_for("pages_dashboard.dashboard"))
    return render_template("login.html.jinja")


@pages_auth_bp.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("pages_auth.login_page"))