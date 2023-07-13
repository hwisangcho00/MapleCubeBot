import discord
from discord.ext import commands
import responses
import os
import random
import cubeProb
from CubeSimulator import CubeSimulator
from cubeIdx import cubeList, rankList, equipmentList

from dotenv import load_dotenv

class MyHelp(commands.HelpCommand):
    def get_command_signature(self, command):
        return '%s%s %s' % (self.context.clean_prefix, command.qualified_name, command.signature)

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Help", color=discord.Color.blurple())

        for cog, commands in mapping.items():
           filtered = await self.filter_commands(commands, sort=True)
           command_signatures = [self.get_command_signature(c) for c in filtered]

           if command_signatures:
                cog_name = getattr(cog, "qualified_name", "No Category")
                embed.add_field(name=cog_name, value="\n".join(command_signatures), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(title=self.get_command_signature(command), color=discord.Color.random())
        if command.help:
            embed.description = command.help
        if alias := command.aliases:
            embed.add_field(name="Aliases", value=", ".join(alias), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

def run_discord_bot():

    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='!', intents = intents, 
                       help_command=commands.MinimalHelpCommand())

    bot.help_command = MyHelp()

    @bot.event
    async def on_ready():   

        print(f'{bot.user} is now running!')

    @bot.command(name='cube')
    async def cube(ctx, cubeName: str, rank: str, equipment:str , level: int):
        """testing!\nyes"""
        cubeName = cubeName.lower()
        rank = rank.lower()
        equipment = equipment.lower()
        
        if cubeName not in cubeList:
            await ctx.send(f'{cubeName} is not a valid cube')
            return

        if rank not in rankList:
            await ctx.send(f'{rank} is not a valid tier')
            return

        if rank != 'legendary':
            await ctx.send("Currently only legendary rank is supported")
            return

        if equipment not in equipmentList:
            await ctx.send(f'{equipment} is not a valid equipment')
            return

        if not 120 <= level <= 250:
            await ctx.send("Please input value between 120 and 250")
            return

        cs = CubeSimulator(cubeName, rank, equipment, level)
        
        res = cs.rollCube()
        
        embed = discord.Embed(title="Cube result")
        embed.add_field(name = f'Rolling {cubeName} cube on lvl {level} {equipment}. Current rank : {rank} \n', value = res)

        await ctx.reply(embed=embed, mention_author=False)

    bot.run(TOKEN)
