import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import time


json_dict = {}


class JoinLeave(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        global json_dict
        memb_joined = member.joined_at
        json_dict.update(
            {member.guild.id: {member.id: {"Joined At": memb_joined}}})
        print("{0.name} Joined {0.id}".format(member))
        print(json_dict)
        print(member.guild.id)

    @commands.command()
    async def dm(self, ctx, member: discord.Member, *, message):
        await member.send(message)
        await ctx.send("Message Sent")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await member.send("You have been banned from this server.")
        memb_joined = member.joined_at
        curr_time = time.gmtime(time.time())
        print(json_dict)
        if (memb_joined.year == curr_time.tm_year) and (memb_joined.month == curr_time.tm_mon) and (memb_joined.day == curr_time.tm_mday) and ((curr_time.tm_hour - memb_joined.hour) < json_dict[member.guild.id]['freeloaderstime']):
            await member.guild.ban(member, reason="bot ban")
            await member.send("You have been banned from {0.guild.name} for Not Staying Long Enough in the server, or You can say... 'For Freeloading'".format(member))
        # print(curr_time)
        # print("{0.name} Left of ID: {0.id}".format(member))
        print(json_dict)
        # print(member.guild.id)

    @commands.command()
    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def setfreeloaderban(self, ctx, hours=6):
        """Sets Time Period for banning freeLoaders automatically"""
        # json_dict.update({ctx.guild.id: {'freeloaderstime': hours}})
        json_dict[ctx.guild.id].update({'freeloaderstime': hours})
        print(json_dict)
        await ctx.send("Freeloaders Ban Time set to {} hours".format(hours))


def setup(bot):
    bot.add_cog(JoinLeave(bot))
    print("JoinLeave.py Loaded")
