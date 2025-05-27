import discord

class Events:
    def __init__(self, client):
        self.client = client
        self.register_events()

    def register_events(self):
        @self.client.event
        async def on_member_join(member: discord.Member):
            channel = discord.utils.get(member.guild.text_channels, name="powitania")
            if channel:
                await channel.send(f"Witam, {member.mention}!")
            
        @self.client.event
        async def on_message_delete(message: discord.Message):
            log_channel = discord.utils.get(message.guild.text_channels, name="logi")
            if log_channel:
                embed = discord.Embed(title="Del msg", color=discord.Color.red())
                embed.add_field(name="Kurwiszon", value=message.author.mention, inline=False)
                embed.add_field(name="Treść rakotworczej wiadomości", value=message.content or "NULL kurwo", inline=False)
                embed.add_field(name="Dziura o nazwie ", value=message.channel.mention, inline=False)
                embed.add_field(name="Data DEL", value=discord.utils.format_dt(message.created_at, style='F'), inline=False)
                await log_channel.send(embed=embed)
