"""MikoBot (c) 2024-2025 by Void"""

import discord

from bot.api.post_log import log
from bot.miko import MikoBot


def listen(client: MikoBot) -> None:
    """Listen for events on the client."""

    @client.event
    async def on_private_channel_pins_update(  # type: ignore
        channel: discord.abc.PrivateChannel, last_pin: discord.Message
    ) -> None:
        log(f"Private channel {channel} pins were updated to {last_pin}")

    @client.event
    async def on_private_channel_update(  # type: ignore
        before: discord.abc.PrivateChannel, after: discord.abc.PrivateChannel
    ) -> None:
        log(f"Private channel {before} was updated to {after}")
