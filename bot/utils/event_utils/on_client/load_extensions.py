"""MikoBot (c) 2024-2025 by Void"""

from bot.miko import MikoBot
from bot.api.post_log import log, LogType


async def load_extensions(client: MikoBot) -> None:
    try:
        for command_group in client.command_groups:
            try:
                await client.load_extension(f"bot.commands.{command_group}.commands")
                log(f"Loading group: '{command_group}'", LogType.DEBUG)
            except Exception as err:
                log(f"Failed to load group: '{command_group}: {err}'", LogType.ERROR)
    except Exception as err:
        log(f"Extensions couldn't be loaded: {err}", LogType.ERROR)
    log(f"Logged in as '{client.user}' (ID: {client.user.id})")  # type: ignore
    log(f"Connected to {len(client.guilds)} guild(s)")
    try:
        await client.tree.sync()
    except Exception as err:
        log(f"Failed to sync tree: {err}", LogType.ERROR)
