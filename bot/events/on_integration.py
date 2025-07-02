"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

import discord

from bot.api.post_log import log
from bot.miko import MikoBot


def listen(client: MikoBot) -> None:
    """Listen for events on the client."""

    @client.event
    async def on_integration_create(integration: discord.Integration) -> None:  # type: ignore
        log(f"Integration {integration} was created")

    @client.event
    async def on_integration_delete(integration: discord.Integration) -> None:  # type: ignore
        log(f"Integration {integration} was deleted")

    @client.event
    async def on_integration_update(  # type: ignore
        before: discord.Integration, after: discord.Integration
    ) -> None:
        log(f"Integration {before} was updated to {after}")
