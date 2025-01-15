import discord
from discord import ui, app_commands
from discord.ext import commands, tasks
from discord.ext.commands import Bot, has_permissions, CheckFailure

bot = commands.Bot(command_prefix="!",intents=discord.Intents.all(), help_command=None) 

@bot.event
async def on_ready():
    
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    print("done but yippee")
    
        
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=f"blackjack")) 
    await bot.tree.sync()
    print('synced')
    target_guild_id = 1200957190471700621

bot.run("")