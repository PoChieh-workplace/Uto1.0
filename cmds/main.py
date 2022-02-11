# ping information
import discord
from discord import embeds
from discord.ext import commands
from discord.ext.commands import errors
from discord.ext.commands.core import dm_only
from core.classes import Cog_Extension
import json, asyncio
from fake_useragent import UserAgent
import requests
from datetime import timedelta


with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
with open('command.json','r',encoding='utf8') as jfile:
    command = json.load(jfile)





class Main(Cog_Extension):
    @commands.command(aliases=['pg'])
    async def ping(self,ctx):
        await ctx.send(f"{round(self.bot.latency*1000)}(ms)")

    
    @commands.command(aliases=['time','dly'])
    async def delay(self,ctx,msg):
        try:
            msgid = await ctx.send(f'開始計時 {msg} 秒！')
            await asyncio.sleep(int(msg))
            await ctx.send('時間到！！')
        except:
            await msgid.edit(content = '❌ | 發生錯誤')
    @commands.command(aliases=['dcr'])
    async def dcard(self,ctx,msg):
        req = ""
        ua = UserAgent()
        user_agent = ua.random
        headers = {'user-agent': user_agent}
        text = f"https://www.dcard.tw/service/api/v2/forums/{command[f'dcard{msg}']}/posts?popular=true&limit=20"
        r = requests.get(text,headers=headers)
        js = json.loads(r.text)
        req += f"**目前版類：**`{command[f'dcard{msg}']}`\n🔹🔹🔹🔹🔹🔹🔹🔹\n"
        for i in js:
            new = f"**{i['title']}**\n{i['excerpt']}...更多\n\n前往連結：https://www.dcard.tw/f/{command[f'dcard{msg}']}/p/{i['id']} \n更新時間：`{i['updatedAt']}`\n🔸🔸🔸🔸🔸🔸🔸🔸\n"
            if(len(req+new)>1930):
                break
            req += new
        req += f"\n\n\n變更版面請回覆表情符號\n🥺心情版\t❤️愛情版\t💬閒聊版\n👩女孩版\t🦹‍♂️追星版\t🥳有趣版\n🎀美妝版\t👚穿搭版\t🔧工作版\n😈梗圖版\t🍰美食版"
        msg = await ctx.send(req)
        for i in range(201,212,1):
            await msg.add_reaction(f"{command[f'{i}']}")
    
    @commands.command(aliases=['inf','bot'])
    async def information(self,ctx):
        guild = self.bot.get_guild(871573666637426738) 
        autor = guild.get_member(561731559493861398)
        embed=discord.Embed(title="information:question:", description="Bot資訊", color=0x00e16e)
        embed.add_field(name="born in:baby:", value="2021/08/01", inline=True)
        embed.add_field(name="power by:zap:", value="𝓗𝓾𝓪 𝓣𝓮𝓬𝓱𝓷𝓸𝓵𝓸𝓰𝔂", inline=True)
        embed.add_field(name="Now-:tools: ", value="updataing", inline=True)
        embed.add_field(name="code using", value="python", inline=True)
        embed.set_footer(text=f"written by {autor}",icon_url=autor.avatar_url)
        await ctx.send(embed=embed)
    
    
    @commands.command(aliases=['commands'])
    async def list(self,ctx):
        text =""
        an = int((int(command['count'])+int(command['count'])%2)/2)
        for i in range(101,an+101):
            text += str(f"\n{command[f'{i}']}\n")
        embed=discord.Embed(title="~ :book:指 令 總 覽 ~ command information(1/2)", description=f"{text}\n\n查詢*command以看更多", color=0x00ff64, timestamp=ctx.message.created_at)
        embed.set_footer(text="discord bot name : Uto , 顯示時間:")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('⏩')

    @commands.command(aliases=['helps','cmd','cmds'])
    async def command(self,ctx):
        text =""
        bn = int(command['count'])
        an = int(command['nowpage'])
        text += str(f"{command[f'{an}']}")
        embed=discord.Embed(title=f"~ :book: 指 令 說 明 command information({an}/{bn})~", description=f":level_slider:指令 <必要函數> (非必要函數)\n{text}", color=0x00ff64, timestamp=ctx.message.created_at)
        embed.set_footer(text="discord bot name : Uto , 顯示時間:")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('⬅️')
        await msg.add_reaction('➡️')


    

    
    
    @commands.command(aliases=['ts'])
    async def test(self,ctx,*,msg):
        await ctx.message.delete()
        text = msg
        embed=discord.Embed(title="📜考試", description=f"{text}", color=0xa686fe, timestamp=ctx.message.created_at)
        embed.set_footer(text=f"發起人 {ctx.author},      發起時間:",icon_url=ctx.author.avatar_url)
        msgid = await ctx.send(embed=embed)
        await msgid.add_reaction('✅')


    @commands.command(aliases=['wk'])
    async def work(self,ctx,*,msg):
        await ctx.message.delete()
        text = msg
        embed=discord.Embed(title="📚作業", description=f"{text}", color=0xa686fe, timestamp=ctx.message.created_at)
        embed.set_footer(text=f"發起人 {ctx.author},      發起時間:",icon_url=ctx.author.avatar_url)
        msgid = await ctx.send(embed=embed)
        await msgid.add_reaction('✅')


    @commands.command(aliases=['vt'])
    async def vote(self,ctx,*,msg):
        await ctx.message.delete()
        msg2id = await ctx.send(f"{ctx.message.guild.default_role}")
        text = msg
        embed=discord.Embed(title="📋投票", color=0x1f7b1e, timestamp=ctx.message.created_at)
        embed.add_field(name="內容", value=f"{text}")
        embed.set_footer(text=f"發起人 {ctx.author},      發起時間:",icon_url=ctx.author.avatar_url)
        msgid = await ctx.send(embed=embed)
        await msgid.add_reaction('✅')
        await msgid.add_reaction('❌')


    @commands.command(aliases=['wn'])
    async def warn(self,ctx,id,msg,*,msg2):
        await ctx.message.delete()
        member = ctx.guild.get_member(int(id))
        print(member)
        embed=discord.Embed(title="⚠️警告", description=f"懲處🚫：\n發現成員 `{member}` 違反規定\n原因：{msg2}\nUto判定懲處：{msg}", color=0xa686fe, timestamp=ctx.message.created_at)
        embed.set_footer(text=f"授予審理人 {ctx.author},      發起時間:",icon_url=ctx.author.avatar_url)
        msg = await ctx.send(embed=embed)


    @commands.command(aliases=['s'])
    async def say(self,ctx,*,msg):
        autor = self.bot.get_user(561731559493861398)
        if(autor==ctx.author):
            try:
                await ctx.message.delete()
            except:
                pass
            msg = await ctx.send(msg)
        else:
            await ctx.send("❌| 你沒有權限使用此指令")
        


    @commands.command(aliases=['clean','purge'])
    async def clear(self,ctx,num):
        autor = self.bot.get_user(561731559493861398)
        if(autor==ctx.author):
            await ctx.channel.purge(limit=int(num))
            await ctx.send(f"✅| 成功清除{num}則訊息")
        else:
            await ctx.send("❌| 你沒有權限使用此指令")

    @commands.command(aliases=['temp'])
    async def tp(self,ctx):
        autor = self.bot.get_user(561731559493861398)
        if(autor==ctx.author):
            await ctx.send(f"getit！It's you！{autor}")
        else:
            await ctx.send(f'{autor} {ctx.author}')



    @commands.command(aliases=['nickurl','url'])
    async def nick(self,ctx,msg,url):
        await ctx.message.delete()
        embed=discord.Embed(description=f"[{msg}]({url})")
        msg = await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Main(bot))
