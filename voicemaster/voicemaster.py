import discord

from redbot.core import commands

class VoiceMaster(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def mute(self, ctx: commands.Context, *, member: discord.Member):
        """Mute a member in a voice channel"""
        if member.voice.self_mute:
            return await ctx.send("This member is already muted")
        try: 
            await member.edit(mute=True)
        except discord.Forbidden:
            return await ctx.send("I don't have permission to mute that member")
        await ctx.send(f"{member.mention} has been muted")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def unmute(self, ctx: commands.Context, *, member: discord.Member):
        """Unmute a member in a voice channel"""
        if not member.voice.self_mute:
            return await ctx.send("This member is not muted")
        try: 
            await member.edit(mute=False)
        except discord.Forbidden:
            await ctx.send("I don't have permission to unmute that member")
        await ctx.send(f"{member.mention} has been unmuted")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def deafen(self, ctx: commands.Context, *, member: discord.Member):
        """Deafen a member in a voice channel"""
        try:
            if member.voice.self_deaf:
                return await ctx.send("This member is already deafened")
        except discord.Forbidden:
            return await ctx.send("I don't have permission to deafen this member")
        await member.edit(deaf=True)
        await ctx.send(f"{member.mention} has been deafened")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def undeafen(self, ctx: commands.Context, *, member: discord.Member):
        """Undeafen a member in a voice channel"""
        if not member.voice.self_deaf:
            return await ctx.send("This member is not deafened")
        try:
            await member.edit(deaf=False)
        except discord.Forbidden:
            return await ctx.send("I do not have the permissions to undeafen this member")
        await ctx.send(f"{member.mention} has been undeafened")
