"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

import discord

from bot.api.post_log import log
from bot.miko import MikoBot


def listen(client: MikoBot) -> None:
    """Listen for events on the client."""

    @client.event
    async def on_reaction_add(  # type: ignore
        reaction: discord.Reaction, user: discord.User
    ) -> None:
        log(f"Reaction {reaction} was added by {user}")

    @client.event
    async def on_reaction_remove(  # type: ignore
        reaction: discord.Reaction, user: discord.User
    ) -> None:
        log(f"Reaction {reaction} was removed by {user}")

    @client.event
    async def on_reaction_clear(  # type: ignore
        message: discord.Message, reactions: discord.Reaction
    ) -> None:
        log(f"Reactions on {message} were cleared")

    @client.event
    async def on_reaction_clear_emoji(reaction: discord.Reaction) -> None:  # type: ignore
        log(f"Reactions on {reaction} were cleared")
