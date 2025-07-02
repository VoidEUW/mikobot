"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

import discord

from bot.api.post_log import log
from bot.miko import MikoBot


def listen(client: MikoBot) -> None:
    """Listen for events on the client."""

    @client.event
    async def on_poll_vote_add(user: discord.User, answer: discord.PollAnswer) -> None:  # type: ignore
        log(f"Poll vote {answer} was added by {user}")

    @client.event
    async def on_poll_vote_remove(  # type: ignore
        user: discord.User, answer: discord.PollAnswer
    ) -> None:
        log(f"Poll vote {answer} was removed by {user}")
