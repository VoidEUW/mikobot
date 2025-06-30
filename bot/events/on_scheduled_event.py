"""MikoBot (c) 2024-2025 by Void"""

import discord

from bot.api.post_log import log
from bot.miko import MikoBot


def listen(client: MikoBot) -> None:
    """Listen for events on the client."""

    @client.event
    async def on_scheduled_event_create(event: discord.ScheduledEvent) -> None:  # type: ignore
        log(f"Scheduled event {event} was created")

    @client.event
    async def on_scheduled_event_delete(event: discord.ScheduledEvent) -> None:  # type: ignore
        log(f"Scheduled event {event} was deleted")

    @client.event
    async def on_scheduled_event_update(  # type: ignore
        before: discord.ScheduledEvent, after: discord.ScheduledEvent
    ) -> None:
        log(f"Scheduled event {before} was updated to {after}")

    @client.event
    async def on_scheduled_event_user_add(  # type: ignore
        event: discord.ScheduledEvent, user: discord.User
    ) -> None:
        log(f"User {user} was added to scheduled event {event}")

    @client.event
    async def on_scheduled_event_user_remove(  # type: ignore
        event: discord.ScheduledEvent, user: discord.User
    ) -> None:
        log(f"User {user} was removed from scheduled event {event}")
