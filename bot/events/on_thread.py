"""MikoBot (c) 2024-2025 by Void"""

import discord

from bot.api.post_log import log
from bot.miko import MikoBot


def listen(client: MikoBot) -> None:
    """Listen for events on the client."""

    @client.event
    async def on_thread_create(thread: discord.Thread) -> None:  # type: ignore
        log(f"Thread {thread} was created")

    @client.event
    async def on_thread_delete(thread: discord.Thread) -> None:  # type: ignore
        log(f"Thread {thread} was deleted")

    @client.event
    async def on_thread_update(  # type: ignore
        before: discord.Thread, after: discord.Thread
    ) -> None:
        log(f"Thread {before} was updated to {after}")

    @client.event
    async def on_thread_member_join(member: discord.ThreadMember) -> None:  # type: ignore
        log(f"Member {member} joined thread {member.thread}")

    @client.event
    async def on_thread_member_leave(member: discord.ThreadMember) -> None:  # type: ignore
        log(f"Member {member} left thread {member.thread}")

    @client.event
    async def on_thread_join(thread: discord.Thread) -> None:  # type: ignore
        log(f"Thread {thread} was joined")

    @client.event
    async def on_thread_remove(member: discord.ThreadMember) -> None:  # type: ignore
        log(f"Member {member} was removed from thread {member.thread}")
