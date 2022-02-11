import asyncio
import random
import discord
from discord import channel
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands import errors
from core.classes import Cog_Extension
import json
from fake_useragent import UserAgent
import requests
import datetime

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
with open('command.json','r',encoding='utf8') as jfile:
    command = json.load(jfile)
with open('return.json','r',encoding='utf8') as jfile:
    nid = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        try:
            with open('welcome.json','r',encoding='utf8') as jfile:
                jwelcome = json.load(jfile)
            guild = self.bot.get_guild(member.guild.id)
            channel = self.bot.get_channel(int(jwelcome[f'{member.guild.id}.channel']))
            text = str(f"{jwelcome[f'{member.guild.id}.text']}")
            if "{member}" in text:
                pos=text.find('{member}')
                tmp = text[(pos+8):]
                text = text[:(pos)] + f'{member}' + tmp
            if "{guild}" in text:
                pos=text.find('{guild}')
                tmp = text[(pos+7):]
                text = text[:(pos)] + f'{guild}' + tmp
            embed=discord.Embed(title=text, color=0x0197f4)
            await channel.send(embed=embed)
        except:
            pass

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        try:
            with open('welcome.json','r',encoding='utf8') as jfile:
                jwelcome = json.load(jfile)
            guild = self.bot.get_guild(member.guild.id)
            channel = self.bot.get_channel(int(jwelcome[f'{member.guild.id}.channel']))
            text = str(f"{jwelcome[f'{member.guild.id}.text2']}")
            if "{member}" in text:
                pos=text.find('{member}')
                tmp = text[(pos+8):]
                text = text[:(pos)] + f'{member}' + tmp
            if "{guild}" in text:
                pos=text.find('{guild}')
                tmp = text[(pos+7):]
                text = text[:(pos)] + f'{guild}' + tmp
            embed=discord.Embed(title=text, color=0x0197f4)
            await channel.send(embed=embed)
        except:
            pass

    @commands.Cog.listener()
    async def on_message(self,msg):
        def getid():
            with open('return.json','r',encoding='utf8') as jfile:
                nid = json.load(jfile)
            if msg.author == self.bot.user and msg.content.startswith('Uto'): 
                x= "Uto"
            elif(msg.author != self.bot.user):
                try:
                    x = nid['nickid'][msg.author.name]
                except:
                    tmpid = int(10000*random.random())
                    nid['nickid'][msg.author.name]=tmpid
                    x = nid['nickid'][msg.author.name]
                    with open('return.json','w',encoding='utf8') as jfile:
                        json.dump(nid,jfile,indent=4)
            else:
                return -2
            return x
        for i in jdata['nickchannel']:
            if (int(msg.channel.id)==int(i)):
                x = getid()
                if x==-2:
                    continue
                tmp = msg.content
                if(tmp.find('showme')==-1):
                    await msg.delete()
                    await msg.channel.send('`'+str(x)+'` 說：'+tmp)
        if msg.content.startswith('cf ') and msg.author != self.bot.user:
            guild = self.bot.get_guild(910150769624358914)
            channel = guild.get_channel(910384305518297098)
            #guild = self.bot.get_guild(901812673279303781)
            #channel = guild.get_channel(901812737389244436)
            x = getid()
            if x!=-2:
                tmp = msg.content
                tmp = tmp.replace("cf ","")
                if(tmp.find('showme')==-1):
                    if isinstance(msg.channel, discord.channel.DMChannel):
                        await msg.add_reaction('✅')
                    else:
                        try:
                            await msg.delete()
                        except:
                            pass
                    await channel.send('`'+str(x)+'` 說：'+tmp)
        if msg.content.startswith('cfsearch') and msg.author != self.bot.user:
            x=getid()
            await msg.channel.send(f"✅|你的匿名暱稱為：{x}")

        if msg.content.startswith('cfset') and msg.author != self.bot.user:
            with open('return.json','r',encoding='utf8') as jfile:
                nid = json.load(jfile)
            if(msg.content==('cfset') or msg.content==('cfset ')):
                tmpid = int(10000*random.random())
                nid['nickid'][msg.author.name]=tmpid
                with open('return.json','w',encoding='utf8') as jfile:
                    json.dump(nid,jfile,indent=4)
                await msg.channel.send(f"✅| 成功更換匿名id為{tmpid}")
            else:
                tmpid = msg.content
                tmpid = tmpid.replace("cfset ","")
                nid['nickid'][msg.author.name]=tmpid
                with open('return.json','w',encoding='utf8') as jfile:
                    json.dump(nid,jfile,indent=4)
                await msg.channel.send(f"✅| 成功更換匿名id為{tmpid}")



        if msg.content.startswith('addbot') and msg.author != self.bot.user:
            guild = self.bot.get_guild(871573666637426738) 
            autor = guild.get_member(561731559493861398)
            a = msg.content
            author = msg.author
            guild = msg.guild
            a = a.replace('add','')
            await msg.channel.send(f"✅| 已向 {autor} 發出請求{a} 至 {guild}")
            embed=discord.Embed(title="請求", description=f"`{author}`請求在`{guild}`邀請`{a}`", color=0xff6842)
            await autor.send(embed=embed)

        if msg.content.startswith('talkauthor') and msg.author != self.bot.user:
            guild = self.bot.get_guild(871573666637426738) 
            autor = guild.get_member(561731559493861398)
            a = msg.content
            author = msg.author
            guild = msg.guild
            a = a.replace('talkauthor','')
            await msg.channel.send(f"✅| 已轉達 {autor} `{a}`")
            embed=discord.Embed(title="轉達", description=f"{author}：`{a}`", color=0xff6842)
            await autor.send(embed=embed)

        if msg.content.startswith('getpart') and msg.author != self.bot.user:
            guild = self.bot.get_guild(871573666637426738) 
            autor = guild.get_member(561731559493861398)
            a = msg.content
            author = msg.author
            guild = msg.guild
            a = a.replace('getpart','')
            await msg.channel.send(f"✅| 已請求 `{autor}` 審核 `{author}` 加入`{a}`身分組")
            embed=discord.Embed(title="身分組請求", description=f"`{author}`：請求於 `{guild}` 更改身分組 `{a}`", color=0xff6842)
            await autor.send(embed=embed)


    @commands.Cog.listener()
    async def on_raw_reaction_add(self,data):
        channel = self.bot.get_channel(data.channel_id)
        message = channel.get_partial_message(data.message_id)
        if (str(data.emoji)==(str('🤚')) and (data.member)!=(self.bot.user)):
            user = self.bot.get_user(data.user_id)
            embed=discord.Embed(title="感謝使用Uto", description=f"加入伺服器步驟", color=0xa686fe, timestamp=datetime.datetime.now())
            embed.add_field(name="說明", value=f"由於服主正在研究路由器阜口\n尚須使用hamachi輔助，\n加入帳號:_wpc.pp_\n密碼:_0_\nminecraft伺服位址_pochiehmc.ddns.net_")
            embed.set_footer(text="discord bot name : Uto , 說明時間:")
            msg = await user.send(embed=embed)
        if (str(data.emoji)==(str('⏩')) and (data.member)!=(self.bot.user)):
            text =""
            fr = int((int(command['count'])+int(command['count'])%2)/2)
            an = int(command['count'])
            for i in range(fr+1+100,an+1+100):
                text += str(f"\n{command[f'{i}']}\n")
            embed=discord.Embed(title="~ :book:指 令 總 覽 ~ command information(2/2)", description=f"{text}", color=0x00ff64, timestamp=message.created_at)
            embed.set_footer(text="discord bot name : Uto , 顯示時間:")
            msg = await message.edit(embed=embed)
            await message.clear_reactions()
            await msg.add_reaction('⏪')
        if (str(data.emoji)==(str('⏪')) and (data.member)!=(self.bot.user)):
            text =""
            an = int((int(command['count'])+int(command['count'])%2)/2)
            for i in range(101,an+1+100):
                text += str(f"\n{command[f'{i}']}\n")
            embed=discord.Embed(title="~ :book:指 令 總 覽 ~ command information(1/2)", description=f"{text}", color=0x00ff64, timestamp=message.created_at)
            embed.set_footer(text="discord bot name : Uto , 顯示時間:")
            msg = await message.edit(embed=embed)
            await message.clear_reactions()
            await msg.add_reaction('⏩')
        if (str(data.emoji)==(str('⬅️')) and (data.member)!=(self.bot.user)):
            text =""
            bn = int(command['count'])
            if(int(command['nowpage'])==1):
                command['nowpage'] = str(command['count'])
            else:
                command['nowpage'] = str(int(command['nowpage'])-1)
            with open('command.json','w') as jfile:
                    json.dump(command,jfile)
            an = int(command['nowpage'])
            text += str(f"{command[f'{an}']}")
            embed=discord.Embed(title=f"~ :book: 指 令 說 明 command information({an}/{bn}) ~", description=f":level_slider:指令 <必要函數> (非必要函數)\n{text}", color=0x00ff64, timestamp=message.created_at)
            embed.set_footer(text="discord bot name : Uto , 顯示時間:")
            msg = await message.edit(embed=embed)
            await msg.add_reaction('⬅️')
            await msg.add_reaction('➡️')
        if (str(data.emoji)==(str('➡️')) and (data.member)!=(self.bot.user)):
            text =""
            bn = int(command['count'])
            if(int(command['nowpage'])==int(command['count'])):
                command['nowpage'] = 1
            else:
                command['nowpage'] = str(int(command['nowpage'])+1)
            with open('command.json','w') as jfile:
                    json.dump(command,jfile)
            an = int(command['nowpage'])
            text += str(f"{command[f'{an}']}")
            embed=discord.Embed(title=f"~ :book: 指 令 說 明 command information({an}/{bn}) ~", description=f":level_slider:指令 <必要函數> (非必要函數)\n{text}", color=0x00ff64, timestamp=message.created_at)
            embed.set_footer(text="discord bot name : Uto , 顯示時間:")
            msg = await message.edit(embed=embed)
            await msg.add_reaction('⬅️')
            await msg.add_reaction('➡️')
        #for i in range(201,212,1):
        #    if (str(data.emoji)==(str(command[f'{i}'])) and (data.member)!=(self.bot.user)):
        #        req = ""
        #        text = f"https://www.dcard.tw/service/api/v2/forums/{command[f'dcard{i-200}']}/posts?popular=true&limit=20"
        #        r = requests.get(text)
        #        js = json.loads(r.text)
        #        req += f"**目前版類：**`{command[f'dcard{i-200}']}`\n🔹🔹🔹🔹🔹🔹🔹🔹\n"
        #        for j in js:
        #            new = f"**{j['title']}**\n{j['excerpt']}...閱讀更多\n\n前往連結：https://www.dcard.tw/f/{command[f'dcard{i-200}']}/p/{j['id']} \n更新時間：`{j['updatedAt']}`\n🔸🔸🔸🔸🔸🔸🔸🔸\n"
        #            if(len(req+new)>1800):
        #                break
        #            req += new
        #        req += f"\n\n\n變更版面請回覆表情符號\n🥺心情版\t❤️愛情版\t💬閒聊版\n👩女孩版\t🦹‍♂️追星版\t🥳有趣版\n🎀美妝版\t👚穿搭版\t🔧工作版\n😈梗圖版\t🍰美食版"
        #        msg = await message.edit(content=req)
        #        await message.clear_reactions()
        #        for i in range(201,212,1):
        #            await msg.add_reaction(f"{command[f'{i}']}")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,data):
        if (str(data.emoji)==(str('⬅️')) and (data.member)!=(self.bot.user)):
            channel = self.bot.get_channel(data.channel_id)
            message = channel.get_partial_message(data.message_id)
            text =""
            bn = int(command['count'])
            if(int(command['nowpage'])==1):
                command['nowpage'] = str(command['count'])
            else:
                command['nowpage'] = str(int(command['nowpage'])-1)
            with open('command.json','w') as jfile:
                    json.dump(command,jfile,indent=4)
            an = int(command['nowpage'])
            text += str(f"{command[f'{an}']}")
            embed=discord.Embed(title=f"~ :book: 指 令 說 明 command information({an}/{bn}) ~", description=f":level_slider:指令 <必要函數> (非必要函數)\n{text}", color=0x00ff64, timestamp=message.created_at)
            embed.set_footer(text="discord bot name : Uto , 顯示時間:")
            msg = await message.edit(embed=embed)
            await msg.add_reaction('⬅️')
            await msg.add_reaction('➡️')
        if (str(data.emoji)==(str('➡️')) and (data.member)!=(self.bot.user)):
            channel = self.bot.get_channel(data.channel_id)
            message = channel.get_partial_message(data.message_id)
            text =""
            bn = int(command['count'])
            if(int(command['nowpage'])==int(command['count'])):
                command['nowpage'] = 1
            else:
                command['nowpage'] = str(int(command['nowpage'])+1)
            with open('command.json','w') as jfile:
                    json.dump(command,jfile,indent=4)
            an = int(command['nowpage'])
            text += str(f"{command[f'{an}']}")
            embed=discord.Embed(title=f"~ :book: 指 令 說 明 command information({an}/{bn}) ~", description=f":level_slider:指令 <必要函數> (非必要函數)\n{text}", color=0x00ff64, timestamp=message.created_at)
            embed.set_footer(text="discord bot name : Uto , 顯示時間:")
            msg = await message.edit(embed=embed)
            await msg.add_reaction('⬅️')
            await msg.add_reaction('➡️')


    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if hasattr(ctx.command,'on_error'):
            return
        if isinstance(error,commands.errors.MissingRequiredArgument):
            await ctx.send("❌|指令所輸入資料並不完全，可輸入*command了解更多")
        elif isinstance(error,commands.errors.CommandNotFound):
            pass
            #await ctx.send("❌|查無此指令，可輸入*list了解更多")
        elif isinstance(error,commands.errors.CommandOnCooldown):
            await ctx.send("❌|指令時間限制，請稍後再試")
        else:
            guild = self.bot.get_guild(871573666637426738) 
            autor = guild.get_member(561731559493861398)
            embed=discord.Embed(title=f"❌|發生錯誤", description=f"Error：```{error}```\n已回報開發者", color=0x00e16e)
            embed.set_footer(text=f"開發者 {autor}",icon_url=autor.avatar_url)
            await ctx.send(embed=embed)
            embed=discord.Embed(title=f"❌|發生錯誤", description=f"Error：```{error}```\n發起指令者：{ctx.author}\n群組：{ctx.guild}\n頻道：{ctx.channel}", color=0x00e16e)
            embed.set_footer(text=f"開發者 {autor}",icon_url=autor.avatar_url)
            await autor.send(embed=embed)


def setup(bot):
    bot.add_cog(Event(bot))