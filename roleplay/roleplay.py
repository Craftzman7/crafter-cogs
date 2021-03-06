import discord
import nekos
import traceback

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
        if user.bot:
            return await ctx.send("You can't interact with bots")
        try:
            embed = discord.Embed(title="Ouch!", color=0x00ff00)
            url = nekos.img("slap")
            embed.set_image(url=url)
            await ctx.send(embed=embed)
        except:
            await ctx.send("An excpetion occured please open an issue on Github! Traceback: {}".format(traceback.print_exc()))

    @commands.command()
    @commands.guild_only()
    async def hug(self, ctx, *, user: discord.Member):
        "Hug another user"
        if user == ctx.author:
            return await ctx.send("You can't hug your self")
        if user.bot:
            return await ctx.send("You can't interact with bots")
        try:
            embed = discord.Embed(title="Awwww", color=0x00ff00)
            url = nekos.img("hug")
            embed.set_image(url=url)
            await ctx.send(embed=embed)
        except:
            await ctx.send("An exception occured please open an issue on Github! Traceback: {}".format(traceback.print_exc()))

    @commands.command()
    @commands.guild_only()
    async def pat(self, ctx, *, user: discord.Member):
        "Pat another user"
        if user == ctx.author:
            return await ctx.send("You can't pat your self")
        if user.bot:
            return await ctx.send("You can't interact with bots")
        try:
            embed = discord.Embed(title="Pat pat", color=0x00ff00)
            url = nekos.img("pat")
            embed.set_image(url=url)
            await ctx.send(embed=embed)
        except:
            await ctx.send("An exception occured please open an issue on Github! Traceback: {}".format(traceback.print_exc()))
    
    @commands.command()
    @commands.guild_only()
    async def tickle(self, ctx, *, user: discord.Member):
        """Tickle another user"""
        if user == ctx.author:
            return await ctx.send("You can't tickle your self")
        if user.bot:
            return await ctx.send("You can't interact with bots")
        try:
            embed = discord.Embed(title="Aaaaaa that tickles", color=0x00ff00)
            url = nekos.img("tickle")
            embed.set_image(url=url)
            await ctx.send(embed=embed)
        except:
            await ctx.send("An exception occured please open an issue on Github! Traceback: {}".format(traceback.print_exc()))

    @commands.command()
    @commands.guild_only()
    async def poke(self, ctx, *, user: discord.Member):
        """Poke another user"""
        if user == ctx.author:
            return await ctx.send("You can't poke your self")
        if user.bot:
            return await ctx.send("You can't interact with bots")
        try:
            embed = discord.Embed(title="Ow", color=0x00ff00)
            url = nekos.img("poke")
            embed.set_image(url=url)
            await ctx.send(embed=embed)
        except:
            await ctx.send("An exception occured please open an issue on Github! Traceback: {}".format(traceback.print_exc()))

    @commands.command()
    @commands.guild_only()
    async def kiss(self, ctx, *, user: discord.Member):
        """Kiss another user"""
        if user == ctx.author:
            return await ctx.send("You can't poke your self")
        if user.bot:
            return await ctx.send("You can't interact with bots")
        try:
            embed = discord.Embed(title="Awwww", color=0x00ff00)
            url = nekos.img("kiss")
            embed.set_image(url=url)
            await ctx.send(embed=embed)
        except:
            await ctx.send("An exception occured please open an issue on Github! Traceback: {}".format(traceback.print_exc()))
