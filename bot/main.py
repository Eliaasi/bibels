import discord
from discord.ext import commands
from timer import Timer
from osuapi import Osuapi
import sys

with open('apikey.txt', 'r') as apifile:
    apimoro = apifile.readlines()
    discordapikey = apimoro[0].rstrip()
    osuapikey = apimoro[1].rstrip()
bot = commands.Bot(command_prefix=',', activity=discord.Game(name="osu!"))
a = Timer()
a.start()
o = Osuapi()

@bot.event
async def on_ready():
    a.stop()
    print(f'Bot log on in')


@bot.event
async def on_message(message):
    if message.content.startswith(',osu'):
        try:
            username, rank = o.profile(" ".join(message.content.split(" ")[1:]), osuapikey)
            await message.channel.send(f"{username} on rankilla {rank}")
        except:
            error = sys.exc_info()[0]
            if error == IndexError:
                await message.channel.send("Haista homo pyronki")
        


bot.run(discordapikey)
