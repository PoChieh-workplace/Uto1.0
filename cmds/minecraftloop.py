import json
import discord
from core.classes import Cog_Extension
from discord_components import *
from discord.ext import commands
import asyncio
import requests

class minecraft(Cog_Extension):
    #def __init__(self,*args,**kwargs):
    #    super().__init__(*args,**kwargs)
#
    #    async def time_task():
    #        await self.bot.wait_until_ready()
    #        while not self.bot.is_closed():
    #            with open('minecraft.json','r',encoding='utf8') as jfile:
    #                data = json.load(jfile)
    #            for i in range(len(data)):
    #                text = f"https://api.mcsrvstat.us/2/{data[i]['name']}"
    #                tryconnect = requests.get(text)
    #                json_data = tryconnect.json()
    #                guild = self.bot.get_guild(910150769624358914)
    #                channel = guild.get_channel(910470472938954772)
    #                if(json_data['online']==True):
    #                    if(data[i]['online']==0):
    #                        data[i]['online']=1
    #                        await channel.send(f"▶️ | 伺服 {i['name']} 已開啟")
    #                else:
    #                    if(data[i]['online']==1):
    #                        await channel.send(f"⏸️ | 伺服 {i['name']} 已關閉")
    #                        data[i]['online']=0
    #            with open('minecraft.json','w',encoding='utf8') as jfile:
    #                json.dump(data,jfile,indent=4)
    #            await asyncio.sleep(300)
    #    self.bg_task = self.bot.loop.create_task(time_task())
    pass

def setup(bot):
    bot.add_cog(minecraft(bot))




