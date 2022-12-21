import discord
import asyncio
import sys
import requests
import riot_auth
from discord.ext import commands
from utils.api import *


class Command(commands.Cog):


    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Command.py is ready!!")

    @commands.command()
    async def embed(self,ctx):
        embed_message = discord.Embed(title="Title", description="Description",color= discord.Color.blue())
        embed_message.set_author(name=ctx.author, icon_url= ctx.author.avatar)
        embed_message.set_thumbnail(url=ctx.guild.icon)
        #embed_message.set_image(url=ctx.guild.icon)
        embed_message.add_field(name="Field Name", value="Field value",inline=False)
        #embed_message.set_footer(text="This is footer" , icon_url=ctx.author.avatar)

        await ctx.send(embed = embed_message)

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"Hi! {ctx.author.mention}")


    @commands.command()
    async def login(self,ctx, username : str , password : str):        
        r = await check_item_shop(username,password)
        print(r)


async def setup(client):
    await client.add_cog(Command(client))