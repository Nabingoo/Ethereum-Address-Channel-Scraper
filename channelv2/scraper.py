#from asyncio.windows_events import NULL
from operator import indexOf
import os
from pickle import NONE
import discord
from discord.ext import commands
from discord import Embed
import time
import datetime
from datetime import timedelta
#from datetime import timezone
from datetime import datetime
import sqlite3
import random
import math
import itertools
from typing import Optional
from discord.utils import get
intents = discord.Intents.default()
conn = sqlite3.connect( 'ethaddress.db')
sqlite3
print ("XP DB Opened Successfully")
print (os.getcwd())
intents.guilds = True

activity = discord.Activity(type=discord.ActivityType.watching, name="Reading Addresses >:)")
bot = commands.Bot(command_prefix = "+", intents = intents, activity=activity, status=discord.Status.online)


        

    
@bot.command()
async def scrape(ctx):
    await ctx.channel.send("Scraping.")
    messages = await ctx.channel.history(limit=10000).flatten()
    m = [x.content for x in messages]
    n = [x.author.id for x in messages]
    set(n)
    set(m)
    del m[0]
    del n[0]
    

    for(a,b) in zip(n,m):
        if b.find("0x") >= 0:
            ind = str(b).index('0x')
        
            v_eth = (b[ind:(ind + 42)])
        else:
            v_eth = ("doesn't have an eth addy lol")
        v_discordid = int(a)    
        print(v_discordid, v_eth)
        cursor = conn.execute('''INSERT INTO EthAddress (DiscordID,EthAddress) VALUES (?,?)''',(v_discordid,v_eth))
        conn.commit()
 
    await ctx.channel.send("done")


bot.run("OTYzMTE0Mjk4NTM4ODg1MTYw.YlRYFg.PYKdCspm0_Nko_74K_adj4n5eGk")