"""MikoBot (c) 2024-2025 by Void"""

from enum import Enum

import discord
from discord import app_commands

from bot.api.get_games import get_games


class Status(Enum):
    JOINED = "Joined"
    DECLINED = "Declined"
    NOT_SURE = "Not sure"


class MikoLetsPlayView(discord.ui.View):
    
    def __init__(self, timeout: int | None = 180) -> None:
        super().__init__(timeout=timeout)
        self.initiator: discord.Member = None  # type: ignore
        self.message: discord.Message = None  # type: ignore
        self.status_list = [Status.JOINED, Status.DECLINED, Status.NOT_SURE]
        self.all_players: list[tuple[discord.Member | discord.User, Status]] = []
        self.game_data: dict[str, str] = {}
        self.max_players: int = 0
        self.game_value: str = ""
        self.mode_value: str = ""

    async def send_message(self, interaction: discord.Interaction) -> None:
        self.append_player_list(interaction.user, Status.JOINED)
        self.game = self.load_game(self.game_value)
        initial_channel = self.initiator.voice

        embed = await self.create_embed()

        await interaction.response.send_message(view=self, embed=embed)
        if initial_channel:
            self.channel = await self.initiator.guild.create_voice_channel(
                f"GAME {self.game['title']}"
            )
            await self.initiator.move_to(self.channel)

        self.message = await interaction.original_response()

    async def update_message(self) -> None:
        embed = await self.create_embed()
        await self.message.edit(view=self, embed=embed)

    async def create_embed(self) -> discord.Embed:
        embed = discord.Embed(
            title="",
            description=f'# Lets play {self.game["title"]}\nJoining will instantly move you into the created Voice-Channel!',
        )

        for status in self.status_list:
            embed.add_field(
                inline=True, name=status.value, value=self.stringify_list(status.value)
            )

        embed.add_field(
            inline=True,
            name=f"{self.count_players()}/{self.max_players} Players",
            value="",
        )
        embed.add_field(inline=True, name="", value="")
        embed.add_field(inline=True, name=f"Mode: {self.mode_value}", value="")

        embed.set_image(url=self.game["image"])

        embed.set_footer(
            icon_url=self.initiator.avatar.url,  # type: ignore
            text=f"Called by {self.initiator.display_name}",
        )

        return embed

    def append_player_list(
        self, player: discord.Member | discord.User, status: Status
    ) -> None:
        self.all_players.append((player, status))

    def stringify_list(self, key: str) -> str:
        string = ""
        for player in self.all_players:
            if player[1].value == key:
                string += "\n" + f"<@{player[0].id}>"
        if string != "":
            return string
        return "-"

    def count_players(self) -> int:
        players = 0
        for player in self.all_players:
            if player[1] == Status.JOINED:
                players += 1
        return players

    @staticmethod
    def load_game(keyname: str) -> dict[str, str]:
        games: dict = get_games()  # type: ignore
        games = games.get("games")  # type: ignore
        for game in games:  # type: ignore
            if game["keyname"] == keyname:
                return {"title": game["name"], "image": game["image"]}
        return {}

    @discord.ui.button(label="Join", style=discord.ButtonStyle.green)
    async def join_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,  # type: ignore
    ) -> None:
        await interaction.response.defer()
        await self.update_player(interaction, Status.JOINED)
        if interaction.user.voice:  # type: ignore
            await interaction.user.move_to(self.channel)  # type: ignore

    @discord.ui.button(label="Decline", style=discord.ButtonStyle.red)
    async def decline_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,  # type: ignore
    ) -> None:
        await interaction.response.defer()
        await self.update_player(interaction, Status.DECLINED)
        if interaction.user.voice:  # type: ignore
            await interaction.user.move_to(self.channel)  # type: ignore

    @discord.ui.button(label="Not sure", style=discord.ButtonStyle.gray)
    async def not_sure_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,  # type: ignore
    ) -> None:
        await interaction.response.defer()
        await self.update_player(interaction, Status.NOT_SURE)
        if interaction.user.voice:  # type: ignore
            await interaction.user.move_to(self.channel)  # type: ignore

    async def update_player(self, interaction: discord.Interaction, key: Status) -> None:
        for player in self.all_players:
            if player[0] == interaction.user:
                if player[1] == key:
                    await interaction.followup.send(
                        f"You are already in the game as '{key.value}'!", ephemeral=True
                    )
                    return
                else:
                    index = self.all_players.index(player)
                    player = (interaction.user, key)
                    self.all_players[index] = player
                    await interaction.followup.send(
                        f"Your status now is '{key.value}'!", ephemeral=True
                    )
                    await self.update_message()
                    return
        self.append_player_list(interaction.user, key)
        await self.update_message()
        


async def initialize(
    interaction: discord.Interaction,
    game: app_commands.Choice[str],
    mode: app_commands.Choice[str],
    player_count: int,
) -> None:
    view: MikoLetsPlayView = await set_view_options(
        initiator=interaction.user,  # type: ignore
        game_value=game.value,
        mode_value=mode.value,
        max_players=player_count,
    )
    await view.send_message(interaction)


async def set_view_options(
    initiator: discord.Member, game_value: str, mode_value: str, max_players: int
) -> MikoLetsPlayView:
    view = MikoLetsPlayView(timeout=None)
    view.initiator = initiator
    view.game_value = game_value
    view.mode_value = mode_value
    view.max_players = max_players
    return view
