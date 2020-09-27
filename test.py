#created by:-Shreyas Pahune , Vishesh Mistry , Dhruvil Patel , Jahanvi Jainwal
import discord
import random
from discord.ext import commands
from RedditReader import Subreddit
#-----------------------------------------------------------------------------------------------
meme = Subreddit("memes")

C = commands.Bot(command_prefix = ".")
wlc = ["Heyy!! Let's Party",
       "Extend your arms and welcome to the future", 
       "You are as welcome as the flowers in May",
       "Good server, good wine, good welcome, can make good people",
       "Alone we can do so little, together we can do so much. Welcome!",
       "Welcome! Hope you took a shower today!",
       "Hi! Welcome to the server which is as dark as my soul!"
       "Joy waits on welcome, not time",
       "We must welcome the night. It's the only time that the stars shine",
       "Welcome ever smiles, and farewell goes out sighing. Welcome my Friend!"]
@C.event
async def on_member_join(member):
    await member.send(f"{member} "+ random.choice(wlc)) 
#-----------------------------------------------------------------------------------------------
@C.command()
async def memes(ctx):
    meme.get_random()
    url = meme.url
    print(url)
    await ctx.send(url)
#-----------------------------------------------------------------------------------------------
@C.event
async def on_ready():
    print("Bot is ready.")
#------------------------------------------------------------------------------------------------

@C.event
async def on_member_remove(member):
    print(f"{member} has left the server. Goodbyes")
#-------------------------------------------------------------------------------------------------
f=open("key.txt","r")
C.run(f.read())