import json
import requests
import discord
from discord.ext import commands
import sys
import pymongo
from pymongo import MongoClient

bot = commands.Bot(command_prefix='¤')

client = MongoClient()
db = client.bibels
collection = db.osuprofile

emojis = {
"X": "<:bibelsX:753277439102418996>",
"S": "<:bibelsS:753277217420607679>",
"XH": "<:bibelsXH:753277379048374334>",
"SH": "<:bibelsSH:753277326128709665>",
"A": "<:bibelsA:753276834933637282>",
"B": "<:bibelsB:753276991473451020>",
"C": "<:bibelsC:753277059094020216>",
"D": "<:bibelsD:753277123070001244>"
}

def mapinhaku(datastream):
    maps = []
    for i in range(0,3):
        map = datastream[i]['beatmap_id']
        modit = datastream[i]['enabled_mods']
        mapinfo = requests.get(f"https://osu.ppy.sh/api/get_beatmaps?k=token&b={map}&m=0&mods={modit}")
        mappi = mapinfo.content.decode("utf-8")
        mapinffo = json.loads(mappi)
        maps.append(mapinffo)
    return maps

def num_to_mod(number):
    number = int(number)
    mod_list = []

    if number & 1<<0:   mod_list.append('NF')
    if number & 1<<1:   mod_list.append('EZ')
    if number & 1<<3:   mod_list.append('HD')
    if number & 1<<4:   mod_list.append('HR')
    if number & 1<<5:   mod_list.append('SD')
    if number & 1<<9:   mod_list.append('NC')
    elif number & 1<<6: mod_list.append('DT')
    if number & 1<<7:   mod_list.append('RX')
    if number & 1<<8:   mod_list.append('HT')
    if number & 1<<10:  mod_list.append('FL')
    if number & 1<<12:  mod_list.append('SO')
    if number & 1<<14:  mod_list.append('PF')
    if number & 1<<15:  mod_list.append('4 KEY')
    if number & 1<<16:  mod_list.append('5 KEY')
    if number & 1<<17:  mod_list.append('6 KEY')
    if number & 1<<18:  mod_list.append('7 KEY')
    if number & 1<<19:  mod_list.append('8 KEY')
    if number & 1<<20:  mod_list.append('FI')
    if number & 1<<24:  mod_list.append('9 KEY')
    if number & 1<<25:  mod_list.append('10 KEY')
    if number & 1<<26:  mod_list.append('1 KEY')
    if number & 1<<27:  mod_list.append('3 KEY')
    if number & 1<<28:  mod_list.append('2 KEY')
    return mod_list

