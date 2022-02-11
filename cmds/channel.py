import discord
from discord.ext import commands
from core.classes import Cog_Extension
from discord_components import *
import json,random

class Channel(Cog_Extension):
    @commands.command(aliases=['gi','guildinformation'])
    async def guildid(self,ctx):
        guild = ctx.guild
        embed=discord.Embed(
            description = f"伺服id：{guild.id}\n\n總人數：{guild.member_count}人，可容納{guild.max_members}\n語言：{guild.preferred_locale}\n加成等級：{guild.premium_tier}",
            color=0x1f7b1e)
        embed.set_author(name=f"{guild.name}",icon_url=guild.icon_url)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Channel(bot))