"""MikoBot (c) 2024-2025 by Void"""

import requests

from config import API_SLUG, API_URL, API_TOKEN


def get_games() -> list[tuple[str, str, str]]:
    response = requests.get(
        f"{API_URL}{API_SLUG}/bot/commands/games",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_TOKEN}",
        },
    )
    if response.status_code == 200:
        return response.json()
    return []
