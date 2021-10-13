# bot.py
import os
import asyncio
import datetime
import discord
from discord_buttons_plugin import *
from dotenv import load_dotenv
from discord.ext import tasks
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
ha = int(100)
gt1 = int(100)
gt2 = int(100)
ogre = int(600)
ogremin = ogre // 60
ogresec = (ogre - (ogremin * 60))
client = discord.Client()
bot = commands.Bot(command_prefix='!')
buttons = ButtonsClient(bot)
@buttons.click
async def button_ha(ctx):
    global ha
    ha -= 1
@buttons.click
async def button_gt1(ctx):
    global gt1
    gt1 -= 1
@buttons.click
async def button_gt2(ctx):
    global gt2
    gt2 -= 1
@buttons.click
async def ogre_minus_three(ctx):
    global ogre
    ogre -= 3
@buttons.click
async def ogre_minus_30(ctx):
    global ogre
    ogre -= 30
@bot.event
async def on_message(message):
    global ha, gt1, gt2, message2, ogre, button, ogremin, ogresec
    if message.content.startswith('!resetmsg'):
        embedVar = discord.Embed(title="HP", description="This shows the HP of OUR structures! *and fuck jacob*",color=0x00ff00)
        embedVar.add_field(name="Guard Tower 1", value=gt1, inline=False)
        embedVar.add_field(name="Guard Tower 2", value=gt2, inline=False)
        embedVar.add_field(name="Holy Artifact", value=ha, inline=False)
        embedVar.add_field(name="Ogre Timer (may differ up to 3 secs)", value=datetime.timedelta(seconds=ogre),inline=False)
        await message2.delete()
        message2 = await message.channel.send(embed=embedVar)
        await message.delete()
    elif message.content.startswith('!start'):
        button = await buttons.send(
            content="Test",
            channel=843225743172435978,
            components=[
                ActionRow([
                    Button(
                        label="Holy Artifact",
                        style=ButtonType().Primary,
                        custom_id="button_ha"
                    ),
                    Button(
                        label="Guard Tower 1",
                        style=ButtonType().Primary,
                        custom_id="button_gt1"
                    ),
                    Button(
                        label="Guard Tower 2",
                        style=ButtonType().Primary,
                        custom_id="button_gt2"
                    ),
                    Button(
                        label="Ogre -3",
                        style=ButtonType().Primary,
                        custom_id="ogre_minus_three"
                    ),
                    Button(
                        label="Ogre -30",
                        style=ButtonType().Primary,
                        custom_id="ogre_minus_30"
                    ),
                ])])
        button2 = await buttons.send(
            content="Test",
            channel=843225743172435978,
            components=[
                ActionRow([
                    Button(
                        label="Holy Artifact",
                        style=ButtonType().Primary,
                        custom_id="button_ha"
                    ),
                    Button(
                        label="Guard Tower 1",
                        style=ButtonType().Primary,
                        custom_id="button_gt1"
                    ),
                    Button(
                        label="Guard Tower 2",
                        style=ButtonType().Primary,
                        custom_id="button_gt2"
                    ),
                    Button(
                        label="Ogre -3",
                        style=ButtonType().Primary,
                        custom_id="ogre_minus_three"
                    ),
                    Button(
                        label="Ogre -30",
                        style=ButtonType().Primary,
                        custom_id="ogre_minus_30"
                    ),
                ])])
        button3 = await buttons.send(
            content="Test",
            channel=843225743172435978,
            components=[
                ActionRow([
                    Button(
                        label="Holy Artifact",
                        style=ButtonType().Primary,
                        custom_id="button_ha"
                    ),
                    Button(
                        label="Guard Tower 1",
                        style=ButtonType().Primary,
                        custom_id="button_gt1"
                    ),
                    Button(
                        label="Guard Tower 2",
                        style=ButtonType().Primary,
                        custom_id="button_gt2"
                    ),
                    Button(
                        label="Ogre -3",
                        style=ButtonType().Primary,
                        custom_id="ogre_minus_three"
                    ),
                    Button(
                        label="Ogre -30",
                        style=ButtonType().Primary,
                        custom_id="ogre_minus_30"
                    ),
                ])])
        embedVar = discord.Embed(title="HP", description="This shows the HP of OUR structures! *and fuck jacob*",color=0x00ff00)
        embedVar.add_field(name="Guard Tower 1", value=gt1, inline=False)
        embedVar.add_field(name="Guard Tower 2", value=gt2, inline=False)
        embedVar.add_field(name="Holy Artifact", value=ha, inline=False)
        embedVar.add_field(name="Ogre Timer (may differ up to 3 secs)", value=datetime.timedelta(seconds=ogre),inline=False)
        message2 = await message.channel.send(embed=embedVar)
        test.start()
        await message.delete()
    elif message.content.startswith('!resetall'):
        ha = 100
        gt1 = 100
        gt2 = 100
        embedVar = discord.Embed(title="HP", description="This shows the HP of OUR structures! *and fuck jacob*",color=0x00ff00)
        embedVar.add_field(name="Guard Tower 1", value=gt1, inline=False)
        embedVar.add_field(name="Guard Tower 2", value=gt2, inline=False)
        embedVar.add_field(name="Holy Artifact", value=ha, inline=False)
        embedVar.add_field(name="Ogre Timer (may differ up to 3 secs)", value=datetime.timedelta(seconds=ogre),inline=False)
        await message2.edit(embed=embedVar)
        await message.delete()
    elif message.content.startswith('!resetha'):
        ha = 100
        embedVar = discord.Embed(title="HP", description="This shows the HP of OUR structures! *and fuck jacob*",color=0x00ff00)
        embedVar.add_field(name="Guard Tower 1", value=gt1, inline=False)
        embedVar.add_field(name="Guard Tower 2", value=gt2, inline=False)
        embedVar.add_field(name="Holy Artifact", value=ha, inline=False)
        embedVar.add_field(name="Ogre Timer (may differ up to 3 secs)", value=datetime.timedelta(seconds=ogre),inline=False)
        await message2.edit(embed=embedVar)
        await message.delete()
    elif message.content.startswith('!resetgt1'):
        gt1 = 100
        embedVar = discord.Embed(title="HP", description="This shows the HP of OUR structures! *and fuck jacob*",color=0x00ff00)
        embedVar.add_field(name="Guard Tower 1", value=gt1, inline=False)
        embedVar.add_field(name="Guard Tower 2", value=gt2, inline=False)
        embedVar.add_field(name="Holy Artifact", value=ha, inline=False)
        embedVar.add_field(name="Ogre Timer (may differ up to 3 secs)", value=datetime.timedelta(seconds=ogre),inline=False)
        await message2.edit(embed=embedVar)
        await message.delete()
    elif message.content.startswith('!resetgt2'):
        gt2 = 100
        embedVar = discord.Embed(title="HP", description="This shows the HP of OUR structures! *and fuck jacob*",color=0x00ff00)
        embedVar.add_field(name="Guard Tower 1", value=gt1, inline=False)
        embedVar.add_field(name="Guard Tower 2", value=gt2, inline=False)
        embedVar.add_field(name="Holy Artifact", value=ha, inline=False)
        embedVar.add_field(name="Ogre Timer (may differ up to 3 secs)", value=datetime.timedelta(seconds=ogre),inline=False)
        await message2.edit(embed=embedVar)
        await message.delete()
    elif message.content.startswith('.3'):
        ha -= 1
        embedVar = discord.Embed(title="HP", description="This shows the HP of OUR structures! *and fuck jacob*",color=0x00ff00)
        embedVar.add_field(name="Guard Tower 1", value=gt1, inline=False)
        embedVar.add_field(name="Guard Tower 2", value=gt2, inline=False)
        embedVar.add_field(name="Holy Artifact", value=ha, inline=False)
        embedVar.add_field(name="Ogre Timer (may differ up to 3 secs)", value=datetime.timedelta(seconds=ogre),inline=False)
        await message.delete()
    elif message.content.startswith('.1'):
        gt1 -= 1
        embedVar = discord.Embed(title="HP", description="This shows the HP of OUR structures! *and fuck jacob*",color=0x00ff00)
        embedVar.add_field(name="Guard Tower 1", value=gt1, inline=False)
        embedVar.add_field(name="Guard Tower 2", value=gt2, inline=False)
        embedVar.add_field(name="Holy Artifact", value=ha, inline=False)
        embedVar.add_field(name="Ogre Timer (may differ up to 3 secs)", value=datetime.timedelta(seconds=ogre),inline=False)
        await message.delete()
    elif message.content.startswith('.2'):
        gt2 -= 1
        embedVar = discord.Embed(title="HP", description="This shows the HP of OUR structures! *and fuck jacob*",color=0x00ff00)
        embedVar.add_field(name="Guard Tower 1", value=gt1, inline=False)
        embedVar.add_field(name="Guard Tower 2", value=gt2, inline=False)
        embedVar.add_field(name="Holy Artifact", value=ha, inline=False)
        embedVar.add_field(name="Ogre Timer (may differ up to 3 secs)", value=datetime.timedelta(seconds=ogre),inline=False)
        await message.delete()
    elif message.content.startswith('!ogre'):
        ogre = 606
        embedVar = discord.Embed(title="HP", description="This shows the HP of OUR structures! *and fuck jacob*",color=0x00ff00)
        embedVar.add_field(name="Guard Tower 1", value=gt1, inline=False)
        embedVar.add_field(name="Guard Tower 2", value=gt2, inline=False)
        embedVar.add_field(name="Holy Artifact", value=ha, inline=False)
        embedVar.add_field(name="Ogre Timer (may differ up to 3 secs)", value=datetime.timedelta(seconds=ogre),inline=False)
        await message.delete()
        await message2.edit(embed=embedVar)
    elif message.content.startswith('FUCK JACOB'):
        embedVar = discord.Embed(title="Fuck Jacob", description="Fuck Jacob", color=0x00ff00)
        embedVar.add_field(name="Fuck Jacob", value="Fuck Jacob", inline=False)
        embedVar.add_field(name="Fuck Jacob", value="Fuck Jacob", inline=False)
        embedVar.add_field(name="Fuck Jacob", value="Fuck Jacob", inline=False)
        embedVar.add_field(name="Fuck Jacob", value="Fuck Jacob", inline=False)
        await message.delete()
        await message2.edit(embed=embedVar)
@tasks.loop(seconds=3)
async def test():
    global ogre, message2, channel, ogremin, ogresec
    ogre -= 3
    ogremin = ogre // 60
    ogresec = (ogre - (ogremin * 60))
    embedVar = discord.Embed(title="HP", description="This shows the HP of OUR structures! *and fuck jacob*",color=0x00ff00)
    embedVar.add_field(name="Guard Tower 1", value=gt1, inline=False)
    embedVar.add_field(name="Guard Tower 2", value=gt2, inline=False)
    embedVar.add_field(name="Holy Artifact", value=ha, inline=False)
    embedVar.add_field(name="Ogre Timer (may differ up to 3 secs)", value=f'{ogremin} minutes and {ogresec} seconds',inline=False)
    await message2.edit(embed=embedVar)
bot.run(TOKEN)
