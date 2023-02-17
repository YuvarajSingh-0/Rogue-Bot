
import discord
import os
# from dotenv import load_dotenv
from discord.ext import commands
from keep_alive import keep_alive
# load_dotenv()
intents = discord.Intents.all()
intents.members = True
intents.reactions-True
bot = commands.Bot(command_prefix=['?', '<@822173614236237865> '],
                   description="A Testing Bot for Admin ^-^",
                   intents=intents)

@bot.event
async def on_ready():
    print("Logged in as ", bot.user.name)
    print('---------------------------')


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension}')


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}')


@bot.command()
async def reloadAll(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension}')

@bot.command()
async def prefix(ctx):
    await ctx.send("Prefix is '?' for now")


@bot.command()
async def hello(ctx, lol=""):
    """Just a Simple Hello Test Message"""
    await ctx.send('?hello {}'.format((lol)))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
if __name__=='__main__':
  
  my_secret = os.environ['TOKEN']
  keep_alive()
  bot.run(my_secret)
