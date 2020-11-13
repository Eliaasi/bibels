import discord
from discord.ext import commands


class Embedi:
    def __init__(self):
        print('moro')


    def addfield(self, name1, value1, inline1, embed):
        embed.add_field(name=name1, value=value1, inline=inline1)
        return embed

    def setauthor(self, urlid, name1, embed):
        embed.set_author(url=f"https://osu.ppy.sh/users/{urlid}", icon_url=f"https://a.ppy.sh/{urlid}", name=name1) 
        return embed

    def setthumbnail(self, urlid, embed):
        embed.set_thumbnail(url=f"https://a.ppy.sh/{urlid}")
        return embed

    def osuemb(self, p, top, embed):
        embed.set_author(url=f"https://osu.ppy.sh/users/{p[0]['user_id']}", icon_url=f"https://a.ppy.sh/{p[0]['user_id']}", name=f"{p[0]['username']} #{p[0]['pp_rank']} ({p[0]['country']}#{p[0]['pp_country_rank']})")
        embed.set_thumbnail(url=f"https://a.ppy.sh/{p[0]['user_id']}")
        embed.add_field(name="Playcount", value=p[0]['playcount'], inline=True)
        embed.add_field(name="Top Play", value=f"{int(round(float(top[0]['pp'])))}pp", inline=True)
        embed.add_field(name="Accuracy", value=f"{float(p[0]['accuracy']):.2f}%", inline=True)
        embed.add_field(name="Total pp", value=int(round(float(p[0]['pp_raw']))), inline=True)
        embed.add_field(name="Score", value=f"{int(p[0]['ranked_score'])/1000000000:.1f}B", inline=True)
        embed.add_field(name="Playtime", value=f"{int(int(p[0]['total_seconds_played'])/3600)}h", inline=True)
        return embed

    def recemb(self, p, r, b, mods, acc, pp, fpp, emojis, embed):
        embed.set_author(url=f"https://osu.ppy.sh/users/{p[0]['user_id']}", icon_url=f"https://a.ppy.sh/{p[0]['user_id']}", name=f"{p[0]['username']} #{p[0]['pp_rank']} ({p[0]['country']}#{p[0]['pp_country_rank']})")
        embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{b[0]['beatmapset_id']}.jpg")
        embed.add_field(name=f"{b[0]['artist']} - {b[0]['title']}\nAcc: {acc:.2f}% {r[0]['maxcombo']}/{b[0]['max_combo']}x [{float(b[0]['difficultyrating']):.2f}*] +{mods}", value=f"{emojis[r[0]['rank']]} Score: {r[0]['score']} [{r[0]['count300']}\{r[0]['count100']}\{r[0]['count50']}\{r[0]['countmiss']}] \n**{pp:.2f}pp, {fpp:.2f}pp if fc.**")
        return embed

