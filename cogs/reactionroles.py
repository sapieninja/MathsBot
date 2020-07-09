import discord
from discord.ext import commands
from __main__ import reaction_message_id
class reactionroles(commands.Cog):#defines a new class inheriting from commands.Cog
    "simple command frontend for my equation class"
    @commands.Cog.listener()
    async def on_reaction_add(self,reaction,user):
        message_id = reaction.message.id 
        print('hello')
def setup(bot):
    bot.add_cog(reactionroles(bot))
    
