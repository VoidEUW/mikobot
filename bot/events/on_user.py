"""MikoBot (c) 2024-2025 by Void"""

import discord

from bot.api.post_log import log
from bot.miko import MikoBot


def listen(client: MikoBot) -> None:
    """Listen for events on the client."""

    @client.event
    async def on_user_update(  # type: ignore
        before: discord.User, after: discord.User
    ) -> None:
        log(f"User {before} was updated to {after}")
