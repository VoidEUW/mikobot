"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

import discord

from bot.api.post_log import log
from bot.miko import MikoBot


def listen(client: MikoBot) -> None:  # type: ignore
    """Listen for events on the client."""

    @client.event
    async def on_entitlement_create(entitlement: discord.Entitlement) -> None:  # type: ignore
        log(f"Entitlement {entitlement} was created")

    @client.event
    async def on_entitlement_delete(entitlement: discord.Entitlement) -> None:  # type: ignore
        log(f"Entitlement {entitlement} was deleted")

    @client.event
    async def on_entitlement_update(  # type: ignore
        before: discord.Entitlement, after: discord.Entitlement
    ) -> None:
        log(f"Entitlement {before} was updated to {after}")
