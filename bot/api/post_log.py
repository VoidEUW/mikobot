"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

from enum import Enum
import requests

from config import API_SLUG, API_URL, API_TOKEN

class LogType(Enum):
    """Log types for the API."""

    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    DEBUG = "DEBUG"


def log(message: str, log_type: LogType = LogType.INFO) -> None:
    """Send a log to the API."""
    requests.post(
        f"{API_URL}{API_SLUG}/bot/logging",
        json={"type": log_type.value, "message": message},
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_TOKEN}",
        },
    )
