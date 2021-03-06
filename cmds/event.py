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
                    await msg.channel.send('`'+str(x)+'` ??????'+tmp)
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
                        await msg.add_reaction('???')
                    else:
                        try:
                            await msg.delete()
                        except:
                            pass
                    await channel.send('`'+str(x)+'` ??????'+tmp)
        if msg.content.startswith('cfsearch') and msg.author != self.bot.user:
            x=getid()
            await msg.channel.send(f"???|????????????????????????{x}")

        if msg.content.startswith('cfset') and msg.author != self.bot.user:
            with open('return.json','r',encoding='utf8') as jfile:
                nid = json.load(jfile)
            if(msg.content==('cfset') or msg.content==('cfset ')):
                tmpid = int(10000*random.random())
                nid['nickid'][msg.author.name]=tmpid
                with open('return.json','w',encoding='utf8') as jfile:
                    json.dump(nid,jfile,indent=4)
                await msg.channel.send(f"???| ??????????????????id???{tmpid}")
            else:
                tmpid = msg.content
                tmpid = tmpid.replace("cfset ","")
                nid['nickid'][msg.author.name]=tmpid
                with open('return.json','w',encoding='utf8') as jfile:
                    json.dump(nid,jfile,indent=4)
                await msg.channel.send(f"???| ??????????????????id???{tmpid}")



        if msg.content.startswith('addbot') and msg.author != self.bot.user:
            guild = self.bot.get_guild(871573666637426738) 
            autor = guild.get_member(561731559493861398)
            a = msg.content
            author = msg.author
            guild = msg.guild
            a = a.replace('add','')
            await msg.channel.send(f"???| ?????? {autor} ????????????{a} ??? {guild}")
            embed=discord.Embed(title="??????", description=f"`{author}`?????????`{guild}`??????`{a}`", color=0xff6842)
            await autor.send(embed=embed)

        if msg.content.startswith('talkauthor') and msg.author != self.bot.user:
            guild = self.bot.get_guild(871573666637426738) 
            autor = guild.get_member(561731559493861398)
            a = msg.content
            author = msg.author
            guild = msg.guild
            a = a.replace('talkauthor','')
            await msg.channel.send(f"???| ????????? {autor} `{a}`")
            embed=discord.Embed(title="??????", description=f"{author}???`{a}`", color=0xff6842)
            await autor.send(embed=embed)

        if msg.content.startswith('getpart') and msg.author != self.bot.user:
            guild = self.bot.get_guild(871573666637426738) 
            autor = guild.get_member(561731559493861398)
            a = msg.content
            author = msg.author
            guild = msg.guild
            a = a.replace('getpart','')
            await msg.channel.send(f"???| ????????? `{autor}` ?????? `{author}` ??????`{a}`?????????")
            embed=discord.Embed(title="???????????????", description=f"`{author}`???????????? `{guild}` ??????????????? `{a}`", color=0xff6842)
            await autor.send(embed=embed)


    @commands.Cog.listener()
    async def on_raw_reaction_add(self,data):
        channel = self.bot.get_channel(data.channel_id)
        message = channel.get_partial_message(data.message_id)
        if (str(data.emoji)==(str('????')) and (data.member)!=(self.bot.user)):
            user = self.bot.get_user(data.user_id)
            embed=discord.Embed(title="????????????Uto", description=f"?????????????????????", color=0xa686fe, timestamp=datetime.datetime.now())
            embed.add_field(name="??????", value=f"???????????????????????????????????????\n????????????hamachi?????????\n????????????:_wpc.pp_\n??????:_0_\nminecraft????????????_pochiehmc.ddns.net_")
            embed.set_footer(text="discord bot name : Uto , ????????????:")
            msg = await user.send(embed=embed)
        if (str(data.emoji)==(str('???')) and (data.member)!=(self.bot.user)):
            text =""
            fr = int((int(command['count'])+int(command['count'])%2)/2)
            an = int(command['count'])
            for i in range(fr+1+100,an+1+100):
                text += str(f"\n{command[f'{i}']}\n")
            embed=discord.Embed(title="~ :book:??? ??? ??? ??? ~ command information(2/2)", description=f"{text}", color=0x00ff64, timestamp=message.created_at)
            embed.set_footer(text="discord bot name : Uto , ????????????:")
            msg = await message.edit(embed=embed)
            await message.clear_reactions()
            await msg.add_reaction('???')
        if (str(data.emoji)==(str('???')) and (data.member)!=(self.bot.user)):
            text =""
            an = int((int(command['count'])+int(command['count'])%2)/2)
            for i in range(101,an+1+100):
                text += str(f"\n{command[f'{i}']}\n")
            embed=discord.Embed(title="~ :book:??? ??? ??? ??? ~ command information(1/2)", description=f"{text}", color=0x00ff64, timestamp=message.created_at)
            embed.set_footer(text="discord bot name : Uto , ????????????:")
            msg = await message.edit(embed=embed)
            await message.clear_reactions()
            await msg.add_reaction('???')
        if (str(data.emoji)==(str('??????')) and (data.member)!=(self.bot.user)):
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
            embed=discord.Embed(title=f"~ :book: ??? ??? ??? ??? command information({an}/{bn}) ~", description=f":level_slider:?????? <????????????> (???????????????)\n{text}", color=0x00ff64, timestamp=message.created_at)
            embed.set_footer(text="discord bot name : Uto , ????????????:")
            msg = await message.edit(embed=embed)
            await msg.add_reaction('??????')
            await msg.add_reaction('??????')
        if (str(data.emoji)==(str('??????')) and (data.member)!=(self.bot.user)):
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
            embed=discord.Embed(title=f"~ :book: ??? ??? ??? ??? command information({an}/{bn}) ~", description=f":level_slider:?????? <????????????> (???????????????)\n{text}", color=0x00ff64, timestamp=message.created_at)
            embed.set_footer(text="discord bot name : Uto , ????????????:")
            msg = await message.edit(embed=embed)
            await msg.add_reaction('??????')
            await msg.add_reaction('??????')
        #for i in range(201,212,1):
        #    if (str(data.emoji)==(str(command[f'{i}'])) and (data.member)!=(self.bot.user)):
        #        req = ""
        #        text = f"https://www.dcard.tw/service/api/v2/forums/{command[f'dcard{i-200}']}/posts?popular=true&limit=20"
        #        r = requests.get(text)
        #        js = json.loads(r.text)
        #        req += f"**???????????????**`{command[f'dcard{i-200}']}`\n????????????????????????????????\n"
        #        for j in js:
        #            new = f"**{j['title']}**\n{j['excerpt']}...????????????\n\n???????????????https://www.dcard.tw/f/{command[f'dcard{i-200}']}/p/{j['id']} \n???????????????`{j['updatedAt']}`\n????????????????????????????????\n"
        #            if(len(req+new)>1800):
        #                break
        #            req += new
        #        req += f"\n\n\n?????????????????????????????????\n?????????????\t???????????????\t?????????????\n?????????????\t??????????????????????\t?????????????\n?????????????\t?????????????\t?????????????\n?????????????\t?????????????"
        #        msg = await message.edit(content=req)
        #        await message.clear_reactions()
        #        for i in range(201,212,1):
        #            await msg.add_reaction(f"{command[f'{i}']}")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,data):
        if (str(data.emoji)==(str('??????')) and (data.member)!=(self.bot.user)):
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
            embed=discord.Embed(title=f"~ :book: ??? ??? ??? ??? command information({an}/{bn}) ~", description=f":level_slider:?????? <????????????> (???????????????)\n{text}", color=0x00ff64, timestamp=message.created_at)
            embed.set_footer(text="discord bot name : Uto , ????????????:")
            msg = await message.edit(embed=embed)
            await msg.add_reaction('??????')
            await msg.add_reaction('??????')
        if (str(data.emoji)==(str('??????')) and (data.member)!=(self.bot.user)):
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
            embed=discord.Embed(title=f"~ :book: ??? ??? ??? ??? command information({an}/{bn}) ~", description=f":level_slider:?????? <????????????> (???????????????)\n{text}", color=0x00ff64, timestamp=message.created_at)
            embed.set_footer(text="discord bot name : Uto , ????????????:")
            msg = await message.edit(embed=embed)
            await msg.add_reaction('??????')
            await msg.add_reaction('??????')


    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if hasattr(ctx.command,'on_error'):
            return
        if isinstance(error,commands.errors.MissingRequiredArgument):
            await ctx.send("???|?????????????????????????????????????????????*command????????????")
        elif isinstance(error,commands.errors.CommandNotFound):
            pass
            #await ctx.send("???|???????????????????????????*list????????????")
        elif isinstance(error,commands.errors.CommandOnCooldown):
            await ctx.send("???|????????????????????????????????????")
        else:
            guild = self.bot.get_guild(871573666637426738) 
            autor = guild.get_member(561731559493861398)
            embed=discord.Embed(title=f"???|????????????", description=f"Error???```{error}```\n??????????????????", color=0x00e16e)
            embed.set_footer(text=f"????????? {autor}",icon_url=autor.avatar_url)
            await ctx.send(embed=embed)
            embed=discord.Embed(title=f"???|????????????", description=f"Error???```{error}```\n??????????????????{ctx.author}\n?????????{ctx.guild}\n?????????{ctx.channel}", color=0x00e16e)
            embed.set_footer(text=f"????????? {autor}",icon_url=autor.avatar_url)
            await autor.send(embed=embed)


def setup(bot):
    bot.add_cog(Event(bot))