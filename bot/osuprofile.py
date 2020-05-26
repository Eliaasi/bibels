import json
import requests
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='¤')

@bot.event
async def on_ready():
    print('Bot log on as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if '¤osu' in message.content:
        command = message.content.split(" ")
        osuname = command[1]
        response = requests.get(f"https://osu.ppy.sh/api/get_user?u={osuname}&k=token")
        data = response.json()
        for username in data:
            lol = username['username'], "rank", username['pp_rank'], "country", username['country'], "country rank", username['pp_country_rank'], "total pp", username['pp_raw']
            userid = username['user_id']
            embedi = discord.Embed(colour=discord.Colour(0xFFC0CB))
            embedi.description=f"{lol} https://osu.ppy.sh/users/{userid})"
            await message.channel.send(embed=embedi)
    elif message.content.startswith("https://osu.ppy.sh/users"):
        osuva = message.content.split("/")
        osuname = osuva[4]
        response = requests.get(f"https://osu.ppy.sh/api/get_user?u={osuname}&k=token")
        data = response.json()
        for username in data:
            lol = username['username'], "rank", username['pp_rank'], "country", username['country'], "country rank", username['pp_country_rank'], "total pp", username['pp_raw']
            embedi = discord.Embed(colour=discord.Colour(0xFFC0CB))
            embedi.description=f"{lol}"
            await message.channel.send(embed=embedi)

bot.run('token')
