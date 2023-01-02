import discord
import requests
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
        skin_data = await check_item_shop(username,password)
        #print(skin_data)

        # embed = discord.Embed(title=skin_data["bundle_name"])
        # embed.set_image(url=skin_data["bundle_image"])
        # await ctx.send(embed=embed)
        
        embed = discord.Embed(title=f"Daily store for {ctx.author} | Remaining in {int(skin_data['SingleItemOffersRemainingDurationInSeconds']/3600)} hour" ,color= discord.Color.random())
        embed.set_author(name=ctx.author, icon_url= ctx.author.avatar)
        await ctx.send(embed=embed)
        try:
            
            embed = discord.Embed(title=f"{skin_data['skin1_name']}", description= f"{skin_data['skin1_price']}" ,color= discord.Color.blue())
            if skin_data["skin1_image"] != None:
                embed.set_thumbnail(url=skin_data["skin1_image"])    
            await ctx.send(embed=embed)

            embed = discord.Embed(title=f"{skin_data['skin2_name']}", description= f"{skin_data['skin2_price']}" ,color= discord.Color.blue())
            if skin_data["skin2_image"] != None:
                embed.set_thumbnail(url=skin_data["skin2_image"])    
            await ctx.send(embed=embed)

            embed = discord.Embed(title=f"{skin_data['skin3_name']}", description= f"{skin_data['skin3_price']}" ,color= discord.Color.blue())
            if skin_data["skin3_image"] != None:
                embed.set_thumbnail(url=skin_data["skin3_image"])    
            await ctx.send(embed=embed)

            embed = discord.Embed(title=f"{skin_data['skin4_name']}", description= f"{skin_data['skin4_price']}" ,color= discord.Color.blue())
            if skin_data["skin4_image"] != None:
                embed.set_thumbnail(url=skin_data["skin4_image"])    
            await ctx.send(embed=embed)
            
        except TypeError:
            embed = discord.Embed(title=f"{skin_data['skin1_name']}", description= f"{skin_data['skin1_price']}" ,color= discord.Color.blue())
            embed.set_thumbnail(url=skin_data["skin1_image"])    
            await ctx.send(embed=embed)

            embed = discord.Embed(title=f"{skin_data['skin2_name']}", description= f"{skin_data['skin2_price']}" ,color= discord.Color.blue())
    
            embed.set_thumbnail(url=skin_data["skin2_image"])    
            await ctx.send(embed=embed)

            embed = discord.Embed(title=f"{skin_data['skin3_name']}", description= f"{skin_data['skin3_price']}" ,color= discord.Color.blue())
            embed.set_thumbnail(url=skin_data["skin3_image"])    
            await ctx.send(embed=embed)

            embed = discord.Embed(title=f"{skin_data['skin3_name']}", description= f"{skin_data['skin4_price']}" ,color= discord.Color.blue())
            embed.set_thumbnail(url=skin_data["skin4_image"])    
            await ctx.send(embed=embed)

            


async def setup(client):
    await client.add_cog(Command(client))