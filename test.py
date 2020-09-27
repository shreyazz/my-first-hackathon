import discord
from discord.ext import commands

C = commands.Bot(command_prefix = ".")

@C.command()
async def ping(ctx):
    await ctx.send(f"Aur kese ho? {round(C.latency * 1000)}ms")

@C.event
async def on_ready():
    print("Bot is ready.")

@C.event
async def on_member_join(member):
    print(f"{member} has joined the server")

@C.event
async def on_member_remove(member):
    print(f"{member} has left the server. Goodbyes")

C.run("")