"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

import discord

from bot.api.post_log import log
from bot.miko import MikoBot


def listen(client: MikoBot) -> None:
    """Listen for events on the client."""

    discord.ChannelType

    @client.event
    async def on_guild_available(guild: discord.Guild) -> None:  # type: ignore
        log(f"Guild {guild} became available")

    @client.event
    async def on_guild_channel_create(channel: discord.abc.GuildChannel) -> None:  # type: ignore
        log(f"Channel {channel} was created in {channel.guild}")

    @client.event
    async def on_guild_channel_delete(channel: discord.abc.GuildChannel) -> None:  # type: ignore
        log(f"Channel {channel} was deleted in {channel.guild}")

    @client.event
    async def on_guild_channel_update(  # type: ignore
        before: discord.abc.GuildChannel, after: discord.abc.GuildChannel
    ) -> None:
        log(f"Channel {before} was updated to {after} in {before.guild}")

    @client.event
    async def on_guild_channel_pins_update(  # type: ignore
        channel: discord.abc.GuildChannel, last_pin: discord.Message
    ) -> None:
        log(f"Channel {channel} pins were updated to {last_pin} in {channel.guild}")

    @client.event
    async def on_guild_emojis_update(  # type: ignore
        guild: discord.Guild, before: discord.Emoji, after: discord.Emoji
    ) -> None:
        log(f"Guild {guild} emoji {before} was updated to {after}")

    @client.event
    async def on_guild_integrations_update(guild: discord.Guild) -> None:  # type: ignore
        log(f"Guild {guild} integrations were updated")

    @client.event
    async def on_guild_join(guild: discord.Guild) -> None:  # type: ignore
        log(f"Joined guild {guild}")

    @client.event
    async def on_guild_remove(guild: discord.Guild) -> None:  # type: ignore
        log(f"Left guild {guild}")

    @client.event
    async def on_guild_role_create(role: discord.Role) -> None:  # type: ignore
        log(f"Role {role} was created in {role.guild}")

    @client.event
    async def on_guild_role_delete(role: discord.Role) -> None:  # type: ignore
        log(f"Role {role} was deleted in {role.guild}")

    @client.event
    async def on_guild_role_update(  # type: ignore
        before: discord.Role, after: discord.Role
    ) -> None:
        log(f"Role {before} was updated to {after} in {before.guild}")

    @client.event
    async def on_guild_stickers_update(guild: discord.Guild) -> None:  # type: ignore
        log(f"Guild {guild} stickers were updated")

    @client.event
    async def on_guild_unavailable(guild: discord.Guild) -> None:  # type: ignore
        log(f"Guild {guild} became unavailable")

    @client.event
    async def on_guild_update(  # type: ignore
        before: discord.Guild, after: discord.Guild
    ) -> None:
        log(f"Guild {before} was updated to {after}")
