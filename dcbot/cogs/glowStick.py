from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension


class GlowStick(Cog_Extension):

    @commands.command()
    async def glowStick(self, ctx):
        await ctx.send(file=discord.File('cogs/Glowsticks.gif'))

def setup(bot):
    bot.add_cog(GlowStick(bot))