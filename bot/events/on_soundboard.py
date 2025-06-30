"""MikoBot (c) 2024-2025 by Void"""

import discord

from bot.api.post_log import log
from bot.miko import MikoBot


def listen(client: MikoBot) -> None:
    """Listen for events on the client."""

    @client.event
    async def on_soundboard_sound_create(sound: discord.SoundboardSound) -> None:  # type: ignore
        log(f"Sound {sound} was created")

    @client.event
    async def on_soundboard_sound_delete(sound: discord.SoundboardSound) -> None:  # type: ignore
        log(f"Sound {sound} was deleted")

    @client.event
    async def on_soundboard_sound_update(  # type: ignore
        before: discord.SoundboardSound, after: discord.SoundboardSound
    ) -> None:
        log(f"Sound {before} was updated to {after}")
