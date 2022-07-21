import discord
from discord.ext import commands
import random
import aiohttp

client = discord.Client()
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Me a bot but me still Draunzie')

words = ["ayo", "hey", "hello", "sup", "what up", "what's up", "yo", "Ayo", "Hey", "Hello", "Sup", "What up", "What's up"]
reply = ["ay!", "sup!", "hey", "sup dawg!"]
ask = ["what is your name", "what's your name"]
mean_reply = ["imagine abusing a bot to boost your ego", "stay virgin <:KEKW:888019808061390888>"]
mean = ["dumb bot", "shit bot", "stupid bot", "trash bot"]
funny = ["lol", "looooool", "lool", "<:KEKW:888019808061390888>", "lmao", "lmfao", "lmafaooo", "loooooooool", "bahahaha", "hahaha"]

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if any(word in message.content.split()for word in words):
    await message.channel.send(random.choice(reply))

  if any(word in message.content.split()for word in funny):
    await message.channel.send("<:KEKW:888019808061390888>")
    
  if message.content == "wtf":
    await message.channel.send("<:KEKW:888019808061390888>")
    
  if any(word in message.content for word in ask):
    await message.channel.send("Hey! My name is Draunzie Bot. I'm named after my developer")

  if message.content.startswith("gay bot"):
    await message.channel.send("I'm straighter than your dick")

  if any(word in message.content for word in mean):
    await message.channel.send(random.choice(mean_reply))

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

client.run('OTYzNDM0NTUyNDk0MjcyNjAy.G_ZR2l.DfjU0eE6tQpqVJNMM42ZhY6KOvsanTQyKH-0w4')