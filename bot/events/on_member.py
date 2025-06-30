"""MikoBot (c) 2024-2025 by Void"""

import discord

from bot.api.post_log import log
from bot.miko import MikoBot


def listen(client: MikoBot) -> None:
    """Listen for events on the client."""

    @client.event
    async def on_member_join(member: discord.Member) -> None:  # type: ignore
        log(f"Member {member} joined the server")

    @client.event
    async def on_member_remove(member: discord.Member) -> None:  # type: ignore
        log(f"Member {member} left the server")

    @client.event
    async def on_member_update(before: discord.Member, after: discord.Member) -> None:  # type: ignore
        log(f"Member {before} was updated to {after}")

    @client.event
    async def on_member_ban(guild: discord.Guild, user: discord.User) -> None:  # type: ignore
        log(f"Member {user} was banned from {guild}")

    @client.event
    async def on_member_unban(guild: discord.Guild, user: discord.User) -> None:  # type: ignore
        log(f"Member {user} was unbanned from {guild}")
