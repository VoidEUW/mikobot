"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

from flask import Blueprint
from config import API_SLUG

from routes.api.v1.auth.basic_auth import basic_auth
from routes.api.v1.users import (
    handle_get_user,
    # handle_get_user_avatar,
)

users_bp = Blueprint("users", __name__, url_prefix=f"{API_SLUG}/users")


@users_bp.route("/<string:username>")
@basic_auth.login_required  # type: ignore
def get_user(username: str):
    """Get user route"""
    return handle_get_user(username)


@users_bp.route("/<string:username>/avatar", methods=["GET"])
@basic_auth.login_required  # type: ignore
def get_user_avatar(username: str):
    """Get user avatar route"""
    # return handle_get_user_avatar(username)
    return {"status": "error", "message": "Avatar not found"}
