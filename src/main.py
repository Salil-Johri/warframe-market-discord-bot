import discord
from discord.ext import commands
import os
import requests
from dotenv import load_dotenv
from frameclientimpl import FrameHttpClientImpl
from framebotimpl import FrameBotImpl

# Get environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
URL = os.getenv('API_URL')

# Set dependencies
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)
http_client = requests
frame_client = FrameHttpClientImpl(http_client, URL)
frame_bot = FrameBotImpl(frame_client)

# Set up discord bot hooks
@client.event
async def on_ready():
    print(f'{client.user} is connected!')

@client.command(name="price")
async def _getprice(ctx, *args):
    if(len(args) == 0):
        await ctx.send("No item supplied you dummy!")
        return
    
    print("Getting price...")
    item_string = " ".join(args)
    price = frame_bot.get_item_price(item_string)
    if price < 0:
        command_result = "item " + item_string + " was not found on warframe market"
        await ctx.reply(command_result)
    else:
        command_result = "The lowest price of " + item_string + " is " + str(price) + " platinum"
        await ctx.reply(command_result)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if(str(message.author) == 'doignuts'):
        await message.channel.send('kiss my ass DoigNuts')
        return
    await client.process_commands(message)
# Run
client.run(TOKEN)