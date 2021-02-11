import discord
import Mimicry
import random
from time import sleep
import json
# This bot casts Vicious Mockery on an unfortunate soul in a discord channel.
#  This is done by typing the command
#
#   !mock @nameOfPerson
#
#The URL for our bot is
#
# "https://discord.com/api/oauth2/authorize?client_id=808865476540366948&permissions=75776&scope=bot"
#
#Enjoy. With great power, comes great responsibility


#First, generate a global client we can use to talk to discord
client = discord.Client()

#Lets the console know we've successfully logged in
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#When we receive a message...
@client.event
async def on_message(message):
    #Split the message into it's sections
    message_parts = message.content.split(' ')
    #If the message is a mock command
    if (message_parts[0].lower() == '!wisdom'):
        if len(message_parts)>1:
            try:
                chaos = min(max(2, int(message_parts[1])),8)
            except (ValueError, IndexError):
                chaos = round((random.randint(3,6) + random.randint(3,6) + random.randint(3, 6))/3)
        else:
            chaos = int((random.randint(3,6) + random.randint(3, 6))/2)
        #Generate a wisdom
        length = random.randint(1,4)
        wisdom = Mimicry.mimic('text_dumps/dalai_lama.txt',length, chaos)
        #Sent that insult to the discord channel
        await message.channel.send('Child, here is my wisdom for you... '+wisdom)

#Get our token from the config file
with open('credentials.config', 'r') as f:
    credentials = json.load(f)
    token = credentials["discord_token"]

#Run the client
try:
    client.run(token)
except Exception as e:
    print(e)
sleep(5)


