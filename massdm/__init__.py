from .basic import BasicCog


def setup(bot):
    bot.add_cog(BasicCog(bot))