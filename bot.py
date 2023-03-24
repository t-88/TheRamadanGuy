import discord
from discord.ext import commands , tasks 
from datetime import datetime , timedelta
import asyncio
import data

client = commands.Bot(command_prefix=".",intents=discord.Intents.all())
genralChannelID = 1088616278341734422


@client.command()
async def sup(ctx):
    await ctx.author.send("sup")


@tasks.loop(seconds=1)
async def salatAlSobhe():
    now = datetime.now()
    fotorTime = datetime(now.year,now.month,now.day,10,0)
    wait_seconds = (fotorTime - now).total_seconds()
    if wait_seconds > 0 :
        await asyncio.sleep(wait_seconds)
    else :
        wait_seconds  = wait_seconds + 24 * 60 * 60
        await asyncio.sleep(wait_seconds)

    channel = client.get_channel(genralChannelID)
    await channel.send("`wake up brother its time to worship salato al sob7e`")

@tasks.loop(seconds=1)
async def alFotore():
    now = datetime.now()
    fotorTime = datetime(now.year,now.month,now.day,17,10)
    wait_seconds = (fotorTime - now).total_seconds()
    if wait_seconds > 0 :
        await asyncio.sleep(wait_seconds)
    else :
        wait_seconds  = wait_seconds + 24 * 60 * 60
        await asyncio.sleep(wait_seconds)

    channel = client.get_channel(genralChannelID)
    await channel.send("`sa7a ftork borther`")


@client.event
async def on_ready():
    salatAlSobhe.start()
    alFotore.start()
    
    print(f"{client.user} is now connected")



client.run(data.token)