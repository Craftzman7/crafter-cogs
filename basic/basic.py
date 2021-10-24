from redbot.core import commands

class BasicCog(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def basic(self, ctx):
        """Basic command"""
        await ctx.send("Basic message")