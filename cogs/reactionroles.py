import json

import discord
from discord.ext import commands
if __name__ != '__main__':
    from __main__ import bot
else:
    raise RuntimeError('running as __main__. Run bot.py instead')


class reactionroles(commands.Cog):  # defines a new class inheriting from commands.Cog
    "simple role on reaction code"
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        with open('info.json', 'r') as info_file:
            info = json.load(info_file)
        message_id = payload.message_id
        guild_id = payload.guild_id
        if message_id == info['reaction_message_id']:
            guild = bot.get_guild(guild_id)
            member = guild.get_member(payload.user_id)
            role = guild.get_role(info['role_id'])
            await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        with open('info.json', 'r') as info_file:
            info = json.load(info_file)
        message_id = payload.message_id
        guild_id = payload.guild_id
        if message_id == info['reaction_message_id']:
            guild = bot.get_guild(guild_id)
            member = guild.get_member(payload.user_id)
            role = guild.get_role(info['role_id'])
            await member.remove_roles(role)


def setup(bot):
    bot.add_cog(reactionroles(bot))
    print("loaded reactionroles")
