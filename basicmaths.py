import discord
from discord.ext import commands
class basicmaths(commands.Cog):#defines a new class inheriting from commands.Cog
    "just basic maths commands which don't store data or do anything complicated for now"
    @commands.command()
    async def add(self,ctx,a: int,b:int):
        await ctx.send(a+b)
def setup(bot):
    bot.add_cog(basicmaths(bot))
    
