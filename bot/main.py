import discord
from discord.ext import commands
from timer import Timer
from osuapi import Osuapi
from embed import Embedi
import sys
import requests
import pymongo
from pymongo import MongoClient
import oppadc

emojis = {
        "X": "<:bibelsX:753277439102418996>",
        "S": "<:bibelsS:753277217420607679>",
        "XH": "<:bibelsXH:753277379048374334>",
        "SH": "<:bibelsSH:753277326128709665>",
        "A": "<:bibelsA:753276834933637282>",
        "B": "<:bibelsB:753276991473451020>",
        "C": "<:bibelsC:753277059094020216>",
        "D": "<:bibelsD:753277123070001244>",
        "F": "<:bibelsF:776190735950544936>"
        }

with open('apikey.txt', 'r') as apifile:
    apimoro = apifile.readlines()
    discordapikey = apimoro[0].rstrip()
    osuapikey = apimoro[1].rstrip()
    mongodbpass = apimoro[2].rstrip()
bot = commands.Bot(command_prefix=',', activity=discord.Game(name="osu!"))
a = Timer()
a.start()
o = Osuapi(osuapikey)
em = Embedi()
client = pymongo.MongoClient(f"mongodb+srv://Eliaasi:{mongodbpass}@bibels.d7mn2.mongodb.net/bibels?retryWrites=true&w=majority")
db = client.bibels
collection = db.osuprofile

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
            em.osuemb(osup, osut, embed)
            await message.channel.send(embed=embed)
        except:
            error = sys.exc_info()[0]
            if error == IndexError:
                if collection.count_documents({"discordid": message.author.id}) == 0:
                    await message.channel.send("Set your osu! username with ,setosu command!")
                else:
                    if len(str(" ".join(message.content.split(" ")[1:]))) != 0:
                        await message.channel.send("User does not exist")
                    else:
                        found = collection.find_one({"discordid": message.author.id}, {"_id": 0, "osuname": 1})
                        osup = o.profile(found['osuname'])  
                        osut = o.top(found['osuname'])
                        embed = discord.Embed(colour=discord.Colour(0xFFC0CB))
                        em.osuemb(osup, osut, embed)
                        await message.channel.send(embed=embed)

    elif message.content.startswith(',setosu'):
        if collection.count_documents({"discordid": message.author.id}) == 0:
            collection.insert_one({"discordid": message.author.id, "osuname": "_".join(message.content.split(" ")[1:])})
            await message.channel.send("pog")
        else:
            found = collection.find_one({"discordid": message.author.id}, {"_id": 0, "osuname": 1})
            collection.update_one({"osuname" :found['osuname']}, {"$set": {"osuname":"_".join(message.content.split(" ")[1:])}})
            await message.channel.send("updated")
    
    elif message.content.startswith(',rs'):
        osur = o.recent("_".join(message.content.split(" ")[1:]))
        mods = o.mod(osur[0]['enabled_mods'])
        fix = o.peppyshitfix(mods, 0)
        osub = o.beatmap(osur[0]['beatmap_id'], int(osur[0]['enabled_mods']) - int(fix))
        embed = discord.Embed(colour=discord.Colour(0xFFc0CB))
        osup = o.profile("_".join(message.content.split(" ")[1:]))
        acc = o.count_acc(int(osur[0]['count50']), int(osur[0]['count100']), int(osur[0]['count300']), int(osur[0]['countmiss']))
        mdata = requests.get(f"https://osu.ppy.sh/osu/{osur[0]['beatmap_id']}").content.decode('utf-8')
        PP, FPP = o.ppcal("".join(mods), acc, osur, mdata), o.fcpp("".join(mods), acc, mdata)
        em.recemb(osup, osur, osub, "".join(mods), acc, PP.total_pp, FPP.total_pp, emojis, embed)
        await message.channel.send(embed=embed)
bot.run(discordapikey)
