#!/usr/bin/env python3.6
import discord
import asyncio
import time
import logging
import requests
import sys
import os
from discord.ext.commands import Bot
from discord.ext import commands

logging.basicConfig(level=logging.INFO)

Client = discord.Client()
bot_prefix= "s."
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.send_message(discord.Object(id="347403986543968267"), "ClueBot's python module is now back online")


#ping
@client.command(pass_context=True)
async def ping(ctx):
    embed = discord.Embed(title = "I am alive!", description = "Yes Mee6. I am alive.", color = 0xFFFFF)
    return await client.say(embed = embed)

#restart
@client.command(pass_context=True)
async def restart(ctx):
    await client.say("Restarting ClueBot.py...")
    os.execv(sys.executable, ["python3.6"] + sys.argv)
    exit()

#command2
@client.command(pass_context = True)
async def getbans(ctx):
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of Banned Members", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

#meow
@client.command(pass_context=True)
async def meow(ctx):
    r = requests.get("http://random.cat/meow")
    if r.status_code == 200:
        js = r.json()
        await client.send_message(ctx.message.channel, js["file"])

#woof
@client.command(pass_context=True)
async def woof(ctx):
    r = requests.get("http://random.dog/woof.json")
    js = r.json()
    await client.send_message(ctx.message.channel, js["url"])

#clue1: Salisbury Park to Skinners' Field
@client.command(pass_context=True)
async def clue1(ctx):
    await client.say("This hunt should be fun, mainly because I tried to cater for everyone.Solve the puzzle to get your first clue, which has something to do with the colour blue. ")
    await client.say("http://nathanf.co.uk/wp-content/uploads/2017/08/logic.png")

#clue1.1: Salisbury PArk to Skinners' Field
@client.command(pass_context=True)
async def clue11(ctx):
    await client.say("Waiting for clearance from @spookydipity...")
    await client.send_message(discord.Object(id="347403986543968267"),"{} needs permission to access the Skinners' Field clue. React with 👌 to allow it.".format(ctx.message.author))
    await client.wait_for_reaction(['👌'], message=msg)
    await client.say("!clear 1")
    await client.send_message(ctx.message.author,"A place to see the opposite to the sea, kept by our sister school under lock and key.")
    await client.send_message(discord.Object(id="347403986543968267"),"{} just accessed Clue 1.1!".format(ctx.message.author))

#clue2: Skinners' Field to TWGSB
@client.command(pass_context=True)
async def clue2(ctx):
    await client.say("Waiting for clearance from @spookydipity...")
    await client.send_message(discord.Object(id="347403986543968267"),"{} needs permission to access the TWGSB clue. React with 👍 to allow it.".format(ctx.message.author))
    await client.wait_for_reaction(['👍'], message=msg)
    await client.say("!clear 1")
    await client.send_message(ctx.message.author,"http://spoti.fi/2tAHjHw")
    await client.send_message(discord.Object(id="347403986543968267"),"{} just accessed Clue 2!".format(ctx.message.author))

#clue3: TWGSB to Calverley Grounds
@client.command(pass_context=True)
async def clue3(ctx):
    await client.say("Waiting for clearance from @spookydipity...")
    await client.send_message(discord.Object(id="347403986543968267"),"{} needs permission to access the Calverley Grounds clue. React with 🏫 to allow it.".format(ctx.message.author))
    await client.wait_for_reaction(['🏫'], message=msg)
    await client.say("!clear 1")
    await client.send_message(ctx.message.author,"http://www.nathanf.co.uk/wp-content/uploads/2017/10/snapcode.png")
    await client.send_message(discord.Object(id="347403986543968267"),"{} just accessed Clue 3!".format(ctx.message.author))

#clue4: Calverley Grounds to The Forum
@client.command(pass_context=True)
async def clue4(ctx):
    await client.say("Waiting for clearance from @spookydipity...")
    await client.send_message(discord.Object(id="347403986543968267"),"{} needs permission to access the The Forum clue. React with 😂 to allow it.".format(ctx.message.author))
    await client.wait_for_reaction(['😂'], message=msg)
    await client.say("!clear 1")
    await client.send_message(ctx.message.author,"D yhqxh iru pxvlf, zlwk vrqjv vr suhwwb. Exw brx pdb qrw xvh lw, 'Fdxvh wkh exloglqj orrnv vklwwb. (Foxh Surylghg eb Hood)")
    await client.send_message(discord.Object(id="347403986543968267"),"{} just accessed Clue 4!".format(ctx.message.author))

#clue5: The Forum to Tunbridge Wells Library
@client.command(pass_context=True)
async def clue5(ctx):
    await client.say("Waiting for clearance from @spookydipity...")
    await client.send_message(discord.Object(id="347403986543968267"),"{} needs permission to access the The Library clue. React with 😉 to allow it.".format(ctx.message.author))
    await client.wait_for_reaction(['😉'], message=msg)
    await client.say("!clear 1")
    await client.send_message(ctx.message.author,"The next clue is on a website, http://nathanf.co.uk/twcavenger/clue-2 (CBA to change the web address). But it is locked. You need to use your knowledge of algorithms to obtain the password.")
    await client.send_message(ctx.message.author,"My brother goes to Boys Grammar. His name is Joel Friend, and he is in Year 8. If he went to SKA, what would his username be? The username is all lowercase.")
    await client.send_message(discord.Object(id="347403986543968267"),"{} just accessed Clue 5!".format(ctx.message.author))

#clue6: Tunbridge Wells Library to Lower Common
@client.command(pass_context=True)
async def clue6(ctx):
    await client.say("Waiting for clearance from @spookydipity...")
    await client.send_message(discord.Object(id="347403986543968267"),"{} needs permission to access the The Library clue. React with 🐈 to allow it.".format(ctx.message.author))
    await client.wait_for_reaction(['🐈'], message=msg)
    await client.say("!clear 1")
    await client.send_message(ctx.message.author,"TQ 580 394")
    await client.send_message(discord.Object(id="347403986543968267"),"{} just accessed Clue 6!".format(ctx.message.author))

client.run("MzM2MDg5NTU1Mjg1NDQyNTYx.DL6O5A.gLZyA72MidfMlU5YjRM4VMBmm5U")
