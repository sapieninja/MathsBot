import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!')
token = input()#you thought i was going to give you my API token haha
cogs = ['cogs.basicmaths','cogs.errorhandling']
if __name__ == '__main__':
    for cog in cogs:
        bot.load_extension(cog)
@bot.event
async def on_message(ctx):
    raise EVERYTHING_IS_NOT_DONE_YET_ERROR()
@bot.event
async def on_ready():
    print(f'logged in as {bot.user.name}')
bot.run(token)
        
