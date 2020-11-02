import json
import requests
import sys
import asyncio
import discord
from discord.ext import commands

class Osuapi:
    def __init__(self, osuapikey):
        self.key = osuapikey
    
    def profile(self, profileid):
        osuprofile = requests.get(f"https://osu.ppy.sh/api/get_user?u={profileid}&k={self.key}").content.decode("utf-8")
        osup = json.loads(osuprofile)
        return osup

    def top(self, profileid):
        osuprofile = requests.get(f"https://osu.ppy.sh/api/get_user_best?u={profileid}&k={self.key}").content.decode("utf-8")
        osut = json.loads(osuprofile)
        return osut
            
            
            
