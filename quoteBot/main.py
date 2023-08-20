import nextcord
import os
import config
from nextcord.ext import commands

intents = nextcord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="quote ", intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

if __name__ == '__main__':
    bot.run(config.TOKEN)