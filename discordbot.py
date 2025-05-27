import discord
from discord.ext import commands
from config import TOKEN
from commands import Commands
from events import Events

intents = discord.Intents.default()
intents.members = True

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = MyClient()

# Rejestr komend 
Commands(client)
Events(client)

if __name__ == "__main__":
    if not TOKEN:
        print("Ustaw kurwo token w .env")
    else:
        client.run(TOKEN)
