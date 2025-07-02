"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

from discord import app_commands


GAME_CHOICES = [
    app_commands.Choice(name="League of Legends", value="league_of_legends"),
    app_commands.Choice(name="Valorant", value="valorant"),
    app_commands.Choice(name="Rocket League", value="rocket_league"),
    app_commands.Choice(name="Minecraft", value="minecraft"),
]

MODE_CHOICES = [
    app_commands.Choice(name="Custom Game", value="Custom Game"),
    app_commands.Choice(name="Ranked", value="Ranked Game"),
    app_commands.Choice(name="Normal Game", value="Normal Game"),
    app_commands.Choice(name="Other", value="Other"),
]
