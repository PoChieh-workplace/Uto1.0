import datetime,json,asyncio
import discord
from discord.ext import commands
from core.classes import Cog_Extension 
import requests
import facebook
import urllib3

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)



class Loop(Cog_Extension):
    #a = datetime.datetime.now().strftime('%Y %m %d %H')
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        async def time_task():
            await self.bot.wait_until_ready()
            now_time = datetime.datetime.now().strftime('%M')
            timer = int(now_time)

            token = jdata['fbchixingToken']
            took = facebook.GraphAPI(access_token=token, version = 2.12)
            string = f"/{jdata['fbchixingid']}?fields=posts.limit(5)"
            getdata = took.request(string)
            jdata['nowchixingid'] = getdata['posts']['data'][0]['id']

            token = jdata['fbwhshfuckToken']
            took = facebook.GraphAPI(access_token=token, version = 2.12)
            string = f"/{jdata['fbTHREE.KBWHSH']}?fields=posts.limit(5)"
            getdata = took.request(string)
            jdata['nowwhshfuckid'] = getdata['posts']['data'][0]['id']


            with open('setting.json','w',encoding='utf8') as jfile:
                json.dump(jdata,jfile,indent=4)

            while not self.bot.is_closed():
                now_time = int(datetime.datetime.now().strftime('%M'))
                if(now_time!=timer and now_time%15==0):
                    self.channel = self.bot.get_channel(901812737389244436)
                    timer = now_time
                    token = jdata['fbchixingToken']
                    took = facebook.GraphAPI(access_token=token, version = 2.12)
                    string = f"/{jdata['fbchixingid']}?fields=posts.limit(5)"
                    getdata = took.request(string)
                    for i in range(5):
                        data = getdata['posts']['data'][4-i]
                        timeid = str(data['id'])
                        if(timeid == jdata['nowchixingid']):
                            updateid = 4-i
                            break
                        else:
                            updateid = -1
                    jdata['nowchixingid'] = getdata['posts']['data'][0]['id']
                    with open('setting.json','w',encoding='utf8') as jfile:
                        json.dump(jdata,jfile,indent=4)
                    def embed(message,time,url):
                        embed=discord.Embed(title=f":tada:最新貼文", description=f"{message}\n貼文發布時間：{time}\n [閱讀更多...]({url}) ", color=0x00ff64)
                        embed.set_footer(text="discord bot name : Uto")
                        return embed
                    print("chixing："+ str(updateid))
                    if(updateid==-1):
                        for i in range(5):
                            data = getdata['posts']['data'][4-i]
                            message = data['message']
                            time = str(data['created_time'])
                            url = "https://www.facebook.com/"+ str(data['id'])
                            await self.channel.send(embed=embed(message,time,url))
                    elif(updateid==0):
                        pass
                    else:
                        for i in range(updateid):
                            data = getdata['posts']['data'][updateid-i-1]
                            message = data['message']
                            time = str(data['created_time'])
                            url = "https://www.facebook.com/"+ str(data['id'])
                            await self.channel.send(embed=embed(message,time,url))

                    #for 靠北文華
                    self.channel = self.bot.get_channel(910471209525854238)
                    token = jdata['fbwhshfuckToken']
                    took = facebook.GraphAPI(access_token=token, version = 2.12)
                    string = f"/{jdata['fbTHREE.KBWHSH']}?fields=posts.limit(100)"
                    getdata = took.request(string)
                    for i in range(100):
                        data = getdata['posts']['data'][99-i]
                        timeid = str(data['id'])
                        if(timeid == jdata['nowwhshfuckid']):
                            updateid = 99-i
                            break
                        else:
                            updateid = -1
                    jdata['nowwhshfuckid'] = getdata['posts']['data'][0]['id']
                    with open('setting.json','w',encoding='utf8') as jfile:
                        json.dump(jdata,jfile,indent=4)
                    def embed(message,time,url):
                        url2="https://submit.crush.ninja/THREEKBWHSH"
                        title = message.split('\n',1)
                        url3="https://www.facebook.com/hashtag/"+ title[0][1:]
                        embed=discord.Embed(title=f"{title[0]}", description=f"{title[1]}\n發布時間：{time}\n [🔍貼文傳送門I]({url}) \t [🔍貼文傳送II]({url3}) \n [📌我想投稿]({url2})", color=0xff7a7a)
                        embed.set_footer(text="code by Po-chieh")
                        return embed
                    print("whshfuck："+ str(updateid))
                    if(updateid==-1):
                        for i in range(100):
                            data = getdata['posts']['data'][99-i]
                            message = data['message']
                            time = str(data['created_time'])
                            url = "https://www.facebook.com/"+ str(data['id'])
                            await self.channel.send(embed=embed(message,time,url))
                            await asyncio.sleep(1)
                    elif(updateid==0):
                        pass
                    else:
                        for i in range(updateid):
                            data = getdata['posts']['data'][updateid-i-1]
                            message = data['message']
                            time = str(data['created_time'])
                            url = "https://www.facebook.com/"+ str(data['id'])
                            await self.channel.send(embed=embed(message,time,url))
                            await asyncio.sleep(1)
                    await asyncio.sleep(30)
                else:
                    await asyncio.sleep(30)
                    pass

        self.bg_task = self.bot.loop.create_task(time_task())
def setup(bot):
    bot.add_cog(Loop(bot))