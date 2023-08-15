import discord
from discord import app_commands
from discord.ext import commands
import os
from CubeSimulator import CubeSimulator
from cubeIdx import cubeList, tierList, equipmentList, tierIdx
from RankUpSimulator import TierUpSimulator
from DatabaseConnector import DatabaseConnector


from dotenv import load_dotenv


class MyHelp(commands.HelpCommand):
    """
    A class that overrides the bots default help command
    """
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
    """
    Central method that initiates and runs the discord bot.\\
    Defines specific commands for the bot.
    """

    load_dotenv()
    TEST_TOKEN = os.getenv('TEST_TOKEN')
    TOKEN = os.getenv('DISCORD_TOKEN')

    dc = DatabaseConnector()

    # Bot initialization
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents = intents, 
                       help_command=commands.MinimalHelpCommand())
    bot.help_command = MyHelp()

    @bot.event
    async def on_ready():   
        print(f'{bot.user} is now running!')
        try:
           synced = await bot.tree.sync()
           print(f"Synced {len(synced)} command(s)")
        except Exception as e:
           print(e, "bot tree sync")

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
          await ctx.send("Please pass in all required arguments. Type <!help cube> for more information.")

    @bot.tree.command(name="miracle", description="Simulate tier ups during DMT")
    @app_commands.describe(cube_name = "glowing / bright", start_tier = "rare / epic / unique", target_tier = "epic / unique / legendary", repetition = "Number of tier up simulations")
    async def miracle(interaction: discord.Interaction, cube_name:str, start_tier:str, target_tier:str, repetition: str):
        """
        cube_name: glowing / bright
        start_tier: rare, epic, unique
        target_tier: epic, unique, legendary
        repetition: 1 ~ 200
        """
        cube_name = cube_name.lower()
        start_tier = start_tier.lower()
        target_tier = target_tier.lower()

        if cube_name not in cubeList:
          await interaction.response.send_message(f'Error (cubeName): {cube_name} is not a valid cube')
          return
        
        if start_tier not in tierList:
          await interaction.response.send_message(f'Error (startRank): {start_tier} is not a valid tier')
          return
        
        if target_tier not in tierList:
          await interaction.response.send_message(f'Error (targetRank): {target_tier} is not a valid tier')
        
          return
        
        if tierIdx[start_tier] >= tierIdx[target_tier]:
          await interaction.response.send_message(f'Error (startRank, targetRank): startRank must be a strictly lower rank than targetRank')
          return
        
        if not repetition.isnumeric(): 
          await interaction.response.send_message("Error (repetition): Please input a numeric value between 1 and 200")
          return

        repetition = int(repetition)

        if not 1 <= repetition <= 200:
          await interaction.response.send_message("Error (repetition): Please input value between 1 and 200")
          return

        rus = TierUpSimulator(cube_name, start_tier, target_tier)

        res = rus.miracleTierUp(repetition)

        embed = discord.Embed(title="Miracle day result", color = discord.Color.pink())
        embed.add_field(name = f'Rolling {cube_name} cube', value = res)

        await interaction.response.send_message(embed=embed)

        dc.incrementLog("miracle")


    @bot.tree.command(name="tier", description="Simulate regular tier ups")
    @app_commands.describe(cube_name = "glowing / bright", start_tier = "rare / epic / unique", target_tier = "epic / unique / legendary", repetition = "Number of tier up simulations")
    async def tier(interaction: discord.Interaction, cube_name:str, start_tier:str, target_tier:str, repetition: str):
        """
        cube_name: glowing / bright
        start_tier: rare, epic, unique
        target_tier: epic, unique, legendary
        repetition: 1 ~ 200
        """
        cube_name = cube_name.lower()
        start_tier = start_tier.lower()
        target_tier = target_tier.lower()

        if cube_name not in cubeList:
          await interaction.response.send_message(f'Error (cubeName): {cube_name} is not a valid cube')
          return
        
        if start_tier not in tierList:
          await interaction.response.send_message(f'Error (startRank): {start_tier} is not a valid tier')
          return
        
        if target_tier not in tierList:
          await interaction.response.send_message(f'Error (targetRank): {target_tier} is not a valid tier')
        
          return
        
        if tierIdx[start_tier] >= tierIdx[target_tier]:
          await interaction.response.send_message(f'Error (startRank, targetRank): startRank must be a strictly lower rank than targetRank')
          return
        
        if not repetition.isnumeric(): 
          await interaction.response.send_message("Error (repetition): Please input a numeric value between 1 and 200")
          return

        repetition = int(repetition)

        if not 1 <= repetition <= 200:
          await interaction.response.send_message("Error (repetition): Please input value between 1 and 200")
          return

        rus = TierUpSimulator(cube_name, start_tier, target_tier)

        res = rus.tierUp(repetition)

        embed = discord.Embed(title="Tier up result", color = discord.Color.pink())
        embed.add_field(name = f'Rolling {cube_name} cube', value = res)

        await interaction.response.send_message(embed=embed)

        dc.incrementLog("tier")

    @bot.tree.command(name="cube", description="Simulate cubing for 3-line legendary potentials")
    @app_commands.describe(cube_name = "glowing / bright", equipment = "weapon / emblem / secondary / eye / face / earrings / pendant / ring / hat / top / overall / bottom", level = "120 ~ 250")
    async def cube(interaction: discord.Interaction, cube_name: str, equipment:str , level: str):
        """
        Returns the appropriate 3-line legendary potentials

        cube_name: glowing / bright
        equipment: weapon / emblem / secondary / eye / face / earrings / pendant / ring / hat / top / overall / bottom

        level: 120 ~ 250
        """

        cube_name = cube_name.lower()
        equipment = equipment.lower()
        
        # Error handling
        if cube_name not in cubeList:
            await interaction.response.send_message(f'Error (cube_name): {cube_name} is not a valid cube')
            return

        if equipment not in equipmentList:
            await interaction.response.send_message(f'Error (equipment): {equipment} is not a valid equipment')
            return

        if not level.isnumeric(): 
            await interaction.response.send_message("Error (level): Please input a numeric value between 120 and 250")
            return

        level = int(level)

        if not 120 <= level <= 250:
            await interaction.response.send_message("Error (level): Please input value between 120 and 250")
            return

        # Roll cubes
        cs = CubeSimulator(cube_name, equipment, level)
        
        res = cs.rollCube()
        
        # Put the result in to Embed
        embed = discord.Embed(title="Cube result", color = discord.Color.green())
        embed.add_field(name = f'Rolling {cube_name} cube on lvl {level} {equipment}. Tier : Legendary \n', value = res)

        # Send reply
        await interaction.response.send_message(embed=embed)

        dc.incrementLog("cube")

    # Actually run the bot
    # bot.run(TOKEN)
    # Test Option
    bot.run(TEST_TOKEN)



if __name__ == '__main__':
  run_discord_bot()
  