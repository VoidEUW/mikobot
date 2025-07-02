"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

from flask import Blueprint
from config import API_SLUG

from routes.api.v1.bot.logging import handle_get_log, handle_post_log
from routes.api.v1.auth.token_auth import token_auth


logging_bp = Blueprint("logging", __name__, url_prefix=f"{API_SLUG}/bot/logging")


@logging_bp.route("/", methods=["GET"])
@token_auth.login_required  # type: ignore
def get_log():
    """Get the log."""
    return handle_get_log()


@logging_bp.route("/", methods=["POST"])
@token_auth.login_required  # type: ignore
def post_log():
    """Post a log."""
    return handle_post_log()
