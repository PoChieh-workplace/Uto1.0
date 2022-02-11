import discord
from discord.ext import commands
from core.classes import Cog_Extension
from discord_components import *
from discord import Client, guild, Embed
import json,random
import asyncio


class WHSH(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content.startswith('add 可以澀澀') and msg.author != self.bot.user:
            embed = discord.Embed(title=f"🔧請求申請 可以澀澀", description="1️⃣ .  確保您已年滿18歲\n\n2️⃣ . 因應 discord 條款規定，禁止幼童色情\n例如：羅莉、正太...等\n\n3️⃣ 以不影響他人為原則，請勿在\n非限制級頻道中傳送色情相關內容，\n否則依伺服校規處置\n\n👇🏻 請於60秒內,確定閱讀", color=0xb494ff)
            component = [Button(style=ButtonStyle.blue,id="accept", label="✅ 我同意")]
            rp = "✅ | 成功新增 可以澀澀 身分組"
            rpnoon = "❌ | 新增 可以澀澀 身分組發生錯誤"
            notin = "❌ | 你不在該身分組的群組裡"
            timeout = "❌ | 超時(tineout)，回應無效"
            send = await msg.channel.send(embed=embed,components=component)
            def check(m):
                return m.channel == msg.channel
            try:
                interaction = await self.bot.wait_for("button_click",check=check)
            except asyncio.TimeoutError:
                await send.delete()
                await msg.channel.send(content=timeout)
            else:
                guild = self.bot.get_guild(910150769624358914)
                role = guild.get_role(913649078582272030)
                author = guild.get_member(msg.author.id)
                if author != None:
                    await author.add_roles(role)
                    await interaction.respond(content=rp)
                else:
                    await msg.channel.send(content=notin)




    @commands.command(aliases=['whsh','whhelp'])
    async def whshhelp(self,ctx):
        guild = self.bot.get_guild(910150769624358914)
        guname = guild.name
        whshhelp1 = [
            [Button(style=ButtonStyle.green,id="whsh1",emoji="🔍",label=f"{guname}伺服導引"),
            Button(style=ButtonStyle.green,id="whsh2",emoji="🤖",label="我想邀請機器人")],
            [Button(style=ButtonStyle.green,id="whsh3",emoji="❤️‍🔥",label=f"給予{guname}邀請連結"),
            Button(style=ButtonStyle.blue,id="whsh5",emoji="🧑🏻‍🏫",label=f"我是老師"),
            Button(style=ButtonStyle.red,id="whsh4",emoji="❓",label="其他")]
        ]
        whshlead = [
            [Button(style=ButtonStyle.blue,id="signin", label="🥐註冊組"),
            Button(style=ButtonStyle.blue,id="whshlove", label="💓暈船文華")],
            [Button(style=ButtonStyle.blue,id="whshannouce", label="📢宣傳文華"),
            Button(style=ButtonStyle.blue,id="whshfuck", label="🎈靠北文華")],
            [Button(style=ButtonStyle.blue,id="whshmusic", label="🎶𝒎𝒖𝒔𝒊𝒄🎶"),
            Button(style=ButtonStyle.red,id="whshleadall", label="😈我要所有")]
        ]

        #導引-1
        whshteacheruse = [
            [Button(style=ButtonStyle.blue,id="trcomputer", label="💻電腦導引"),
            Button(style=ButtonStyle.blue,id="trphone", label="📱手機導引")]
        ]

        #導引-電腦
        trcomputer = [
            [Button(style=ButtonStyle.blue,id="comset", label="🔧基本設置(必要)"),
            Button(style=ButtonStyle.blue,id="touse", label="❓如何使用")],
            [Button(style=ButtonStyle.blue,id="comother", label="🎈通知設定"),
            Button(style=ButtonStyle.blue,id="tofind", label="🔍想探索更多")]
        ]
        comset = "💓感謝老師使用 Whsh & Discord 請進行以下步驟\n\n1.請點選左側文字頻道 <#911530663159676948> 詳閱規則\n\n2.選擇文字頻道 <#911520540756410429>\n 將會看到一則訊息，點擊下方 🧑🏻‍🏫 符號，\n 使此文華系統得知您為老師"
        comother = f"由於本群訊息流通量大，為避免打擾老師，\n可進行以下步驟精簡通知\n\n1.點擊左上角群組名 {guname} \n2.點擊 `通知` \n3.選擇 `只有@memtion` >>>完成"
        

        #導引-手機
        trphone = [
            [Button(style=ButtonStyle.blue,id="phoneset", label="🔧基本設置(必要)"),
            Button(style=ButtonStyle.blue,id="touse", label="❓如何使用")],
            [Button(style=ButtonStyle.blue,id="phoneother", label="🎈通知設定"),
            Button(style=ButtonStyle.blue,id="tofind", label="🔍想探索更多")]
        ]

        phoneset = "💓感謝老師使用 Whsh & Discord 請進行以下步驟\n\n1.請將螢幕向左滑，將顯示一條列表，點選 <#911530663159676948> 詳閱規則\n\n2.點擊文字頻道 <#911520540756410429>\n 將會看到一則訊息，點擊下方 🧑🏻‍🏫 符號，\n 使此文華系統得知您為老師"
        phoneother = f"由於本群訊息流通量大，為避免打擾老師，\n可進行以下步驟精簡通知\n\n1.左滑後點擊群組名 {guname} \n2.點擊 `通知` \n3.選擇 `只有@memtion` >>>完成"

        tofind = f"回到最上方訊息，並選擇 `🔍{guname} 伺服導引` 按鈕"
        touse = [
            [Button(style=ButtonStyle.blue,id="tritd", label="🏷️軟體介紹"),
            Button(style=ButtonStyle.blue,id="anous", label="📢公告全校")],
            [Button(style=ButtonStyle.blue,id="message", label="💬我想留言"),
            Button(style=ButtonStyle.blue,id="voicechat", label="🔊我想語音")]
        ]
        tritd = "discord 主要特色為分流聊天，可避免話題混亂\n頁面左側(手機左滑)為顯示所有類別與設定，\n頁面右側(手機右滑)為成員列表"
        anous = "左側(左滑後)點擊文字頻道 <#912637208991793162>，\n傳送公告時可使用 `@everyone` 來提及所有人"
        message = "左測(左滑後)列表中，\n擁有 # 符號的項目皆為文字頻道，各項目皆為獨立區域\n，點擊想要的項目後，即可在下方留言"
        voicechat = "左測(左滑後)列表中，\n擁有 🔊 符號的項目皆為語音頻道，\n同項目之群體皆可聽到彼此聲音\n，點擊後即可進入。電腦左下方將顯示語音設定。"

        whsh2text = ("💬請將機器人邀請連結貼給管管，並煩請耐心等待審核，\n🤖若要邀請自製機器人，請附加上機器人程式碼")
        invitembed = discord.Embed(title=f"{guname}邀請連結", description="https://discord.gg/dghmdEhDvv", color=0xb494ff)
        whsh4text = ("❓歡迎與 <@&910351390122078239> 提出呦，可以是點子，也可以是其他想說的話")


        signintext = ("可 在 <#911520540756410429> 中 選 擇 想 要 的 主 題 🔧 ,\n我們會提供相對應的頻道,\n使用方式：只要點擊身分組對應的符號即可新增\n```ex:點擊🧑🏻‍🏫可取得 <@&911524075359305749> ```\n\n如果反悔選擇，再點擊一次符號即可刪除❌")
        lovetext = ("<#910384305518297098> 為匿名系統，使用指令如下：\n\n1. 💬 直接在 💓暈船文華 上留言\n\n監獄長會替換留言，\n但會有因電腦延遲 產生0.1秒露頭的風險 ouo ，\n而且如果開發者(我)在進行更新時，\n你就會完全露頭 \n\n\n2.💬  私聊 <@871569806439088208> 或\n其他有 <@871569806439088208> 在的伺服器，\n使用指令：\n\ncf (留言)  或  *cf (留言) \n✅ 能避免露頭風險的 傳送訊息至版面\n\n\ncfset (暱稱)  或 *cfset (暱稱) 或 *cs (暱稱)\n:thonk: 如果暱稱不慎外漏，可更改你的匿稱\n若此指令不填暱稱，會以隨機數字替代\n p.s.我相信你不會在暈船版面用此指令(雖然可以用\n\ncfsearch  或  *cfsearch 或  *cfs\n查詢當前使用暱稱\n\n\nBeta版，如有bug請使用 \ntalkauthor (錯誤內容)  指令回報我，謝謝你")
        annoucetext = ("<#912637208991793162> 可宣傳許 **除了有涉及:underage:相關以外**的任何內容，可以是 圖片 或 文字說明\n也可使用投票指令 :inbox_tray: ，\n使用方式： `&poll <標題> <選項1> <選項2> [選項3]...`\n至少需要兩個選項 最多18個選項\n選項不可重複，如果選項中有 空白鍵使用 請冠上 `""`\nex: \n```\n&poll 服主如何 很帥 超帥 還是很帥\n&poll 今天的早餐吃什麼? \"西瓜 牛奶\" 蛋 熱狗```")
        whshfuck = ("<#910471209525854238> 💻開發中，\n之後將會在此更新 facebook靠杯文華貼文，\n正在等待小編授予權限")
        musictext = "可於 <#910386094846136341> 點歌，\n音樂指令 `&p 網址(關鍵字)`"
        whshleadall = ("開發者不想寫了，QQ求幫")

        embed=discord.Embed(title="伺服引導", description="**請問我可以幫你甚麼**，請點選下方按鈕👇🏻", color=0xff0000)
        await ctx.send(
            embed=embed,
            components = whshhelp1
        )
        if not isinstance(ctx.channel, discord.channel.DMChannel):
            while True:
                interaction = await self.bot.wait_for("button_click")
                if interaction.channel == ctx.channel:
                    responceid = interaction.component.id
                    if(responceid == "whsh1"):
                        if(ctx.guild.id==910150769624358914):
                            await interaction.respond(content=f"伺服引導",components = whshlead)
                        else:
                            await interaction.respond(content=f"❌| 此指令不是用於此")
                    if(responceid == "signin"):
                        await interaction.respond(content=signintext)
                    if(responceid == "whshlove"):
                        await interaction.respond(content=lovetext)
                    if(responceid == "whshannouce"):
                        await interaction.respond(content=annoucetext)
                    if(responceid == "whshfuck"):
                        await interaction.respond(content=whshfuck)
                    if(responceid == "whshmusic"):
                        await interaction.respond(content=musictext)
                    if(responceid == "whshleadall"):
                        await interaction.respond(content=whshleadall)

                    
                    if(responceid == "whsh2"):
                        await interaction.respond(content=whsh2text)
                    if(responceid == "whsh3"):
                        await interaction.respond(embed=invitembed)
                    if(responceid == "whsh4"):
                        await interaction.respond(content=whsh4text)

                    
                    if(responceid == "whsh5"):
                        if(ctx.guild.id==910150769624358914):
                            await interaction.respond(content=f"選擇使用工具🔧",components = whshteacheruse)
                        else:
                            await interaction.respond(content=f"❌| 此指令不是用於此")


                    if(responceid == "trcomputer"):
                        await interaction.respond(content=f"電腦導引",components = trcomputer)
                    if(responceid == "comset"):
                        await interaction.respond(content=f"{comset}")
                    if(responceid == "comuse"):
                        await interaction.respond(content=f"功能如下🔧",components = touse)

                    if(responceid == "trphone"):
                        await interaction.respond(content=f"手機導引",components = trphone)
                    if(responceid == "phoneset"):
                        await interaction.respond(content=phoneset)
                    if(responceid == "touse"):
                        await interaction.respond(content=f"❓如何使用",components = touse)
                    if(responceid == "tritd"):
                        await interaction.respond(content=tritd)
                    if(responceid == "anous"):
                        await interaction.respond(content=anous)
                    if(responceid == "message"):
                        await interaction.respond(content=message)
                    if(responceid == "voicechat"):
                        await interaction.respond(content=voicechat)
                    if(responceid == "phoneother"):
                        await interaction.respond(content=phoneother)
                    if(responceid == "comother"):
                        await interaction.respond(content=comother)
                    if(responceid == "tofind"):
                        await interaction.respond(content=tofind)

    @commands.command(aliases=['cs'])
    async def cfset(self,ctx,msg):
        with open('return.json','r',encoding='utf8') as jfile:
                nid = json.load(jfile)
        tmpid = msg
        nid['nickid'][ctx.author.name]=tmpid
        with open('return.json','w',encoding='utf8') as jfile:
            json.dump(nid,jfile,indent=4)
        await ctx.send(f"✅| 成功更換匿名id為{tmpid}")
    @cfset.error
    async def cfset_error(self,ctx,error):
        if(isinstance(error,commands.errors.MissingRequiredArgument)):
            with open('return.json','r',encoding='utf8') as jfile:
                nid = json.load(jfile)
            tmpid = int(10000*random.random())
            nid['nickid'][ctx.author.name]=tmpid
            with open('return.json','w',encoding='utf8') as jfile:
                json.dump(nid,jfile,indent=4)
            await ctx.send(f"✅| 成功更換匿名id為{tmpid}")

    @commands.command()
    async def cf(self,ctx,*,msg):
        with open('return.json','r',encoding='utf8') as jfile:
            nid = json.load(jfile)
        guild = self.bot.get_guild(910150769624358914)
        channel = guild.get_channel(910384305518297098)
        try:
            x = nid['nickid'][ctx.author.name]
        except:
            tmpid = int(10000*random.random())
            nid['nickid'][ctx.author.name]=tmpid
            x = nid['nickid'][ctx.author.name]
            with open('return.json','w',encoding='utf8') as jfile:
                json.dump(nid,jfile,indent=4)
        if x!=-2:
            tmp = msg
            if(tmp.find('showme')==-1):
                if isinstance(ctx.channel, discord.channel.DMChannel):
                    await ctx.message.add_reaction('✅')
                else:
                    try:
                        await ctx.message.delete()
                    except:
                        pass
                await channel.send('`'+str(x)+'` 說：'+tmp)
    @commands.command(aliases=['gcf'])
    async def getcf(self,ctx):
        autor = self.bot.get_user(561731559493861398)
        if(autor==ctx.author):
            with open('return.json','r',encoding='utf8') as jfile:
                nid = json.load(jfile)
            x = nid['nickid']
            await ctx.send(f"```{x}```")
        else:
            await ctx.send("❌| 你沒有權限使用此指令")

    @commands.command(aliases=['cfs'])
    async def cfsearch(self,ctx):
        with open('return.json','r',encoding='utf8') as jfile:
            nid = json.load(jfile)
        guild = self.bot.get_guild(910150769624358914)
        channel = guild.get_channel(910384305518297098)
        #guild = self.bot.get_guild(901812673279303781)
        #channel = guild.get_channel(901812737389244436)
        try:
            x = nid['nickid'][ctx.author.name]
        except:
            tmpid = int(10000*random.random())
            nid['nickid'][ctx.author.name]=tmpid
            x = nid['nickid'][ctx.author.name]
            with open('return.json','w',encoding='utf8') as jfile:
                json.dump(nid,jfile,indent=4)
        await ctx.send(f"✅|你的匿名暱稱為：{x}")
def setup(bot):
    bot.add_cog(WHSH(bot))