from email import message
import discord
from discord.ext import commands
import asyncio


class Timer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def timer(self, ctx, t: int, reason="Timer"):
        embed = discord.Embed(title=reason, description="{} secs".format(t), color=0x00ff00).set_author(
            icon_url="https://thumbs.dreamstime.com/b/timer-concept-vector-linear-icon-isolated-transparent-backgro-background-transparency-outline-style-130085747.jpgg", name=ctx.guild.name)
        mess = await ctx.send(embed=embed)
        await mess.add_reaction('😀')
        while (t != 0):
            t = t - 1
            # await mess.edit(embed=discord.Embed(title='Timer', description="{} secs".format (t), color=0x00ff00).set_author(icon_url="https://thumbs.dreamstime.com/b/timer-concept-vector-linear-icon-isolated-transparent-backgro-background-transparency-outline-style-130085747.jpg",name="Server Name"))
            await asyncio.sleep(1)
        mess = await mess.channel.fetch_message(mess.id)
        # print(mess.reactions[0].users())
        react_users_list = [u.mention async for u in mess.reactions[0].users()]
        await ctx.send("{0}".format(react_users_list), delete_after=5)
        await ctx.send("Your Timer for {0} has Ended => {1}".format(reason, mess.jump_url))
        await mess.edit(embed=discord.Embed(title=reason, description="Your Timer has Ended.", color=0x00ff00).set_author(icon_url="https://thumbs.dreamstime.com/b/timer-concept-vector-linear-icon-isolated-transparent-backgro-background-transparency-outline-style-130085747.jpg", name=ctx.guild.name))


def setup(bot):
    bot.add_cog(Timer(bot))
    print("Timer.py Loaded")
