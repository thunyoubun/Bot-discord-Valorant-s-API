import discord
import asyncio
import os
from discord.ext import commands


bot = commands.Bot(command_prefix="!" , intents=discord.Intents.all())

BOT_TOKEN = "BOT_TOKEN"


    
@bot.event
async def on_ready():
    print(f"{bot.user} is connected!!")


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start(BOT_TOKEN)

asyncio.run(main())
