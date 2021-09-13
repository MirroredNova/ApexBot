import os

import discord
import requests
import json
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='|')

load_dotenv('.env')
TOKEN = os.getenv('TOKEN')
API_KEY = os.getenv('API_KEY')


@bot.command()
async def rotation(ctx):
    await ctx.send(embed=get_map())


def get_map():
    data = requests.get("https://api.mozambiquehe.re/maprotation?version=2&auth={}".format(API_KEY)).json()
    embeded = discord.Embed(title="Map Rotation", description="The current map is: " + data['battle_royale']['current']['map'])
    embeded.add_field(name="Minutes Remaining", value=data['battle_royale']['current']['remainingMins'])
    return embeded


bot.run(TOKEN)
