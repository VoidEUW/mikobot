"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

import discord
from discord.ext import commands


class MikoBot(commands.Bot):
    """MikoBot class

    MikoBot is a subclass of discord.ext.commands.Bot that
    initializes the bot with a command prefix and intents.
    It is used to give the bot more functionality.
    """

    command_groups: list[str] = ["client", "games"]

    def __init__(self):
        """MikoBot subclass

        MikoBot is a subclass of discord.ext.commands.Bot that
        initializes the bot with a command prefix and intents.
        """
        super().__init__(command_prefix="!", intents=discord.Intents.all())
