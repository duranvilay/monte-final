import discord
import os
import random
from dotenv import load_dotenv
from ec2_metadata import ec2_metadata 

load_dotenv() 

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)
token = str(os.getenv('TOKEN'))

print(f'This is my Ec2_metadata.region:', ec2_metadata.region)
print(f'This is my Ec2_metadata.instance.id:', ec2_metadata.instance_id)

@client.event #<--Fix
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    
    
    print(f'Message {user_message} by {username} on {channel}')

    
    if message.author == client.user:
        return 
    
    
    if channel == "hi":
        if user_message.lower() == "test" or user_message.lower() == "test":
            await message.channel.send(f"okay! {username} Your EC2 Data: {ec2_metadata.region}")
            return 
        
        elif user_message.lower() == "hello?":
            await message.channel.send(f'Sooner! {username}')
            
         
        elif user_message.lower() == "EC2 Data":
            await message.channel.send("Your instance data is" + ec2_metadata.region)
        

client.run(token)