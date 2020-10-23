import discord
from discord.ext import commands
from cogs.equation import equation as equation
class maths(commands.Cog):#defines a new class inheriting from commands.Cog
    "simple command frontend for my equation class"
    @commands.command(name = "eval")
    async def evaluate(self,ctx,exp:str):
        expression = equation(exp)
        await ctx.send(str(expression))
def setup(bot):
    bot.add_cog(maths(bot))
    
