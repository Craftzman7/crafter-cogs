import aiohttp
import discord


from redbot.core import commands

class Animal(commands.Cog):
    """Cog for fetching pictures of animals"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    @commands.command()
    async def Dog(self, ctx):
        """Fetch a random picture of a dog"""
        try:
            async with self.session.get("https://api.thedogapi.com/v1/images/search?format=json") as response:
                data = await response.json()
                embed = discord.Embed(title="Woof!", color=0x00ff00)
                embed.set_image(url=data[0]["url"])
                await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send("There was an exception. Please open an issue on Github") 
