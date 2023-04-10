import discord
from discord import app_commands
from discord.ext import commands
from utils.api import *


class command(commands.Cog):

    def __init__(self, bot:commands.Bot)-> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Command.py is ready!!")

    @app_commands.command(name="ping",description="ping Paimon")
    async def ping(self,interaction:discord.Interaction):
        await interaction.response.send_message(f"Hi! {interaction.user.mention}")

    # @app_commands.command(name="embed",description="test embed")
    # async def embed(self,interaction:discord.Interaction):
    #     embed_message = discord.Embed(title="Title", description="Description",color= discord.Color.blue())
    #     embed_message.set_author(name=interaction.user.name, icon_url= interaction.user.avatar)
    #     embed_message.set_thumbnail(url=interaction.guild.icon)
    #     #embed_message.set_image(url=interaction.guild.icon)
    #     embed_message.add_field(name="Field Name", value="Field value",inline=False)
    #     #embed_message.set_footer(text="This is footer" , icon_url=interaction.author.avatar)
    #     await interaction.response.send_message(embed = embed_message)

    @app_commands.command(name="login",description="login to check dailyshop")
    async def login(self,interaction:discord.Interaction, username : str , password : str):
        await interaction.response.defer()
        skin_data = await check_item_shop(username,password)
        #print(skin_data)

        # embed = discord.Embed(title=skin_data["bundle_name"])
        # embed.set_image(url=skin_data["bundle_image"])
        # await ctx.send(embed=embed)
        
        embed = discord.Embed(title=f"Daily store for {interaction.user} | Remaining in {int(skin_data['SingleItemOffersRemainingDurationInSeconds']/3600)} hour" ,color= discord.Color.random())
        embed.set_author(name=interaction.user, icon_url= interaction.user.avatar)
        await interaction.followup.send(embed=embed)
        try:
            
            embed = discord.Embed(title=f"{skin_data['skin1_name']}", description= f"{skin_data['skin1_price']}" ,color= discord.Color.blue())
            if skin_data["skin1_image"] != None:
                embed.set_thumbnail(url=skin_data["skin1_image"])    
            await interaction.followup.send(embed=embed)

            embed = discord.Embed(title=f"{skin_data['skin2_name']}", description= f"{skin_data['skin2_price']}" ,color= discord.Color.blue())
            if skin_data["skin2_image"] != None:
                embed.set_thumbnail(url=skin_data["skin2_image"])    
            await interaction.followup.send(embed=embed)

            embed = discord.Embed(title=f"{skin_data['skin3_name']}", description= f"{skin_data['skin3_price']}" ,color= discord.Color.blue())
            if skin_data["skin3_image"] != None:
                embed.set_thumbnail(url=skin_data["skin3_image"])    
            await interaction.followup.send(embed=embed)

            embed = discord.Embed(title=f"{skin_data['skin4_name']}", description= f"{skin_data['skin4_price']}" ,color= discord.Color.blue())
            if skin_data["skin4_image"] != None:
                embed.set_thumbnail(url=skin_data["skin4_image"])    
            await interaction.followup.send(embed=embed)
            
        except TypeError:
            embed = discord.Embed(title=f"{skin_data['skin1_name']}", description= f"{skin_data['skin1_price']}" ,color= discord.Color.blue())
            embed.set_thumbnail(url=skin_data["skin1_image"])    
            await interaction.followup.send(embed=embed)

            embed = discord.Embed(title=f"{skin_data['skin2_name']}", description= f"{skin_data['skin2_price']}" ,color= discord.Color.blue())
    
            embed.set_thumbnail(url=skin_data["skin2_image"])    
            await interaction.followup.send(embed=embed)

            embed = discord.Embed(title=f"{skin_data['skin3_name']}", description= f"{skin_data['skin3_price']}" ,color= discord.Color.blue())
            embed.set_thumbnail(url=skin_data["skin3_image"])    
            await interaction.followup.send(embed=embed)

            embed = discord.Embed(title=f"{skin_data['skin3_name']}", description= f"{skin_data['skin4_price']}" ,color= discord.Color.blue())
            embed.set_thumbnail(url=skin_data["skin4_image"])    
            await interaction.followup.send(embed=embed)

            


async def setup(bot:commands.Bot)-> None:
    await bot.add_cog(command(bot),guild=None)
