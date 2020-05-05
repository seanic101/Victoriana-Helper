# bot.py
import os
import random 
import player
from roller import DiceRoller

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    grumpy = [
        'Go talk to someone else',
        'Who controls the server interactions and hates being texted? this guy',
        (
            'Stop talking to me peasent, '
            'if you keep texting ill fuck up your next roll.'
        ),
    ]

    if message.content == ('99!') or message.content == ('42!'):
                print(str(message.author)+" typed "+str(message.content))
                response = random.choice(grumpy)
                await message.channel.send(response)

    if message.content == ('roll8'):
                print(str(message.author)+" typed "+str(message.content))
                response = "The";
                await message.channel.send(response)
                
print(DiceRoller.roll_successes(8))
client.run(TOKEN)
