"""MikoBot (c) 2024-2025 by Void"""

import discord

from bot.api.post_log import log
from bot.miko import MikoBot


def listen(client: MikoBot):
    """Listen for events on the client."""

    @client.event
    async def on_automod_action(action: discord.AutoModAction):  # type: ignore
        log(f"Automod Action {action} was created")

    @client.event
    async def on_automod_rule_create(rule: discord.AutoModRule):  # type: ignore
        log(f"Automod Rule {rule} was created")

    @client.event
    async def on_automod_rule_update(  # type: ignore
        before: discord.AutoModRule, after: discord.AutoModRule
    ):
        log(f"Automod Rule {before} was updated to {after}")
