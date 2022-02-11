import psutil,os
import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Developer(Cog_Extension):
    @commands.command(aliases=['memory'])
    async def ram(self,ctx):
        def my_ram():
            process = psutil.Process(os.getpid())
            return (psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)

        memoryEmbed = discord.Embed(title="🔧 | 記憶體使用量", description=f"已使用 `{my_ram()}` MB", color=0x0000ff)
        await ctx.send(embed=memoryEmbed)



def setup(bot):
    bot.add_cog(Developer(bot))
