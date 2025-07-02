"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

from flask import Blueprint
from config import API_SLUG

from routes.api.v1.bot.commands.games import handle_get_games
from routes.api.v1.auth.token_auth import token_auth


games_bp = Blueprint("games", __name__, url_prefix=f"{API_SLUG}/bot/commands/games")


@games_bp.route("", methods=["GET"])
@token_auth.login_required  # type: ignore
def get_games():
    """Get the games."""
    return handle_get_games()
