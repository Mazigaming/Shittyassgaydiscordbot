import discord
from discord import app_commands
import random

class Commands:
    def __init__(self, client):
        self.client = client
        self.tree = client.tree
        self.warns = {}  #warn count ofc  
        self.register_commands()
    #czesz command
    def register_commands(self):
        @self.tree.command(name="hello", description="hello motherfucker")
        async def hello(interaction: discord.Interaction):
            await interaction.response.send_message(f"Cześć, {interaction.user.mention}!")
       # roll
        @self.tree.command(name="roll", description="Roll a number of kebabs")
        @app_commands.describe(min="min", max="Max")
        async def roll(interaction: discord.Interaction, min: int, max: int):
            if min > max:
                await interaction.response.send_message("Błąd: min nie może być większe niż max.", ephemeral=True)
                return
            result = random.randint(min, max)
            await interaction.response.send_message(f"ilość kebabów to: {result}")
           #dox
        @self.tree.command(name="userinfo", description="Dox")
        @app_commands.describe(user="dox who?")
        async def userinfo(interaction: discord.Interaction, user: discord.User):
            guild = interaction.guild
            member = None
            if guild:
                member = guild.get_member(user.id)
            joined_at = member.joined_at.strftime("%Y-%m-%d %H:%M:%S") if member and member.joined_at else "uknw"
            message = (
                f"Nazwa Gagadtka: {user}\n"
                f"ID Cwela: {user.id}\n"
                f"Data dołączenia do spierdoliska: {joined_at}"
            )
            await interaction.response.send_message(message)
           #warn
        @self.tree.command(name="warn", description="KOP W DUPE")
        @app_commands.describe(user="Kogo ujebać", reason="Kopas w dupas za co?")
        @app_commands.checks.has_permissions(kick_members=True)
        async def warn(interaction: discord.Interaction, user: discord.Member, reason: str = "Brak powodu"):
            user_id = user.id
            self.warns[user_id] = self.warns.get(user_id, 0) + 1
            await interaction.response.send_message(f"{user.mention} Dostał kopa w dupe za. Powód: {reason}. Liczba Dokonanych pogwałceń: {self.warns[user_id]}")
          #odmowa dostepu
        @warn.error
        async def warn_error(interaction: discord.Interaction, error):
            if isinstance(error, app_commands.errors.MissingPermissions):
                await interaction.response.send_message("L BOZO  MAKE UR OWN BOT or get an admin.", ephemeral=True)
