from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension


class Hello(Cog_Extension):

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"!Hi <@{ctx.author.id}>")

def setup(bot):
    bot.add_cog(Hello(bot))