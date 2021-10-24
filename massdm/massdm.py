from redbot.core import commands
import discord

class MassDmCog(commands.Cog):
    """A cog used for messaging all users in a server"""

    def __init__(self, bot):
        self.bot = bot
        
    
    @commands.command(name="massdmrole")
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages=True)
    async def massdmrole(self, ctx: commands.Context, role: discord.Role, *, message: str) -> None:
        """Send messages to members with a specified role"""
        
        progress = await ctx.send("Starting DMs")

        for member in [e for e in role.members]:
            if member.id == ctx.author.id:
                continue
            if member.bot:
                await progress.edit(content=f"Skipping {member} (They are a bot)", embed=None)
                continue
            try:
                await progress.edit(content=f"Sending message to {member}", embed=None)
                await member.send(message.format(member=member, role=role, server=ctx.guild, sender=ctx.author))
            except discord.Forbidden:
                ctx.send(f"Error sending a message to {member} due to insufficient permissions")
                continue
            except discord.DiscordException:
                ctx.send(f"Exception when sending a message to {member}. Please report this to my developers.")
                continue

        await progress.edit(content="Done. Mass DMing complete")
    
    @commands.has_guild_permissions(manage_messages=True)
    @commands.command(name="massdmserver")
    @commands.guild_only()
    async def massdmserver(self, ctx: commands.Context, *, message: str) -> None:
        """Send messages to members in the whole server"""
        
        progress = await ctx.send("Starting DMs")
        for member in ctx.guild.members:
            if member.id == ctx.author.id:
                continue
            if member.bot:
                await progress.edit(content=f"Skipping {member} (They are a bot)", embed=None)
                continue
            try:
                await progress.edit(content=f"Sending message to {member}", embed=None)
                await member.send(message.format(member=member, server=ctx.guild, sender=ctx.author))
            except discord.Forbidden:
                ctx.send(f"Error sending a message to {member} due to insufficient permissions")
                continue
            except discord.DiscordException:
                ctx.send(f"Discord API exception when sending a message to {member}")
                continue

        await progress.edit(content="Done. Mass DMing complete")