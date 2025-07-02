"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

from flask import Blueprint, redirect, url_for, session

pages_bp = Blueprint("pages", __name__)

@pages_bp.route("/")
def index():
    """Index page"""
    if "username" in session:
        return redirect(url_for("pages_dashboard.dashboard"))
    return redirect(url_for("pages_auth.login_page"))