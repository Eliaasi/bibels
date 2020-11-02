import discord
from discord.ext import commands
from timer import Timer
from osuapi import Osuapi
from embed import Embedi
import sys

with open('apikey.txt', 'r') as apifile:
    apimoro = apifile.readlines()
    discordapikey = apimoro[0].rstrip()
    osuapikey = apimoro[1].rstrip()
bot = commands.Bot(command_prefix=',', activity=discord.Game(name="osu!"))
a = Timer()
a.start()
o = Osuapi(osuapikey)
em = Embedi()
#em.printt()

@bot.event
async def on_ready():
    a.stop()
    print(f'Bot log on in')

@bot.event
async def on_message(message):
    if message.content.startswith(',osu'):
        try:
            osup = o.profile(" ".join(message.content.split(" ")[1:]))
            osut = o.top(" ".join(message.content.split(" ")[1:]))
            embed = discord.Embed(colour=discord.Colour(0xFFC0CB))
            em.setauthor(osup[0]['user_id'], f"{osup[0]['username']} #{osup[0]['pp_rank']} ({osup[0]['country']}#{osup[0]['pp_country_rank']})", embed)
            em.setthumbnail(osup[0]['user_id'], embed)
            em.addfield("Playcount", osup[0]['playcount'], "True", embed)
            em.addfield("Top Play", f"{int(round(float(osut[0]['pp'])))}pp", "True", embed)
            em.addfield("Accuracy", f"{float(osup[0]['accuracy']):.2f}%", "True", embed)
            em.addfield("Total pp", int(round(float(osup[0]['pp_raw']))), "True", embed)
            em.addfield("Score", f"{int(osup[0]['ranked_score'])/1000000000:.1f}B", "True", embed)
            em.addfield("Playtime", f"{int(int(osup[0]['total_seconds_played'])/3600)}h", "True", embed)
            await message.channel.send(embed=embed)
        except Exception as a:
            print(a)

bot.run(discordapikey)
