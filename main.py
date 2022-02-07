import discord
from discord.ext import commands
import os
import random
from keep_alive import keep_alive

yes_text = """
**•Добро пожаловать Сеньор в RP проект со своим лором, рады видеть вас.
Должн(-а) сказать, всё  замечательно.

• Ваша заявка Одобрена.
Если вашу заявку одобрили, вы можете вступать в rp 

{Приятного Времяпрепровождения в RP фентези. 
RP можно начать сегодня.
Помните о правилах Рп и правописания в каналах Информаций и правил.

Информация о городах и Лоре в категории Help RP.
Приятного Дня/Вечера дорогой Сеньор.}**
"""

def yes_emb(titl, desc):
    embed = discord.Embed(
        title = titl,
        description = desc,
        colour = 0x71C947)
    embed.set_image(url = 'https://share-cdn.picrew.me/shareImg/org/202201/147002_Cb3EqsjR.png')
    return embed

intents = discord.Intents.all()
client = commands.Bot(command_prefix='>', intents = intents)

@client.event
async def on_ready():
  print("the bot is ready :)")

@client.command()
async def ping(ctx, member: discord.Member):
    await ctx.send("pong, " + member.mention)

@client.command()
async def yes(ctx, member: discord.Member):
    if member is not None:
        embed = yes_emb("Проверили", member.mention + yes_text)
    await member.add_roles(member.guild.get_role(919276951255019521))
    await ctx.send(embed = embed)

keep_alive()
TOKEN = os.getenv('MorTok')
client.run(TOKEN)