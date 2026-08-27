import discord, sys, traceback, asyncio, os, random
from discord.ext import commands
from discord.ext.commands.errors import BadArgument

token = 'OTE2NDM2NzU2ODEzOTc1NjI2.GF6YlJ.V5Z7AmgFnWQTML-mIYZU_lIE370AjchBZtMn3A'
intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix = '!', intents=intents)

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')
   

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('that'))
    #ea_sports = await client.fetch_user(476006484858109972)
    #await ea_sports.send('buenos noches')
    print('awake.')

@client.command(name = 'ping', help = 'returns bots ping in ms')
async def ping(ctx):
    await ctx.reply(f"Pong! {round(client.latency * 1000)}ms")




async def main():
    await client.load_extension('jishaku')
    await load()
    await client.start(token)
