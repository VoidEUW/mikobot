"""MikoBot (c) 2024-2025 by Void"""

import discord

from bot.api.post_log import log
from bot.miko import MikoBot


def listen(client: MikoBot) -> None:
    """Listen for events on the client."""

    @client.event
    async def on_invite_create(invite: discord.Invite) -> None:  # type: ignore
        log(f"Invite {invite} was created")

    @client.event
    async def on_invite_delete(invite: discord.Invite) -> None:  # type: ignore
        log(f"Invite {invite} was deleted")
