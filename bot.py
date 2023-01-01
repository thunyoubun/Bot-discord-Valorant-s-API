import discord
import asyncio
import os
from discord.ext import commands


bot = commands.Bot(command_prefix="!" , intents=discord.Intents.all())

BOT_TOKEN = "MTAxNDkxOTc5OTA4NTc0NDI1OQ.Gn4th5.gmXaQUntDNO7UPmu0o4xZT81sfGMAi9QgHU8ic"


    
@bot.event
async def on_ready():
    print(f"{bot.user} is connected!!")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('!login username password | เพื่อเช็คร้านค้า'))
    


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start(BOT_TOKEN)

asyncio.run(main())