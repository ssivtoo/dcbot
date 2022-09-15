from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension


def getBudget():
    import pygsheets
    gc = pygsheets.authorize(service_file='dcbudget-ebd6ae3a6cc0.json')

    sht = gc.open_by_url(
        'https://docs.google.com/spreadsheets/d/1OpOhzSdHlHq2CwH87Sda4UEdf3GCvr9Ez4HIDATOTYc/edit?usp=sharing')

    # wks_list = sht.worksheets()
    # print(wks_list)

    wks = sht[0]

    budget = wks.cell('C1')
    return budget.value


class Budget(Cog_Extension):

    @commands.command()
    async def budget(self, ctx):
        # code here
        await ctx.send(getBudget())


def setup(bot):
    bot.add_cog(Budget(bot))