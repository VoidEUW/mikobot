"""MikoBot (c) 2024-2025 by Void"""

import discord
from discord import app_commands
from discord.ext import commands


class ClientCommandGroup(app_commands.Group):
    @app_commands.command(name="ping", description="DESCRIPTION")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"Pong! {round(interaction.client.latency * 1000)}ms"
        )


async def setup(bot: commands.Bot):
    bot.tree.add_command(ClientCommandGroup(name="client", description="DESCRIPTION"))
