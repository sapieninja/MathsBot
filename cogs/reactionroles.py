import json

import discord
from discord.ext import commands
if __name__ != '__main__':
    from __main__ import bot
else:
    raise RuntimeError('running as __main__. Run bot.py instead')


class reactionroles(commands.Cog):#defines a new class inheriting from commands.Cog
    "simple command frontend for my equation class"
    def roles_info(self,payload):
        with open('info.json','r') as info_file:
            info = json.load(info_file)
        if payload.message_id != info['reaction_message_id']:
            return None
        guild = bot.get_guild(payload.guild_id)
        role = guild.get_role(info["role_id"])#
        return role,guild
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        role, guild= self.roles_info(payload)
        if role is not None: #avoid some console spam (not necessary but nice to have)
            await payload.member.add_roles(role)
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload):
        role, guild = self.roles_info(payload)
        if role is not None:
            member = guild.get_member(payload.user_id) #payload does not have a member subclass in this occasion-
            await member.remove_roles(role)
    @commands.command()
    async def chicken(self,ctx):
        await ctx.send('ping')
def setup(bot):
    bot.add_cog(reactionroles(bot))
