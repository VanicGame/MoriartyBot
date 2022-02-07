import discord
from discord.ext import commands
import os
import random
from keep_alive import keep_alive

intents = discord.Intents.all()
client = commands.Bot(command_prefix='>', intents = intents)

@client.event
async def on_ready():
  print("the bot is ready :)")

@client.command()
async def ping(ctx, member: discord.Member):
    await ctx.send("pong, " + member.mention)

keep_alive()
TOKEN = os.getenv('MorTok')
client.run(TOKEN)