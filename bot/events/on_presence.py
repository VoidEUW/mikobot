"""MikoBot (c) 2024-2025 by Void"""

import discord

from bot.api.post_log import log
from bot.miko import MikoBot


def listen(client: MikoBot) -> None:
    """Listen for events on the client."""

    @client.event
    async def on_presence_update(before: discord.Member, after: discord.Member) -> None:  # type: ignore
        log(f"Presence {before} was updated to {after}")
