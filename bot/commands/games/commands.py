"""MikoBot (c) 2024-2025 by Void"""

import discord
from discord import app_commands
from discord.ext import commands

from bot.commands.games import lets_play
from bot.commands.config import GAME_CHOICES, MODE_CHOICES


class ClientCommandGroup(app_commands.Group):
    @app_commands.command(name="lets_play", description="DESCRIPTION")
    @app_commands.choices(game=GAME_CHOICES)
    @app_commands.choices(mode=MODE_CHOICES)
    @app_commands.describe(game="DESCRIPTION", player_count="DESCRIPTION")
    async def command_lets_play(
        self,
        interaction: discord.Interaction,
        game: app_commands.Choice[str],
        mode: app_commands.Choice[str],
        player_count: int,
    ) -> None:
        await lets_play.initialize(interaction, game, mode, player_count)


async def setup(bot: commands.Bot):
    bot.tree.add_command(ClientCommandGroup(name="games", description="DESCRIPTION"))
