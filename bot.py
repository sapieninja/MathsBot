import discord
from discord.ext import commands
import json
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!',
                   description="Bot to help with some functionality on speedcubers server",
                   intents=intents)
with open('info.json', 'r') as info_file:
    info = json.load(info_file)
token = info['token']
with open("loadedcogs.json", 'r') as cogs_file:
    cogs = json.load(cogs_file)
if __name__ == '__main__':
    for cog in cogs:
        bot.load_extension(cog)


@bot.event
async def on_ready():
    print(f'logged in as {bot.user.name}')


@bot.command()
@commands.has_role('4x4 (mods)')
async def addcog(ctx, cogname):
    with open("loadedcogs.json", "r") as cogs_file:
        cogs = json.load(cogs_file)
    cogname = 'cogs.' + cogname
    if cogname not in cogs:
        try:
            bot.load_extension(cogname)
            cogs.append(cogname)
        except:
            raise ValueError('You moron that cog does not exist')
    with open("loadedcogs.json", 'w') as cogs_file:
        json.dump(cogs, cogs_file)
    print(f"added {cogname}")


@bot.command()
@commands.has_role('4x4 (mods)')
async def removecog(ctx, cogname):
    with open("loadedcogs.json", "r") as cogs_file:
        cogs = json.load(cogs_file)
    cogname = 'cogs.' + cogname
    try:
        bot.unload_extension(cogname)
        cogs.remove(cogname)
    except:
        raise ValueError('You did something wrong idk')
    with open("loadedcogs.json", "w") as cogs_file:
        json.dump(cogs, cogs_file)
    await ctx.send(f"removed {cogname}")


@bot.command()
@commands.has_role('4x4 (mods)')
async def refreshcog(ctx, cogname):
    await removecog(ctx, cogname)
    await addcog(ctx, cogname)
    await ctx.send(f"refreshed {cogname}")

bot.run(token)
