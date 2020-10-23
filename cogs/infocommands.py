import discord
from discord.ext import commands
import json
class infocommands(commands.Cog):#defines a new class inheriting from commands.Cog
    "allows info commands that just send a certain message when called"
    @commands.has_role('4x4 (mods)')
    @commands.group()
    async def info(self,ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('No subcommand specified; try info setnew')
    @info.command()
    async def setnew(self,ctx,new_command_name:str,*,new_command_string):
        new_command_name.replace(" ","")  #remove all whitespace which could cause issues later
        new_command_string.replace(" ","")
        with open('infocommands.json','r') as infocommands_file:
            infocommands = json.load(infocommands_file)
        if bool(new_command_name) and bool(new_command_string):
            infocommands[new_command_name] = new_command_string
            with open('infocommands.json','w') as infocommands_file:
                json.dump(infocommands,infocommands_file)
    @info.command()
    async def remove(self,ctx,command_name):
        with open("infocommands.json","r") as infocommands_file:
            infocommands = json.load(infocommands_file)
        infocommands.pop(command_name,None)#none stops an error being generated 
        with open("infocommands.json","w") as infocommands_file:
            json.dump(infocommands,infocommands_file)
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.content.startswith('!'):
            with open("infocommands.json","r") as infocommands_file:
                infocommands = json.load(infocommands_file)
            if message.content[1::] in infocommands:
                await message.channel.send(infocommands[message.content[1::]])


def setup(bot):
    bot.add_cog(infocommands(bot))
    
