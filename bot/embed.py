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

