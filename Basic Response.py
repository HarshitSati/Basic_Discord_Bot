import discord
from discord.ext import commands
import random

# This determines a keyword that the bot will look for. Having nothing means it can reply even when the bot isnt called
client = commands.Bot(command_prefix="")

# this will print as soon as the bot is live
@client.event
async def on_ready():
	print("bot is ready.")

# Whenever the bot sees a 'uwu" message, it will reply
@client.command()
async def uwu(ctx):
	await ctx.send("> owo")

# Replies to 'ayy' with 'lmao'
@client.command()
async def ayy(ctx):
	await ctx.send("> lmao")

# replies to 'ping' command with the latency
@client.command()
async def ping(ctx):
	await ctx.send(f"> Pong! {round(client.latency * 1000)}ms")

# replies to any sentence that could be a question with a random annoying response
@client.command(aliases=['will','should', 'Should', 'does','is','Is', 'can', 'have','Will', 'Does', 'Can', 'Have'])
async def question(ctx, *, Question):
	responses = ['Definetly','I am sure','Yes', 'No', 'I dont think so', 'I guess', 'i dont know.']
	await ctx.send(f"> {random.choice(responses)}")

# She used to call me on my cell phone
@client.command(aliases=["sheusedto", "Sheusedto"])
async def drake(ctx):
	await ctx.send('*** Call me on my cell phone ***')

# replies to all the code cells posted 
@client.command(aliases=["```cpp","```py"])
async def code(ctx):
	await ctx.send('*** I like coding. ***')

# replies to the orz emote
@client.command(aliases=["<:orz:708198765286129684>", "orz"])
async def orzxx(ctx):
	await ctx.send(' <:orz:708198765286129684> <:orz:708198765286129684> <:orz:708198765286129684> ')

# xd
@client.command(aliases=["xd", "XD", "xD", "Xd"])
async def xdddd(ctx):
	await ctx.send('*** XD ***')

# kills the bot
@client.command()
async def diebot(ctx):
	await ctx.send("Dying")
	exit()
client.run(PUT ID HERE)
