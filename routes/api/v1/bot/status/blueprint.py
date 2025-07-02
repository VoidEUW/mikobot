"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

import threading

from flask import Blueprint
from config import API_SLUG

from routes.api.v1.bot.status import (
    handle_start,  # type: ignore
    handle_stop,
    handle_status,
)
from routes.api.v1.auth.basic_auth import basic_auth

status_bp = Blueprint("status", __name__, url_prefix=f"{API_SLUG}/bot/status")

bot_process = None  # type: ignore
lock = threading.Lock()


@status_bp.route("/", methods=["GET"])
@basic_auth.login_required  # type: ignore
def status():
    """Status route"""
    return handle_status()


@status_bp.route("/start", methods=["GET"])
@basic_auth.login_required  # type: ignore
def start():
    """Start route"""
    global bot_process
    return handle_start(bot_process, lock)


@status_bp.route("/stop", methods=["GET"])
@basic_auth.login_required  # type: ignore
def stop():
    """Stop route"""
    return handle_stop()
