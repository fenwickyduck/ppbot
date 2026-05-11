import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


messages = ["↑\nDoesn't know.","↑\nSkill issue?","↑\nSompCoc.","↑\nFaulty Wetware.","↑\nNever gets hacked.",
            "↑\nUses Vim.","↑\nHello, human resources?","↑\nSorry, I cannot fulfill that request.",
            "↑\nHigh and low.","↑\nUses Windows.","↑\nTrivial.","↑\npphuman (presumably).","↑\n@everyone",
            "↑\nFun at parties.","↑\nWho is this?","↑\nCan't afford CompSoc membership.","↑\nNice use of free will.",
            "↑\nSoftware crashes itself in your presence."]

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    else:
        mess = random.choice(messages)
        await message.channel.send(mess)

def run_bot(key):
    print("running bot")
    client.run(key)