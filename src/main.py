import os

from discord.ext import commands
from src.delve import Delve

bot = commands.Bot(command_prefix='$')

@bot.command()
async def salvage(ctx, area_level: int, task_difficulty: int):
    result = Delve(area_level, task_difficulty).salvage()
    await ctx.send(result.message())

bot.run(os.getenv('TOKEN'))
