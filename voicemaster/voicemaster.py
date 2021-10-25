import discord

from redbot.core import commands

class VoiceMaster(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_members=True)
    @commands.guild_only()
    async def mute(self, ctx: commands.Context, *, member: discord.Member):
        """Mute a member in a voice channel"""
        if member.voice.self_mute:
            return await ctx.send("This member is already muted")
        await member.edit(mute=True)
        await ctx.send(f"{member.mention} has been muted")

    @commands.command()
    @commands.has_permissions(manage_members=True)
    @commands.guild_only()
    async def unmute(self, ctx: commands.Context, *, member: discord.Member):
        """Unmute a member in a voice channel"""
        if not member.voice.self_mute:
            return await ctx.send("This member is not muted")
        await member.edit(mute=False)
        await ctx.send(f"{member.mention} has been unmuted")

    @commands.command()
    @commands.has_permissions(manage_members=True)
    @commands.guild_only()
    async def deafen(self, ctx: commands.Context, *, member: discord.Member):
        """Deafen a member in a voice channel"""
        if member.voice.self_deaf:
            return await ctx.send("This member is already deafened")
        await member.edit(deaf=True)
        await ctx.send(f"{member.mention} has been deafened")

    @commands.command()
    @commands.has_permissions(manage_members=True)
    @commands.guild_only()
    async def undeafen(self, ctx: commands.Context, *, member: discord.Member):
        """Undeafen a member in a voice channel"""
        if not member.voice.self_deaf:
            return await ctx.send("This member is not deafened")
        await member.edit(deaf=False)
        await ctx.send(f"{member.mention} has been undeafened")
        