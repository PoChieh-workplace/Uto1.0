
#team range

import discord
from discord.ext import commands
from discord.ext.commands import errors
from core.classes import Cog_Extension
import json
import random

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
with open('welcome.json','r',encoding='utf8') as jfile:
    welcome = json.load(jfile)
with open('command.json','r',encoding='utf8') as jfile:
    command = json.load(jfile)


class Player(Cog_Extension):
    @commands.command(aliases=['tm'])
    async def team(self,ctx,msg,msg2):
        online=[]
        count= 0
        test=""
        for member in ctx.guild.members:
            if str(member.status) == 'online' and member.bot == False:
                test += f"{member}\n"
                online.append(member.name)
                count = count+1
        embed=discord.Embed(title=f":one: 確認在線名單",description=f"{test}", color=0xfef60b)
        await ctx.send(embed=embed)
        if int(msg)*int(msg2) > count:
            embed=discord.Embed(title=f"❌| 人數不足", color=0xff0000)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=f":two: 即將進行分組", color=0xff0000)
            await ctx.send(embed=embed)

            for c in range(int(msg)):
                all = random.sample(online, k=(int(msg2)))
                text = str(all)
                for j in all:
                    online.remove(j)
                text = text.replace("['"," ")
                text = text.replace("']"," ,")
                embed=discord.Embed(title=f":pushpin: 第{c+1}小隊:"+ text, color=0x8afff7)
                await ctx.send(embed=embed)

    @commands.command(aliases=['r'])
    async def range(self,ctx):
        player=[]
        count= 0
        test=""
        for member in ctx.guild.members:
            if str(member.status) == 'online' and member.bot == False:
                test += f"{member}\n"
                player.append(member.name)
                count = count+1
        all = random.sample(player, k=1)
        text = str(all)
        text = text.replace("['"," ")
        text = text.replace("']"," ,")
        embed=discord.Embed(title=f":pushpin: 就是你了"+ text, color=0x8afff7)
        await ctx.send(embed=embed)

    @commands.command(aliases=['jc'])
    async def joinconnect(self,ctx,*,msg):
        guild = self.bot.get_guild(ctx.guild.id)
        member = ctx.guild.get_member(561731559493861398)
        channels = self.bot.get_channel(ctx.channel.id)
        welcome[f'{ctx.guild.id}.channel'] = int(ctx.channel.id)
        welcome[f'{ctx.guild.id}.text'] = msg
        with open('welcome.json','w') as jfile:
                json.dump(welcome,jfile)
        await ctx.send(f"✅| 已連接 歡迎訊息 至 {channels}")
        await member.send(f'新的歡迎文:\n```"{ctx.guild.id}.channel":"{int(ctx.channel.id)}","{ctx.guild.id}.text":"{msg}"```')

    @commands.command(aliases=['lc'])
    async def leaveconnect(self,ctx,*,msg):
        guild = self.bot.get_guild(ctx.guild.id)
        member = ctx.guild.get_member(561731559493861398)
        channels = self.bot.get_channel(ctx.channel.id)
        welcome[f'{ctx.guild.id}.channel'] = int(ctx.channel.id)
        welcome[f'{ctx.guild.id}.text2'] = msg
        with open('welcome.json','w') as jfile:
                json.dump(welcome,jfile)
        await ctx.send(f"✅| 已連接 離開訊息 至 {channels}")
        await member.send(f'新的離開文:\n```"{ctx.guild.id}.channel":"{int(ctx.channel.id)}","{ctx.guild.id}.text2":"{msg}"```')

        
def setup(bot):
    bot.add_cog(Player(bot))
