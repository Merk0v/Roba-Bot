import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='RektNoob'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '$bot':
        await client.send_message(message.channel,'no u')
    if message.content == '$robert':
        await client.send_message(message.channel,'fucking legend')
client.run('NTg0MTQ3NjczNTA2OTA2MTQy.XPGyaA.KkhLYG6Tau7iaNszbP8IxJsKRVs')
