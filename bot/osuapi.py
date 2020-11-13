import json
import requests
import sys
import asyncio
import discord
from discord.ext import commands
import oppadc

class Osuapi:
    def __init__(self, osuapikey):
        self.key = osuapikey
    
    def beatmap(self, beatmapid, mods):
         osuprofile = requests.get(f"https://osu.ppy.sh/api/get_beatmaps?b={beatmapid}&mods={mods}&k={self.key}").content.decode("utf-8")
         osub = json.loads(osuprofile)
         return osub

    def profile(self, profileid):
        osuprofile = requests.get(f"https://osu.ppy.sh/api/get_user?u={profileid}&k={self.key}").content.decode("utf-8")
        osup = json.loads(osuprofile)
        return osup

    def top(self, profileid):
        osuprofile = requests.get(f"https://osu.ppy.sh/api/get_user_best?u={profileid}&k={self.key}").content.decode("utf-8")
        osut = json.loads(osuprofile)
        return osut

    def recent(self, profileid):
        osuprofile = requests.get(f"https://osu.ppy.sh/api/get_user_recent?u={profileid}&k={self.key}").content.decode("utf-8")
        osur = json.loads(osuprofile)
        return osur

    def count_acc(self, count50, count100, count300, countmiss):
        up50 = count50 * 50; up100 = count100 * 100; up300 = count300 * 300
        acc = (up50+ up100+ up300)/(300*(count50+count100+count300+countmiss))*100
        return float(acc)

    def ppcal(self, mods, acc, r, mdata):
        Map = oppadc.OsuMap(raw_str=mdata)
        PP = Map.getPP(mods, misses=int(r[0]['countmiss']), combo=int(r[0]['maxcombo']), accuracy=float(acc))
        return PP

    def fcpp(self, mods, acc, mdata):
        Map = oppadc.OsuMap(raw_str=mdata)
        FPP = Map.getPP(mods, accuracy=float(acc))
        return FPP

    def peppyshitfix(self, mods, fix):
        if 'HD' in mods:
            fix += 8                           
        elif 'NF' in mods:
            fix += 1                                   
        elif 'FL' in mods:                                      
            fix += 1024                                  
        elif 'SD' in mods:                                      
            fix += 32
        return fix

    def mod(self, number):
            number = int(number)
            mod_list = []

            if number == 0: mod_list.append('NM')
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
            
            
            
