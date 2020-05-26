import discord
from discord.ext import commands

bot=commands.Bot(command_prefix='¤')

@bot.event
async def on_ready():
    print('Bot log on as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if 'tino' in message.content:
        await message.channel.send('kielletty sana häpeä ittees')
    if '¤ping' in message.content:
        await message.channel.send('pong')




bot.run('token')
