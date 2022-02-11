
#openHa opennormal close reset resetopen

from os import replace
import discord
import requests
from discord.ext import commands
from discord.ext.commands import errors
from core.classes import Cog_Extension
import json
import requests
from datetime import date


with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Server(Cog_Extension):

    @commands.command()
    async def open(self,ctx,*,msg):
        await ctx.message.delete()
        embed=discord.Embed(title=f"~:video_game:伺服器已開啟:tada:~", description=f"{ctx.author}又又又開圖啦!!:tada:", color=0xa686fe, timestamp=ctx.message.created_at)
        embed.add_field(name="今天開的是", value=f"{msg}\n\n如需加入方式請按:raised_back_of_hand:")
        embed.set_footer(text=f"發起人 {ctx.author},      發起時間:",icon_url=ctx.author.avatar_url)
        channel = self.bot.get_channel(int(jdata['PoWelcome']))
        msg = await channel.send(embed=embed)
        await msg.add_reaction('🤚')
        channel = self.bot.get_channel(int(jdata['212game']))
        msg = await channel.send(embed=embed)
        await msg.add_reaction('🤚')

    
    
    @commands.command()
    async def close(self,ctx):
        embed=discord.Embed(title=f"伺服器已關閉", color=0x0197f4)
        channel = self.bot.get_channel(int(jdata['PoWelcome']))
        await channel.send(embed=embed)
        channel = self.bot.get_channel(int(jdata['212game']))
        await channel.send(embed=embed)

    @commands.command()
    async def reset(self,ctx):
        embed=discord.Embed(title=f"伺服器備份中", description=f"地圖備份中，暫時關閉地圖", color=0x0197f4)
        channel = self.bot.get_channel(int(jdata['PoWelcome']))
        await channel.send(embed=embed)
        channel = self.bot.get_channel(int(jdata['Huagame']))
        await channel.send(embed=embed)
        channel = self.bot.get_channel(int(jdata['dreamplay']))
        await channel.send(embed=embed)
        channel = self.bot.get_channel(int(jdata['212game']))
        await channel.send(embed=embed)
    
    @commands.command()
    async def resetopen(self,ctx):
        embed=discord.Embed(title=f"伺服器已重啟", description=f"地圖備份完畢", color=0x0197f4)
        channel = self.bot.get_channel(int(jdata['PoWelcome']))
        await channel.send(embed=embed)
        channel = self.bot.get_channel(int(jdata['Huagame']))
        await channel.send(embed=embed)
        channel = self.bot.get_channel(int(jdata['dreamplay']))
        await channel.send(embed=embed)
        channel = self.bot.get_channel(int(jdata['212game']))
        await channel.send(embed=embed)

    @commands.command(aliases=['mcs'])
    async def mcserver(self,ctx,*,msg):
        text = "https://api.mcsrvstat.us/2/" + f"{msg}"
        tryconnect = requests.get(text)
        json_data = tryconnect.json()
        if(json_data['online']==True):
            if(json_data['motd']['clean']):
                tit = str(json_data['motd']['clean'])
                tit = tit.replace("[",'')
                tit = tit.replace("]",'')
                tit = tit.replace("'",'')
                tit = tit.replace(",",'')
            if(json_data['port']==25565):
                port = " "
            else:
                port = f":{json_data['port']}"
            if(json_data['players']['online']!=0):
                member = 0
                try:
                    member = str(json_data['players']['list'])
                    member = member.replace("[",'')
                    member = member.replace("]",'')
                    member = member.replace("'",'')
                    member = member.replace(",",f'\t')
                    if(json_data['players']['online']>=10):
                        member += "...更多"
                except:
                    pass
            else:
                member = "無人在線"
            text = ""
            if({json_data['hostname']}):
                text += f"\nhostname：{json_data['hostname']}{port}\n"
            if({json_data['version']}):
                text += f"\n版本：{json_data['version']}\n"
            text += f"\n上線人數：{json_data['players']['online']}人\t上限{json_data['players']['max']}人\n"
            if(member):
                text += f"\n名單：{member}"
            embed=discord.Embed(title=f"{tit}",description=f"{text}", color=0xa62b2b)
            embed.set_image(url=f"https://eu.mc-api.net/v3/server/favicon/{msg}")
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"❌ | 無法連接伺服器  `{msg}`")


    @commands.command(aliases=['uuid','mcid','id'])
    async def mcuuid(self,ctx,*,msg):
        message = await ctx.send(f"🔍 | 正在查詢玩家UUID：{msg}")
        try:
            text = "https://api.mojang.com/users/profiles/minecraft/" + f"{msg}"
            tryconnect = requests.get(text)
            json_data = tryconnect.json()
            id = json_data['id']
            name = json_data['name']
            embed=discord.Embed(title=f"✅ | 查詢到玩家UUID：{name}",description=f"{id}", color=0xa62b2b)
            await message.edit(content=None,embed=embed)
        except:
            await message.edit(content=f"❌ | 無法查詢玩家 `{msg}`")
    
    @commands.command(aliases=['playskin','skin','psk'])
    async def mcskin(self,ctx,*,msg):
        message = await ctx.send(f"🔍 | 正在查詢玩家UUID：{msg}")
        try:
            text = "https://api.mojang.com/users/profiles/minecraft/" + f"{msg}"
            tryconnect = requests.get(text)
            json_data = tryconnect.json()
            id = json_data['id']
            name = json_data['name']
            embed=discord.Embed(title=f"✅ | 查詢到玩家UUID：{name}",description=f"{id}", color=0xa62b2b)
            await message.edit(content=None,embed=embed)
        except:
            await message.edit(content=f"❌ | 無法查詢玩家 `{msg}`")


def setup(bot):
    bot.add_cog(Server(bot))
