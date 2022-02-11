import discord
from discord.ext import commands
import json
import os
from discord.ext.commands.help import HelpCommand
from discord_components import *

from cmds.mathonly.Trigonometric import *
from cmds.mathonly.sqrl import *

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
with open('command.json','r',encoding='utf8') as jfile:
    cmds = json.load(jfile)


class CustonmHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()
    
    async def send_bot_help(self, mapping):
        
        embed=discord.Embed(title="~ :book:指 令 教 學 文 件 ~", description="ヽ(ヅ)ノ感謝使用Uto-212class,\n希望能幫助到你!有任何問題都可以查看 [說明文件](https://utoclass.000webhostapp.com/) 哦!", color=0x00ff64)
        embed.set_author(name="Uto-212class",icon_url= bot.user.avatar_url) 
        embed.set_footer(text="Discord bot name : Uto , Code by：Po-Chieh")
        msg = await self.get_destination().send(embed=embed)
        #for cog in mapping:
        #    await self.get_destination().send(f'{cog.qualified_name}:{[command.name for command in mapping[cog]]}')


    async def send_cog_help(self, cog):
        await self.get_destination().send(f'{cog.qualified_name}:{[command.name for command in cog.get_commands()]}')
    async def send_group_help(self, group):
        await self.get_destination().send(f'{group.name}:{[command.name for index, command in enumerate(group,commands)]}')
    async def send_command_help(self, command):
        get = command.name
        get = cmds[get]
        get = cmds[get]
        await self.get_destination().send(get)



intents = discord.Intents.all()
bot = commands.Bot(command_prefix='*',intents=intents)


#def fun1():
#    subprocess.call(['java', '-jar', 'JMusicBot.jar'])


@bot.event
async def on_ready():
    print("212bot已上線")
    game = discord.Game('212の小天使')
    DiscordComponents(bot)
    await bot.change_presence(status=discord.Status.idle, activity=game)
#    sing_thread = threading.Thread(target=fun1)
#    sing_thread.start()



for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')



if __name__ == "__main__":
    bot.run(jdata['Token'])
