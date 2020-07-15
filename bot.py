import discord
from discord.ext import commands
import json
bot = commands.Bot(command_prefix='!',description="Bot to help with some functionality on speedcubers server")
with open('info.json','r') as info_file:
    info = json.load(info_file) 
token = info['token']
reaction_message_id = 100
with open("loadedcogs.json",'r') as cogs_file:
    cogs = json.load(cogs_file)
if __name__ == '__main__':
    for cog in cogs:
        bot.load_extension(cog)
@bot.event
async def on_ready():
    print(f'logged in as {bot.user.name}')
@bot.command()
@commands.has_role('4x4(mods)')
async def addcog(ctx,cogname):
    with open("loadedcogs.json","r") as cogs_file:
        cogs = json.load(cogs_file)
    cogname = 'cogs.' + cogname
    if cogname not in cogs:
        try:
            bot.load_extension(cogname)
            cogs.append(cogname)
        except:
            raise ValueError('You moron that cog does not exist')
    with open("loadedcogs.json",'w') as cogs_file:
        json.dump(cogs,cogs_file)
@bot.command()
@commands.has_role('4x4(mods)')
async def removecog(ctx,cogname):
    with open("loadedcogs.json","r") as cogs_file:
        cogs = json.load(cogs_file)
    cogname = 'cogs.' + cogname
    try:
        bot.unload_extension(cogname)
        cogs.remove(cogname)
    except:
        raise ValueError('You did something wrong idk')
    with open("loadedcogs.json","w") as cogs_file:
        json.dump(cogs,cogs_file)          
    
bot.run(token)
        
