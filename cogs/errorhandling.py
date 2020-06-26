import discord
from discord.ext import commands
class errorhandling(commands.Cog):
    "basic error handling"
    @commands.Cog.listener()#will check for an event happening and call the coroutine on that event.
    async def on_command_error(self,ctx,error):
        print('{0.mention} that command has resulted in the following error: {1}'.format(ctx.author,error))
def setup(bot):
    bot.add_cog(errorhandling(bot))
