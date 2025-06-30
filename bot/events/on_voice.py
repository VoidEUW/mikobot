"""MikoBot (c) 2024-2025 by Void"""

import discord

from bot.api.post_log import log
from bot.miko import MikoBot


def listen(client: MikoBot) -> None:
    """Listen for events on the client."""

    @client.event
    async def on_voice_state_update(  # type: ignore
        member: discord.Member, before: discord.VoiceState, after: discord.VoiceState
    ) -> None:
        log(f"Voice state of {member} was updated from {before} to {after}")

    @client.event
    async def on_voice_channel_create(channel: discord.VoiceChannel) -> None:  # type: ignore
        log(f"Voice channel {channel} was created")
