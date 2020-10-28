import discord
from discord.ext import commands
from timer import Timer

with open('apikey.txt', 'r') as apifile:
    discordapikey = apifile.readline()
bot = commands.Bot(command_prefix=',')
a = Timer()
a.start()

@bot.event
async def on_ready():
    a.stop()
    print(f'Bot log on in')


@bot.event
async def on_message(message):
    if message.content.startswith(',test'):
        print('moro')


bot.run(discordapikey)
    

