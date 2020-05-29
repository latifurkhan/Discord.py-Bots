import random
import discord
from discord.ext import commands

TOKEN = ''

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("Bot is ready")


#anytime someone @ a dave (everyone is dave in the chat) ask which dave
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    author = message.author
    mention = message.author.mention
    content = message.content
    if '@' in content:
        response = f"{mention} which dave?"
        await message.channel.send(response)
    await client.process_commands(message)


#Help command explaining the different commands
@client.command()
async def h(ctx):
    roll_define = "Type !roll to roll the dice!\n"
    flip_define = "Type !flip to flip a coin!\n"
    dave_function = "If you @dave in the server, I get confused\n"
    await ctx.send("Hello daves, this is daveBot:\n" + roll_define + flip_define + dave_function)


#Coin flip command !flip
@client.command()
async def flip(ctx):
    await ctx.send("Flipped the coin: \n" + random.choice(["Heads", "Tails"]) + " was flipped!")


#Dice roll command !roll giving numbers [1-6]
@client.command()
async def roll(ctx):
    num = str((random.randrange(6)) + 1)
    await ctx.send("You rolled a " + num + "!")


client.run(TOKEN)
