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
        osuprofile = requests.get(f"https://osu.ppy.sh/api/get_user?u={profileid}&k={osuapikey}").content.decode("utf-8")
        o = json.loads(osuprofile)
        username = o[0]['username']
        rank = o[0]['pp_rank']
        return username, rank;
            
            
            
