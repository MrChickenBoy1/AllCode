import discord
from discord.ext import commands
import random

words = ["It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
        "Ask Akshat and Kushagra"]

client  = commands.Bot(command_prefix = "!")

@client.event

async def on_ready():
    print ("I AM READY")
    
@client.event
async def on_member_join(member):
    print (f"{member} joined the server!" )

@client.command()

async def MinecraftTime(ctx, message):
    if message == "MinecraftTime?":
        await ctx.send(f"Question: {message}")
        await ctx.send(f"Answer: {random.choice(words)} ")
    



    
client.run("OTAzNTczNzU5OTg0ODAzODQw.YXu8ow.xqvwBmDLfpqb0L-SPBobh7soEGQ")