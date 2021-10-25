import discord
import nekos

from redbot.core import commands

class Roleplay(commands.Cog):
    """Roleplay cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def slap(self, ctx, *, user: discord.Member):
        """Slap another user"""
        if user == ctx.author:
            return await ctx.send("You can't slap your self!")
        try:
            embed = discord.Embed(title="Ouch!", color=0x00ff00)
            url = nekos.img("slap")
            embed.set_image(url=url)
            await ctx.send(embed=embed)
        except:
            await ctx.send("An excpetion occured please open an issue on Github!")

    @commands.command()
    @commands.guild_only()
    async def hug(self, ctx, *, user: discord.Member):
        "Hug another user"
        if user == ctx.author:
            return await ctx.send("You can't slap your self")
        try:
            embed = discord.Embed(title="Awwww", color=0x00ff00)
            url = nekos.img("hug")
            embed.set_image(url=url)
            await ctx.send(embed=embed)
        except:
            await ctx.send("An exception occured please open an issue on Github!")