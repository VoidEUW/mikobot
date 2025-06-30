"""MikoBot (c) 2024-2025 by Void"""

import discord
import datetime

from bot.api.post_log import log
from bot.miko import MikoBot
from bot.interactions import interaction_handler
from bot.utils.event_utils import on_message as on_message_utils


def listen(client: MikoBot) -> None:
    """Listen for events on the client."""

    @client.event
    async def on_typing(  # type: ignore
        channel: discord.abc.Messageable, user: discord.User, when: datetime.datetime
    ) -> None:
        log(f"'{user.display_name}'({user.name}) is typing in '{channel}'")

    @client.event
    async def on_message(message: discord.Message) -> None:  # type: ignore
        if message.author.bot:
            return
        log(
            f"'{message.author.display_name}'({message.author.global_name}) in '{message.channel}': '{message.content}' "
        )
        if on_message_utils.check_message_content(message):
            await interaction_handler.trigger(client, message)
        else:
            await message.delete()

    @client.event
    async def on_message_delete(message: discord.Message) -> None:  # type: ignore
        log(
            f"'{message.author.display_name}'({message.author.global_name}) in '{message.channel}': deleted '{message.content}'"
        )

    @client.event
    async def on_message_edit(  # type: ignore
        before: discord.Message, after: discord.Message
    ) -> None:
        log(
            f"'{before.author.display_name}'({before.author.global_name}) in '{before.channel}': {before.content} edited to {after.content}"
        )
