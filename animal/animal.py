import aiohttp
import discord


from redbot.core import commands

class Animal(commands.Cog):
    """Cog for fetching pictures of animals"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    @commands.command()
    @commands.guild_only()
    async def dog(self, ctx):
        """Fetch a random picture of a dog"""
        try:
            async with self.session.get("https://api.thedogapi.com/v1/images/search?format=json") as response:
                data = await response.json()
                embed = discord.Embed(title="Woof!", color=0x00ff00)
                embed.set_image(url=data[0]["url"])
                await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send("There was an exception. Please open an issue on Github") 

    @commands.command()
    @commands.guild_only()
    async def cat(self, ctx):
        """Fetch a random picture of a cat"""
        try:
            async with self.session.get("https://api.thecatapi.com/v1/images/search?format=json") as response:
                data = await response.json()
                embed = discord.Embed(title="Meow!", color=0x00ff00)
                embed.set_image(url=data[0]["url"])
                await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send("There was an exception. Please open an issue on Github") 

    @commands.command()
    @commands.guild_only()
    async def fox(self, ctx):
        """Fetch a random picture of a fox"""
        try:
            async with self.session.get("https://randomfox.ca/floof/") as response:
                data = await response.json()
                embed = discord.Embed(title="What does the fox say?", color=0x00ff00)
                embed.set_image(url=data["image"])
                await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send("There was an exception. Please open an issue on Github")

    @commands.command()
    @commands.guild_only()
    async def lizard(self, ctx):
        """Fetch a random picture of a lizard"""
        try:
            async with self.session.get("https://nekos.life/api/lizard") as response:
                data = await response.json()
                embed = discord.Embed(title="Lizard!", color=0x00ff00)
                embed.set_image(url=data["url"])
                await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send("There was an exception. Please open an issue on Github")

    @commands.command()
    @commands.guild_only()
    async def bird(self, ctx):
        """Fetch a random picture of a bird"""
        try:
            async with self.session.get("https://some-random-api.ml/img/birb") as response:
                data = await response.json()
                embed = discord.Embed(title="Tweet tweet!", color=0x00ff00)
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send("There was an exception. Please open an issue on Github")

    @commands.command()
    @commands.guild_only()
    async def panda(self, ctx):
        """Fetch a random picture of a panda"""
        try:
            async with self.session.get("https://some-random-api.ml/img/panda") as response:
                data = await response.json()
                embed = discord.Embed(title="Panda!", color=0x00ff00)
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send("There was an exception. Please open an issue on Github")

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())