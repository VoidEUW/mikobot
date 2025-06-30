"""MikoBot (c) 2024-2025 by Void"""

import asyncio

import discord

from bot.api.post_log import log, LogType
from bot.miko import MikoBot
from bot.utils.event_utils.on_client import load_extensions


def listen(client: MikoBot) -> None:
    """Listen for events on the client."""

    @client.event
    async def on_connect() -> None:  # type: ignore
        log("Bot has connected to Discord")

    @client.event
    async def on_disconnect() -> None:  # type: ignore
        log("Bot has been disconnected. Attempting reconnect...", LogType.WARNING)
        await asyncio.sleep(10)

    @client.event
    async def on_ready() -> None:  # type: ignore
        await client.change_presence(
            status=discord.Status.do_not_disturb,
            activity=discord.Activity(type=discord.ActivityType.listening, name="Void"),
        )
        await load_extensions(client)

    @client.event
    async def on_resumed() -> None:  # type: ignore
        log("Successfully resumed session")

    # @client.event
    # async def on_error(event, *args, **kwargs) -> None: #type: ignore
    #    post_log(f"An error occurred: {event}, {args}, {kwargs}")

    @client.event
    async def on_interaction(interaction: discord.Interaction) -> None:  # type: ignore
        if interaction.type == discord.InteractionType.application_command:
            log(
                f"'{interaction.guild}': Slash Command '{interaction.data['name']}' was executed by {interaction.user} in #{interaction.channel}."  # type: ignore
            )
        elif interaction.type == discord.InteractionType.component:
            log("Component interaction received")
        elif interaction.type == discord.InteractionType.modal_submit:
            log("Modal interaction received")
