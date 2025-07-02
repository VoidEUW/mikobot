"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

import discord

from bot.api.post_log import log
from bot.miko import MikoBot


def listen(client: MikoBot) -> None:
    """Listen for events on the client."""

    @client.event
    async def on_interaction(interaction: discord.Interaction) -> None:  # type: ignore
        log(f"Interaction {interaction}")
