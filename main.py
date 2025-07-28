import os

import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True  # Required to manage roles
intents.message_content = True # Required to read message content
intents.reactions = True # Required to detect reactions

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)