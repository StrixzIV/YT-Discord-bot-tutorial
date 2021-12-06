import os
import dotenv
from discord.ext import commands

dotenv.load_dotenv()

client = commands.Bot(command_prefix = '#!')

@client.event
async def on_ready():
    print(f'Successfully logged in as {client.user}')


@client.event
async def on_message(message):
    await client.process_commands(message)


# Commands

@client.command()
async def hello(ctx):
    await ctx.channel.send(f'Hello! {ctx.author}')


token = os.getenv('TOKEN')
client.run(token)