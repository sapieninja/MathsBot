import discord
from discord.ext import commands
class reactionroles(commands.Cog):#defines a new class inheriting from commands.Cog
    "simple command frontend for my equation class"
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        with open('info.json','r') as 
    @commands.command()
    async def chicken(self,ctx):
        await ctx.send('ping')
def setup(bot):
    bot.add_cog(reactionroles(bot))
    
