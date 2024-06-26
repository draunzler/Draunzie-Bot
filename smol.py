import discord
from discord.ext import commands
import aiohttp
import random
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('ID')

client = discord.Client()
client = commands.Bot(command_prefix = '!')

@client.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

client.run(TOKEN)
