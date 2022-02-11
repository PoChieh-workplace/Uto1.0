import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import math


from cmds.mathonly.Trigonometric import *
from cmds.mathonly.sqrl import *


with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

reply = [['*','x','×','ｘ','＊'],
        ['**','^','︿','＊＊'],
        ['+','＋'],
        ['-','－'],
        ['/','／','÷'],
        ['abs','fabs','ａｂｓ','ｆａｂｓ'],
        ['sin','ｓｉｎ'],
        ['cos','ｃｏｓ'],
        ['tan','ｔａｎ'],
        ['csc','ｃｓｃ'],
        ['sec','ｓｅｃ'],
        ['cot','ｃｏｔ'],
        ['log','ｌｏｇ'],
        ['sqr','ｓｑｒ','sqrt','ｓｑｒｔ'],
        ['abs(','|','｜'],
        ['sqr(','√']
        ]

mathid = ['sin','cos','tan','csc','sec','cot','log','abs','sqr']

def calcu(text):
    text = (text.replace('(','')).replace(')','')
    text = eval(text)
    return str(text)
def get(text):
    text = str(text)
    while(text.find(")")!=-1):
        count = text.find(")")
        while(text[count]!="("):
            count -=1
            if(count==-1):
                return "`❌|括弧放置錯誤`"
        getto = text[count:text.find(")")+1]
        turnto = calcu(getto)
        for i in range(len(mathid)):
            if(text[count-3:].find(mathid[i])==0):
                if(i==0):
                    turnto = str(sin(float(turnto)))
                elif(i==1):
                    turnto = str(cos(float(turnto)))
                elif(i==2):
                    turnto = str(tan(float(turnto)))
                    if(turnto=="tan極端值(錯誤)"):
                        return "`❌|tan極端值(錯誤)`"
                elif(i==3):
                    turnto = str(csc(float(turnto)))
                elif(i==4):
                    turnto = str(sec(float(turnto)))
                elif(i==5):
                    turnto = str(cot(float(turnto)))
                    if(turnto=="cot極端值(錯誤)"):
                        return "`❌|cot極端值(錯誤)`"
                elif(i==6):
                    turnto = str(log(turnto))
                    if(turnto=="對數給予資料錯誤"):
                        return "`❌|對數給予資料錯誤`"
                elif(i==7):
                    turnto = str(fabs(float(turnto)))
                elif(i==8):
                    turnto = str(sqr(float(turnto)))
                    if(turnto == "無法計算虛數"):
                        return "`❌|無法計算虛數`"
                getto = mathid[i]+getto
        text = text.replace(getto,turnto)
    text = eval(text)
    return str(text)


class Math(Cog_Extension):
    @commands.command(aliases=['math'])
    async def calcutor(self,ctx,*,msg):
        try:
            Text = msg
            for i in range(len(reply)):
                    for j in range(1,len(reply[i])):
                        Text = Text.replace(reply[i][j],reply[i][0])
            await ctx.send(str("`"+msg+"`="+get(Text)))
        except:
            await ctx.send("❌| 計算錯誤")
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content.endswith('=') and msg.author != self.bot.user:
            try:
                Text = msg.content
                Text = Text[:-1]
                for i in range(len(reply)):
                        for j in range(1,len(reply[i])):
                            Text = Text.replace(reply[i][j],reply[i][0])
                await msg.channel.send(str(msg.content+get(Text)))
            except:
                await msg.channel.send("❌| 計算錯誤")

def setup(bot):
    bot.add_cog(Math(bot))