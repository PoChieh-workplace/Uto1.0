import discord
from discord.ext import commands
from core.classes import Cog_Extension 

import requests
import facebook
import urllib3
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)


class request(Cog_Extension):
    @commands.command(aliases=['chixing'])
    async def chixingupdate(self,ctx):
        autor = self.bot.get_user(561731559493861398)
        if(autor==ctx.author):
            token = jdata['fbchixingToken']
            took = facebook.GraphAPI(access_token=token, version = 2.12)
            getdata = took.request(f"/{jdata['fbchixingid']}?fields=posts.limit(1)")
            data = getdata['posts']['data'][0]
            time = str(data['created_time'])
            message = data['message']

            url = "https://www.facebook.com/"+ str(data['id'])
            embed=discord.Embed(title=":tada:最新貼文", description=f"{message}\n貼文發布時間：{time}\n [閱讀更多...]({url}) ", color=0x00ff64, timestamp=ctx.message.created_at)
            embed.set_footer(text="discord bot name : Uto , 現在時間:")
            await ctx.send(embed=embed)
        else:
            await ctx.send("❌| 你沒有權限使用此指令")
    @commands.command(aliases=['whshfuck','fuck'])
    async def whshfuckupdate(self,ctx):
        autor = self.bot.get_user(561731559493861398)
        if(autor==ctx.author):
            with open('setting.json','r',encoding='utf8') as jfile:
                jdata = json.load(jfile)
            token = jdata['fbwhshfuckToken']
            took = facebook.GraphAPI(access_token=token, version = 2.12)
            getdata = took.request(f"/{jdata['fbTHREE.KBWHSH']}?fields=posts.limit(1)")
            data = getdata['posts']['data'][0]
            time = str(data['created_time'])
            message = data['message']
            url = "https://www.facebook.com/"+ str(data['id'])
            url2="https://submit.crush.ninja/THREEKBWHSH"
            title = message.split('\n',1)
            url3="https://www.facebook.com/hashtag/"+ title[0][1:]
            embed=discord.Embed(title=f"{title[0]}", description=f"{title[1]}\n發布時間：{time}\n [🔍貼文傳送門I]({url}) \t [🔍貼文傳送II]({url3}) \n [📌我想投稿]({url2})", color=0xff7a7a, timestamp=ctx.message.created_at)
            embed.set_footer(text="code by Po-chieh , 現在時間:")
            await ctx.send(embed=embed)
        else:
            await ctx.send("❌| 你沒有權限使用此指令")
def setup(bot):
    bot.add_cog(request(bot))
