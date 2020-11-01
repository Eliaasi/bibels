import json
import requests
import sys
import asyncio
import discord
from discord.ext import commands

class Osuapi:
    def __init__(self):
        print('moro')
    
    def profile(self, profileid, osuapikey):
        print('1')
        print(osuapikey)
        osuprofile = requests.get(f"https://osu.ppy.sh/api/get_user?u={profileid}&k={osuapikey}").content.decode("utf-8")
        print('2')
        o = json.loads(osuprofile)
        print(o)
        username = o['username']
        rank = o['pp_rank']
        print(username, rank)
        return(username, rank)
            
            
            