import discord
from discord.ext import commands
from cogs.equation import equation as equation
import asyncio
class clearcommand(commands.Cog):#defines a new class inheriting from commands.Cog
    "simple command that can delete messages "
    @commands.command()
    async def clear(self,ctx,no: int):
        if no < 1:
            raise ValueError()
        async for message in ctx.channel.history(limit = no+1):
            await message.delete()
        message = await ctx.send(f"Deleted {no+1} messages in this channel")
        await asyncio.sleep(10)
        await message.delete()
    @clear.error
    async def clearerror(self,ctx,error):
        message = await ctx.send("You must give a number that is more than/equal to 1")
        await asyncio.sleep(10)
        await message.delete()
def setup(bot):
    bot.add_cog(clearcommand(bot))
