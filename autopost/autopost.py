import aiohttp
import asyncio
import discord

from redbot.core import Config, commands, checks

class Autopost(commands.Cog):
    """Auto post images from different sources to a channel"""

    def __init__(self):
        self.config = Config.get_conf(self, 49751390, force_registration=true)

    @commands.command()
    async def autopost(self, ctx, channel: discord.Channel, content: str):
        content_list = ["panda", "fox", "cat"]
        if content not in content_list:
            await ctx.send("Please specify `panda`, `fox`, or `cat`")
            return
        await self.config