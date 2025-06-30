"""MikoBot (c) 2024-2025 by Void"""

import discord

from bot.miko import MikoBot


async def trigger(client: MikoBot, message: discord.Message) -> None:
    """Trigger an interaction based on the message."""
    # TODO: Implement interaction handling
    if message.content.startswith(client.user.mention):  # type: ignore
        await message.channel.send("Hello! How can I assist you today?")
