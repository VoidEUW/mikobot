"""MikoBot (c) 2024-2025 by Void"""

import discord


def check_message_content(message: discord.Message) -> bool:
    """Check the content of a message."""
    if check_blacklisted_links(message):
        return False
    return True


def check_blacklisted_links(message: discord.Message) -> bool:
    """Check if the message contains blacklisted links."""
    # TODO: Request links from the database
    blacklisted_links: list[str] = [
        "https://discord.gg/",
    ]
    for link in blacklisted_links:
        if link in message.content:
            return True
    return False
