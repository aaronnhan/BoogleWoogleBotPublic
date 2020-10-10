# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
intents.typing = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


# @client.event
# async def on_typing(channel, user, when):
#     if channel.name == "library":
#         await channel.send("QUIET " + user.name.upper() + "! THIS IS A LIBRARY")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name == "library":
         await message.channel.purge(limit=1)
         await message.channel.send("QUIET " + message.author.name.upper() + "! THIS IS A LIBRARY")


@client.event
async def on_message_edit(before, after):
    await before.channel.send("I saw u edit that")
client.run(TOKEN)