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

#command1
#@client.command(pass_context = True)
#async def invite(ctx):
#    x = await client.invites_from(ctx.message.server)
#    x = ["<" + y.url + ">" for y in x]
#    print(x)
#    embed = discord.Embed(title = "Invite Links", description = x, color = 0xFFFFF)
#    return await client.say(embed = embed)

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
    await client.say("!clear 1")
    await asyncio.sleep(2)
    await client.say("This hunt should be fun, mainly because I tried to cater for everyone.Solve the puzzle to get your next clue, which has something to do with the colour blue. ")
    await client.say("http://nathanf.co.uk/wp-content/uploads/2017/08/logic.png")

#clue1.1: Salisbury Park to Skinners' Field
@client.command(pass_context=True)
async def gideontambry(ctx):
    await client.say("!clear 1")
    await asyncio.sleep(2)
    await client.send_message(ctx.message.author,"Use command clue12 to get your next clue!")

#clue1.2: Salisbury PArk to SKinners' Field
@client.command(pass_context=True)
async def clue12(ctx):
    await client.say("!clear 1")
    await asyncio.sleep(2)
    await client.send_message("A place to see the opposite to the sea, kept by our sister school under lock and key.")
    await client.send_message(discord.Object(id="347403986543968267"),"{} just accessed Clue 1.2!".format(ctx.message.author))

#clue2: Skinners' Field to TWGSB
@client.command(pass_context=True)
async def clue2(ctx):
    await client.say("!clear 1")
    await asyncio.sleep(2)
    await client.send_message(ctx.message.author,"http://spoti.fi/2tAHjHw")
    await client.send_message(discord.Object(id="347403986543968267"),"{} just accessed Clue 2!".format(ctx.message.author))

#clue3: TWGSB to Calverley Grounds
@client.command(pass_context=True)
async def clue3(ctx):
    await client.say("!clear 1")
    await asyncio.sleep(2)
    await client.send_message(ctx.message.author,"PLACE SNAPCODE HERE")

#clue4: Calverley Grounds to The Forum
@client.command(pass_context=True)
async def clue4(ctx):
    await client.say("!clear 1")
    await asyncio.sleep(2)
    await client.send_message(ctx.message.author,"D yhqxh iru pxvlf, zlwk vrqjv vr suhwwb. Exw brx pdb qrw xvh lw, 'Fdxvh wkh exloglqj orrnv vklwwb. (Foxh Surylghg eb Hood)")

#clue5: The Forum to Tunbridge Wells Library
@client.command(pass_context=True)
async def clue5(ctx):
	await client.say("Nathan still needs to do this clue... Go nag him.")


#command5 @client.command(pass_context=True) async def clear(ctx, number):
    #mgs = []
    #number = int(number) #Converting the amount of messages to delete to an integer
    #async for x in client.logs_from(ctx.message.channel, limit = number):
        #mgs.append(x)
    #await client.delete_messages(mgs)

client.run("MzM2MDg5NTU1Mjg1NDQyNTYx.DEzTjQ.fL4TLOO_zv8Xu1yImZrG0GYJXRs")
