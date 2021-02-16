import discord
from discord.ext import tasks
from configparser import ConfigParser
import sqlite3

def config(section, filename = '.env'): #constants initizalization /opt/inetra_stat/.ENV
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section
    result = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            result[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return result


token = config('discord')['token']
intents = discord.Intents.all()

client = discord.Client(intents=intents)

# unheilbar id 520447922307858433
# sharen id 342602246225133568
# little lady id 746166385054449782

admins = []

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    for member in client.get_all_members():
        if (member.id == 520447922307858433 or member.id == 342602246225133568) and member not in admins:
            admins.append(member)
    send_admin.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        print(admins)

@tasks.loop(minutes=10, count=100)
async def send_admin():
    for i in admins:
        await i.send('fuck you')

client.run(token)