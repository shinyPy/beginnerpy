import discord
import random
import datetime
from discord.ext import commands
from discord.ext import tasks
import asyncio


## configuration
TOKEN = "ENTER TOKEN HERE" # enter your bot token here
prefix = ">" # set prefix here
bot = commands.Bot(command_prefix=prefix)
color = 0xffffff # enter hex color of the color you want to set for your embeds (not necessary but yh)
timestamp = (datetime.datetime.utcnow())
bot.remove_command('help')
guild = 682992871326089236 # set the guild id that you're using the bot in
channel = 707239761533861899 



@bot.event
async def on_ready():
    print("Bot is ready for use")
    await bot.change_presence(activity=discord.Game(name='mhm'))


@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Commands",color=color,timestamp=timestamp)
    embed.add_field(name="!start",value="start",inline=False)
    embed.add_field(name="!stop",value="stops",inline=False)
    await ctx.send(embed=embed)


@tasks.loop(seconds=0.1)
async def gen_loop():
    await bot.wait_until_ready()
    get_guild = bot.get_guild(guild)
    get_channel = get_guild.get_channel(channel)
    code = ["A","B","C","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
    letter1 = random.choice(code)
    letter2 = random.choice(code)
    letter3 = random.choice(code)
    letter4 = random.choice(code)
    letter5 = random.choice(code)
    letter6 = random.choice(code)
    code = (letter1+letter2+letter3+letter4+letter5+letter6)
    await get_channel.send(code)


@bot.command()
async def startgen(ctx):
    await ctx.send("starting")
    asyncio.sleep(1)
    await gen_loop.start() #return to tasks

@bot.command()
async def stopgen(ctx):
    gen_loop.stop()
    await ctx.send("stop.") #stop it








bot.run(TOKEN)
