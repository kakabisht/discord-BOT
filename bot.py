from botkey import token    # This just contains the Bot token
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_member_join(member):
    print("{0} has joined the server".format(member))

@client.event
async def on_member_remove(member):
    print("{0} has left the server".format(member))

# to check the latency
@client.command()
async def ping(ctx):
    await ctx.send(f"Latency: {round(client.latency*1000)}ms")


client.run(token)