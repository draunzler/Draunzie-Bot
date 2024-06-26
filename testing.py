import discord
from discord.ext import commands
import random
import aiohttp
from aiohttp import web
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('ID')

intents = discord.Intents.default()
intents.message_content = True

async def handle(request):
    return web.Response(text="Hello, this is a web server running within your Discord bot.")

app = web.Application()
app.router.add_get('/', handle)

client = commands.Bot(command_prefix = '/', intents=intents)

@client.event
async def on_ready():
  for guild in client.guilds:
    if guild.name == "OnlyFriends":
      break
        
  print(f'{client.user} has connected to Discord!')
  print(f'{guild.name}(id: {guild.id})')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  # print("message:", message)
  # print(f"Message content: {message.content}")
  if message.content.startswith("hey sunday" or "Hey sunday" or "Hey Sunday" or "hey Sunday"):

    async with aiohttp.ClientSession() as session:
      payload = message.content + " within 1800 characters"
      req_body = {'prompt': payload}
      print(req_body, type(req_body))
      async with session.post("https://sunday-hx52.onrender.com", json=req_body, headers={'Content-Type': 'application/json'}) as response:
        if response.status == 200:
          response_text = await response.json()
          await message.channel.send(response_text['bot'])
        else:
          await message.channel.send("Waiting on the server.")

@client.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'Kicked {member.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')
  for ban_entry in banned_users:
    user = ban_entry.user
  if(user.name, user.discriminator) == (member_name, member_discriminator):
    await ctx.guild.unban(user)
    await ctx.send(f'Unbanned {user.mention}')
    return

async def start_bot():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.getenv('PORT', 8080)))
    await site.start()

    await client.start(TOKEN)

import asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