@bot.event
async def on_ready():
    print('Bot log on as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.content.startswith(',osu'):
        try:
            osuname = "_".join(message.content.split(" ")[1:])
            pp = requests.get(f"https://osu.ppy.sh/api/get_user_best?u={osuname}&k=token")
            isopp = pp.content.decode("utf-8")
            tosiisopp = json.loads(isopp)
            isoinpp = tosiisopp[0]['pp']
            intpp = int(round(float(isoinpp)))
            response = requests.get(f"https://osu.ppy.sh/api/get_user?u={osuname}&k=token")
            data = response.json()
            for u in data:
                userid = u['user_id']
                rawaccuracy = u['accuracy']
                accuracy = float(rawaccuracy)
                acc = "{:.2f}".format(accuracy)
                rawpp = int(round(float(u['pp_raw'])))
                scorenum = int(u['ranked_score'])
                if scorenum >= 1000000000:
                    oikeest = "{:.1f}".format(scorenum/1000000000)
                else:
                    oikeest = "0"
                playtime = int(u['total_seconds_played'])
                hplaytime = playtime/3600
                hplaytime = int(hplaytime)
                embedi = discord.Embed(colour=discord.Colour(0xFFC0CB))
                embedi.set_author(url=f"https://osu.ppy.sh/users/{userid}", icon_url=f"https://a.ppy.sh/{userid}", name=f"{u['username']} #{u['pp_rank']} ({u['country']}#{u['pp_country_rank']})")
                embedi.set_thumbnail(url=f"https://a.ppy.sh/{userid}")
                embedi.add_field(name="Playcount", value=u['playcount'], inline=True)
                embedi.add_field(name="Top Play", value=f"{intpp}pp", inline=True)
                embedi.add_field(name="Accuracy", value=f"{acc}%", inline=True)
                embedi.add_field(name="Total pp", value=rawpp, inline=True)
                embedi.add_field(name="Score", value=f"{oikeest}B", inline=True)
                embedi.add_field(name="Playtime", value=f"{hplaytime}h", inline=True)
                await message.channel.send(embed=embedi)
        except:
            error = sys.exc_info()[0]
            if error == IndexError:
                discordid = message.author.id
                haku = { "discordid": discordid }
                naku = { "_id": 0, "osuname": 1 }
                paku = collection.find(haku, naku)
                for osunimi in paku:
                    ousnimi = (f"{osunimi}")
                    oosnimi = ousnimi.split("'")
                    osuname = oosnimi[3]
                    pp = requests.get(f"https://osu.ppy.sh/api/get_user_best?u={osuname}&k=token")
                    isopp = pp.content.decode("utf-8")
                    tosiisopp = json.loads(isopp)
                    isoinpp = tosiisopp[0]['pp']
                    intpp = int(round(float(isoinpp)))
                    response = requests.get(f"https://osu.ppy.sh/api/get_user?u={osuname}&k=token")
                    data = response.json()
                    if len(data) == 0:
                        embedi = discord.Embed(colour=discord.Colour(0xFFC0CB))
                        embedi.description="et oo laittanu nimee tai nimes on väärin"
                        await message.channel.send(embed=embedi)
                    for u in data:
                        userid = u['user_id']
                        rawaccuracy = u['accuracy']
                        accuracy = float(rawaccuracy)
                        acc = "{:.2f}".format(accuracy)
                        rawpp = int(round(float(u['pp_raw'])))
                        scorenum = int(u['ranked_score'])
                        oikea = int(min(1000000000, scorenum))
                        if oikea == 1000000000:
                            oikean = scorenum/1000000000
                            oikeest = "{:.1f}".format(oikean)
                            billion = "B"
                        else:
                            oikeest = "0"
                            billion = "0"
                        playtime = int(u['total_seconds_played'])
                        hplaytime = playtime/3600
                        hplaytime = int(hplaytime)
                        embedi = discord.Embed(colour=discord.Colour(0xFFC0CB))
                        embedi.set_author(url=f"https://osu.ppy.sh/users/{userid}", icon_url=f"https://a.ppy.sh/{userid}", name=f"{u['username']} #{u['pp_rank']} ({u['country']}#{u['pp_country_rank']})")
                        embedi.set_thumbnail(url=f"https://a.ppy.sh/{userid}")
                        embedi.add_field(name="Playcount", value=u['playcount'], inline=True)
                        embedi.add_field(name="Top Play", value=f"{intpp}pp", inline=True)
                        embedi.add_field(name="Accuracy", value=f"{acc}%", inline=True)
                        embedi.add_field(name="Total pp", value=rawpp, inline=True)
                        embedi.add_field(name="Score", value=f"{oikeest}{billion}", inline=True)
                        embedi.add_field(name="Playtime", value=f"{hplaytime}h", inline=True)
                        await message.channel.send(embed=embedi)




                #errori = discord.Embed(colour=discord.Colour(0xFFC0CB))
                #errori.description=("Et laittanu nimee")
                #await message.channel.send(embed=errori)
            #else:
                #errori = discord.Embed(colour=discord.Colour(0xFFC0CB))
                #errori.description=("umm")
                #await message.channel.send(embed=errori)

    elif message.content.startswith("https://osu.ppy.sh/users"):
        osuva = message.content.split("/")
        osuname = osuva[4]
        pp = requests.get(f"https://osu.ppy.sh/api/get_user_best?u={osuname}&k=token")
        isopp = pp.content.decode("utf-8")
        tosiisopp = json.loads(isopp)
        isoinpp = tosiisopp[0]['pp']
        intpp = int(round(float(isoinpp)))
        response = requests.get(f"https://osu.ppy.sh/api/get_user?u={osuname}&k=token")
        data = response.json()
        for u in data:
            userid = u['user_id']
            rawaccuracy = u['accuracy']
            accuracy = float(rawaccuracy)
            acc = "{:.2f}".format(accuracy)
            rawpp = int(round(float(u['pp_raw'])))
            scorenum = int(u['ranked_score'])
            oikea = int(min(1000000000, scorenum))
            if oikea == 1000000000:
                oikean = scorenum/1000000000
                oikeest = "{:.1f}".format(oikean)
                billion = "B"
            else:
                oikeest = "0"
                billion = "0"
            playtime = int(u['total_seconds_played'])
            hplaytime = playtime/3600
            hplaytime = int(hplaytime)
            embedi = discord.Embed(colour=discord.Colour(0xFFC0CB))
            embedi.set_author(url=f"https://osu.ppy.sh/users/{userid}", icon_url=f"https://a.ppy.sh/{userid}", name=f"{u['username']} #{u['pp_rank']} ({u['country']}#{u['pp_country_rank']})")
            embedi.set_thumbnail(url=f"https://a.ppy.sh/{userid}")
            embedi.add_field(name="Playcount", value=u['playcount'], inline=True)
            embedi.add_field(name="Top Play", value=f"{intpp}pp", inline=True)
            embedi.add_field(name="Accuracy", value=f"{acc}%", inline=True)
            embedi.add_field(name="Total pp", value=rawpp, inline=True)
            embedi.add_field(name="Score", value=f"{oikeest}{billion}", inline=True)
            embedi.add_field(name="Playtime", value=f"{hplaytime}h", inline=True)
            await message.channel.send(embed=embedi)

    elif message.content.startswith(',setosu'):
        discordid = message.author.id
        osuname = "_".join(message.content.split(" ")[1:])
        haku = { "discordid": discordid }
        naku = { "_id": 0, "osuname": 1 }
        paku = collection.find(haku, naku).count()
        osunimi = collection.find(haku, naku)
        if paku == 0:
            osumonkey = {
            "discordid":discordid,
            "osuname":osuname,
            }
            collection.insert_one(osumonkey)
            embedi = discord.Embed(colour=discord.Colour(0xFFC0CB))
            embedi.description=("nimes ehkä meni databasee")
            await message.channel.send(embed=embedi)
        else:
            for nbot in osunimi:
                ousnimi = (f"{nbot}")
                oosnimi = ousnimi.split("'")
                ooonimi = oosnimi[3]
                osumonkey = {
                "osuname":ooonimi,
                }
                osuhorse = { "$set": { "osuname": osuname } }
                collection.update_one(osumonkey, osuhorse)
                embedi = discord.Embed(colour=discord.Colour(0xFFC0CB))
                embedi.description=("nimes ehkä päivitty")
                await message.channel.send(embed=embedi)

    elif message.content.startswith(',nimi'):
        discordid = message.author.id
        haku = { "discordid": discordid }
        naku = { "_id": 0, "osuname": 1 }
        paku = collection.find(haku, naku)
        for osunimi in paku:
            ousnimi = (f"{osunimi}")
            oosnimi = ousnimi.split("'")
            ooonimi = oosnimi[3]
            embedi = discord.Embed(colour=discord.Colour(0xFFC0CB))
            embedi.description=f"{ooonimi}"
            await message.channel.send(embed=embedi)
            print(oosnimi[3])

    elif message.content.startswith(',avatarosu'):
        try:
            discordid = message.author.id
            command = message.content.split(" ")
            osuname = command[1]
            response = requests.get(f"https://osu.ppy.sh/api/get_user?u={osuname}&k=token")
            data = response.json()
            for username in data:
                avatar = username['user_id']
                embedi = discord.Embed(colour=discord.Colour(0xFFC0CB))
                embedi.description="moi"
                embedi.set_author(icon_url=f"https://a.ppy.sh/{avatar}", name="ei")
                await message.channel.send(embed=embedi)
        except:
            error = sys.exc_info()[0]
            if error == IndexError:
                haku = { "discordid": discordid }
                naku = { "_id": 0, "osuname": 1 }
                paku = collection.find(haku, naku)
                for osunimi in paku:
                    ousnimi = (f"{osunimi}")
                    oosnimi = ousnimi.split("'")
                    ooonimi = oosnimi[3]
                    print(ooonimi)
                    response = requests.get(f"https://osu.ppy.sh/api/get_user?u={ooonimi}&k=token")
                    data = response.json()
                    for username in data:
                        avatar = username['user_id']
                        embedi = discord.Embed(colour=discord.Colour(0xFFC0CB))
                        embedi.description="moi"
                        embedi.set_author(icon_url=f"https://a.ppy.sh/{avatar}",name="oi")
                        await message.channel.send(embed=embedi)

    elif message.content.startswith(',toposu'):
        osuname = "_".join(message.content.split(" ")[1:])
        response = requests.get(f"https://osu.ppy.sh/api/get_user_best?u={osuname}&k=token")
        data = response.content.decode("utf-8")
        datastream = json.loads(data)
        maps = mapinhaku(datastream)
        osunimi = osuname[0].upper()+osuname[1:]
        embedi = discord.Embed(colour=discord.Colour(0xFFC0CB))
        embedi.set_author(url=f"https://osu.ppy.sh/users/{osuname}", name=f"Top 3 osu! plays for {osunimi}")
        print(maps)
        for i in range(0,3):
            mods = "".join(num_to_mod(datastream[i]['enabled_mods']))
            embedi.add_field(name=f" {emojis[datastream[i]['rank']]}  ({maps[i][0]['difficultyrating']}){maps[i][0]['title']} [{maps[i][0]['version']}] {mods}", value=datastream[i]['pp'], inline=False)
        await message.channel.send(embed=embedi)
        #dataa = f"{data}"f
        #moikka = list(data.split("{"))"enabled_mods"
        #print(datastream[1]['pp'])
        #hei = moikka[1]
        #heippa = moikka[1]['pp']
        #heippa = hei["pp"]
        #embedi = discord.Embed(colour=discord.Colour(0xFFC0CB))
        #embedi.description=f"{heippa}"
        #await message.channel.send(embed=embedi)
        #print(heippa)
    elif ',testi' in message.content:
        command = message.content.split(" ")
        command = command[1:]
        joo = "_"
        osuname = joo.join(command)
        print(osuname)
        osuname = int(osuname)
        oikea = int(min(1000000000, osuname))
        print(oikea)
        if oikea == 1000000000:
            oikea = osuname/1000000000
            oikeest = "{:.1f}".format(oikea)
            print(oikeest)






    elif '.pptesti' in message.content:
        command = message.content.split(" ")
        osuname = command[1]
        pp = requests.get(f"https://osu.ppy.sh/api/get_user?u={osuname}&k=token")
        ppp = pp.json()
        for u in ppp:
            rawpp = int(round(float(u['pp_raw'])))
            print(rawpp)

bot.run('discordtoken')
