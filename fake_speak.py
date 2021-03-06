import discord
from Mimicry import Mimicry
from twitterScraper import twitterScraper
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

#Get the configuration from the config file
with open("credentials.config", 'r') as f:
    configuration = json.load(f)
twitter_user  = configuration['twitter_user']
discord_token = configuration['discord_token']

#First, generate a global client we can use to talk to discord
client = discord.Client()
#Lets the console know we've successfully logged in
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('Fetching Tweets from '+twitter_user+'...')
    tweet_texts = twitterScraper.getTweetsAsString(twitter_user)
    print('Fetched Tweets. Saving to file.')
    with open('text_dumps/'+twitter_user+'.txt', 'w') as f:
        f.write(tweet_texts)
    print('Saved Tweets to file. Running application...')
    
    

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
        wisdom = Mimicry.mimic('text_dumps/'+twitter_user+'.txt',length, chaos)
        #Sent that insult to the discord channel
        await message.channel.send('Child, here is my wisdom for you... '+wisdom)
        print('Sent messags...\n'+wisdom+'\n\n')


#Run the client
try:
    client.run(discord_token)
except Exception as e:
    print(e)
sleep(5)


