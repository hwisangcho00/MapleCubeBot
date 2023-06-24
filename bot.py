import discord
from discord.ext import commands
import responses
import os
import random
import cubeProb
from CubeSimulator import CubeSimulator
from cubeIdx import cubeList, rankList, equipmentList

from dotenv import load_dotenv



async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():

    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='!', intents = intents, 
                       help_command=commands.MinimalHelpCommand())

    # client = discord.Client(intents=intents)

    @bot.event
    async def on_ready():   

        print(f'{bot.user} is now running!')

    # @bot.event
    # async def on_message(message):
    #     if message.author == bot.user:
    #         return
        
    #     username = str(message.author)
    #     user_message = str(message.content)
    #     channel = str(message.channel)

    #     print(f'{username} said: "{user_message}" ({channel})')

    #     if user_message[0] == '?':
    #         user_message = user_message[1:]
    #         await send_message(message, user_message, is_private=True)
    #     else:
    #         await send_message(message, user_message, is_private=False)
    
    @bot.command(name='hello')
    async def _hello(ctx):
        await ctx.send('Hey there!')

    @bot.command(name='cube')
    async def _cube(ctx, cubeName, rank, equipment, level):

        cubeName = cubeName.lower()
        rank = rank.lower()
        equipment = equipment.lower()
        
        if cubeName not in cubeList:
            await ctx.send(f'{cubeName} is not a valid cube')
            return

        if rank not in rankList:
            await ctx.send(f'{rank} is not a valid tier')
            return

        if equipment not in equipmentList:
            await ctx.send(f'{equipment} is not a valid equipment')
            return

        cs = CubeSimulator(cubeName, rank, equipment, level)
        
        cs.rollCube()

        await ctx.send(f'Rolling {cubeName} cube on lvl {level} {equipment}. Current rank : {rank}')



    bot.run(TOKEN)
