from redbot.core import commands

class BasicCog(commands.Cog):
    """A cog used for messaging all users in a server"""

    def __init__(self, bot):
        self.bot = bot
        
    
    @commands.command(name="massdmrole")
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages=True)
    async def massdmrole(self, ctx: commands.Context, role: discord.Role, *, message: str) -> None:
        """Send messages to members with a specified role"""
        

        for member in [e for e in role.members]:
            try:
                await member.send(message.format(member=member, role=role, server=ctx.guild, sender=ctx.author))
            except discord.Forbidden:
                ctx.send(f"Error sending a message to {member} due to insufficient permissions")
                continue
            except discord.DiscordException:
                ctx.send(f"Exception when sending a message to {member}. Please report this to my developers.")
                continue
    
    @commands.has_guild_permissions(manage_messages=True)
    @commands.command(name="massdmserver")
    @commands.guild_only()
    async def massdmserver(self, ctx: commands.Context, *, message: str) -> None:
        """Send messages to members in the whole server"""
        
        role = ctx.guild.id
        for member in [e for e in role.members]:
            try:
                await member.send(message.format(member=member, role=role, server=ctx.guild, sender=ctx.author))
            except discord.Forbidden:
                ctx.send(f"Error sending a message to {member} due to insufficient permissions")
                continue
            except discord.DiscordException:
                ctx.send(f"Exception when sending a message to {member}. Please report this to my developers.")
                continue