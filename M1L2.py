import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.command()
async def repeat(ctx, times: int, content='BEN LİBERALİST BİR BOTUM'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

bot.run('Token gir')
