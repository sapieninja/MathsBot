import discord
from discord.ext import commands
import json
bot = commands.Bot(command_prefix='!')
with open('info.json','r') as info_file:
    info = json.load(info_file)
token = info['token']
reaction_message_id = 100
cogs = ['cogs.maths','cogs.errorhandling','cogs.reactionroles']
if __name__ == '__main__':
    for cog in cogs:
        bot.load_extension(cog)
@bot.event
async def on_ready():
    print(f'logged in as {bot.user.name}')
bot.run(token)
        
