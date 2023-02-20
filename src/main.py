import discord , os
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

@bot.event
async def on_ready():
    print(f'logged in as: {bot.user.name}')
    await bot.change_presence(status=discord.Status.idle, activity = discord.Streaming(name=f"Version 1.1 | !help", url="https://www.twitch.tv/discord"))


for f in os.listdir("./cogs"):
	if f.endswith(".py"):
		bot.load_extension("cogs." + f[:-3])

# Please replace botToken = os.environ['TOKEN'] WITH botToken="<PUT YOUR TOKEN HERE>" IF you are not using docker
# botToken="<PUT YOUR TOKEN HERE>"

		
botToken = os.environ['TOKEN']

bot.run(botToken)
