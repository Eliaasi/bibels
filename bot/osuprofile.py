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
    if message.content.startswith(',osu'):
        try:
            command = message.content.split(" ")
            command = command[1:]
            joo = "_"
            osuname = joo.join(command)
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

bot.run('token')
