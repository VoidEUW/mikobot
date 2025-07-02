"""Mikotools (c) 2024-2025 by Void

Author: VoidEUW
"""

from . import (
    on_automod,
    on_client,
    on_entitlement,
    on_guild,
    on_integration,
    on_interaction,
    on_invite,
    on_member,
    on_message,
    on_poll,
    on_presence,
    on_private_channel,
    on_raw,
    on_reaction,
    on_scheduled_event,
    on_soundboard,
    on_stage,
    on_thread,
    on_user,
    on_voice,
)
from bot.miko import MikoBot


def event_listener(client: MikoBot) -> None:
    """Listen to events and handle them.

    events:
        - `on_client`
        - `on_message`
    """
    on_client.listen(client)
    on_message.listen(client)


"""
on_automod.listen(client)
on_client.listen(client)
on_entitlement.listen(client)
on_guild.listen(client)
on_integration.listen(client)
on_interaction.listen(client)
on_invite.listen(client)
on_member.listen(client)
on_message.listen(client)
on_poll.listen(client)
on_presence.listen(client)
on_private_channel.listen(client)
on_raw.listen(client)
on_reaction.listen(client)
on_scheduled_event.listen(client)
on_soundboard.listen(client)
on_stage.listen(client)
on_thread.listen(client)
on_user.listen(client)
on_voice.listen(client)
"""
