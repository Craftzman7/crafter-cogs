from .massdm import MassDmCog


def setup(bot):
    bot.add_cog(MassDmCog(bot))