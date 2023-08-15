import discord
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

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
          await ctx.send("Please pass in all required arguments. Type <!help cube> for more information.")

    @bot.command(name='miracle')
    async def miracle(ctx, cubeName:str, startTier:str, targetTier:str, repetition: str):
        """
        cubeName: glowing / bright
        startTier: rare, epic, unique
        targetTier: epic, unique, legendary
        repetition: 1 ~ 200
        """
        cubeName = cubeName.lower()
        startTier = startTier.lower()
        targetTier = targetTier.lower()

        if cubeName not in cubeList:
          await ctx.send(f'Error (cubeName): {cubeName} is not a valid cube')
          return
        
        if startTier not in tierList:
          await ctx.send(f'Error (startRank): {startTier} is not a valid tier')
          return
        
        if targetTier not in tierList:
          await ctx.send(f'Error (targetRank): {targetTier} is not a valid tier')
          return
        
        if tierIdx[startTier] >= tierIdx[targetTier]:
          await ctx.send(f'Error (startRank, targetRank): startRank must be a strictly lower rank than targetRank')
          return
        
        if not repetition.isnumeric(): 
            await ctx.send("Error (repetition): Please input a numeric value between 1 and 200")
            return

        repetition = int(repetition)

        if not 1 <= repetition <= 200:
            await ctx.send("Error (repetition): Please input value between 1 and 200")
            return

        rus = TierUpSimulator(cubeName, startTier, targetTier)

        res = rus.miracleTierUp(repetition)

        embed = discord.Embed(title="Miracle day result", color = discord.Color.pink())
        embed.add_field(name = f'Rolling {cubeName} cube', value = res)

        await ctx.reply(embed=embed, mention_author=False)

        dc.incrementLog("miracle")

    @bot.command(name='tier')
    async def tier(ctx, cubeName:str, startTier:str, targetTier:str, repetition: str):
        """
        cubeName: glowing / bright
        startTier: rare, epic, unique
        targetTier: epic, unique, legendary
        repetition: 1 ~ 200
        """
        cubeName = cubeName.lower()
        startTier = startTier.lower()
        targetTier = targetTier.lower()

        if cubeName not in cubeList:
          await ctx.send(f'Error (cubeName): {cubeName} is not a valid cube')
          return
        
        if startTier not in tierList:
          await ctx.send(f'Error (startTier): {startTier} is not a valid tier')
          return
        
        if targetTier not in tierList:
          await ctx.send(f'Error (targetTier): {targetTier} is not a valid tier')
          return
        
        if tierIdx[startTier] >= tierIdx[targetTier]:
          await ctx.send(f'Error (startTier, targetTier): startTier must be a strictly lower tier than targetTier')
          return
        
        if not repetition.isnumeric(): 
            await ctx.send("Error (repetition): Please input a numeric value between 1 and 200")
            return

        repetition = int(repetition)

        if not 1 <= repetition <= 200:
            await ctx.send("Error (repetition): Please input value between 1 and 200")
            return

        rus = TierUpSimulator(cubeName, startTier, targetTier)

        res = rus.tierUp(repetition)

        embed = discord.Embed(title="Tier up result", color = discord.Color.pink())
        embed.add_field(name = f'Rolling {cubeName} cube', value = res)

        await ctx.reply(embed=embed, mention_author=False)

        dc.incrementLog("tier")


    @bot.command(name='cube')
    async def cube(ctx, cubeName: str, equipment:str , level: str):
        """
        Returns the appropriate 3-line legendary potentials

        cubeName: glowing / bright
        equipment: weapon / emblem / secondary / eye / face / earrings / pendant / ring / hat / top / overall / bottom
        level: 120 ~ 250
        """
        cubeName = cubeName.lower()
        equipment = equipment.lower()
        
        # Error handling
        if cubeName not in cubeList:
            await ctx.send(f'Error (cubeName): {cubeName} is not a valid cube')
            return

        if equipment not in equipmentList:
            await ctx.send(f'Error (equipment): {equipment} is not a valid equipment')
            return

        if not level.isnumeric(): 
            await ctx.send("Error (level): Please input a numeric value between 120 and 250")
            return

        level = int(level)

        if not 120 <= level <= 250:
            await ctx.send("Error (level): Please input value between 120 and 250")
            return

        # Roll cubes
        cs = CubeSimulator(cubeName, equipment, level)
        
        res = cs.rollCube()
        
        # Put the result in to Embed
        embed = discord.Embed(title="Cube result", color = discord.Color.green())
        embed.add_field(name = f'Rolling {cubeName} cube on lvl {level} {equipment}. Tier : Legendary \n', value = res)

        # Send reply
        await ctx.reply(embed=embed, mention_author=False)

        dc.incrementLog("cube")

    # Actually run the bot
    bot.run(TOKEN)
    # Test Option
    # bot.run(TEST_TOKEN)



if __name__ == '__main__':
  run_discord_bot()
  