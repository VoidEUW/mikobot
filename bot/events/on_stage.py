"""MikoBot (c) 2024-2025 by Void"""

import discord

from bot.api.post_log import log
from bot.miko import MikoBot


def listen(client: MikoBot) -> None:
    """Listen for events on the client."""

    @client.event
    async def on_stage_instance_create(stage_instance: discord.StageInstance) -> None:  # type: ignore
        log(f"Stage instance {stage_instance} was created")

    @client.event
    async def on_stage_instance_delete(stage_instance: discord.StageInstance) -> None:  # type: ignore
        log(f"Stage instance {stage_instance} was deleted")

    @client.event
    async def on_stage_instance_update(  # type: ignore
        before: discord.StageInstance, after: discord.StageInstance
    ) -> None:
        log(f"Stage instance {before} was updated to {after}")
