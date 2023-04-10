import discord
import asyncio
import os
from discord.ext import commands


bot = commands.Bot(command_prefix="!" , intents=discord.Intents.all())

BOT_TOKEN = "TOKEN"


class Bot(commands.Bot):
    
    def __init__(self) -> None:
        super().__init__(command_prefix='!',intents=discord.Intents.all(), application_id=1014919799085744259)

    async def on_ready(self):
        print(f"{self.user} is connected!!")
        await bot.change_presence(status=discord.Status.online, activity=discord.Game('/login | เพื่อเช็คร้านค้า'))
        


    async def setup_hook(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")
        await bot.tree.sync(guild=None)

    async def main():
        async with bot:
            #await load()
            await bot.start(BOT_TOKEN)
        

bot = Bot()
bot.run(BOT_TOKEN)
