import discord
from general.keep_alive import keep_alive
from general.command_handler import execute_command
from config.environment_keys import *
from util.constants import *
from config.strings import text_large_result

client = discord.Client()
  
@client.event
async def on_ready(): 
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): 
  if message.author == client.user: 
    return
  messageReceived = message.content
  print(messageReceived)
  if bot_mention in message.content:
    answer_message = str(execute_command(messageReceived))
    length = len(answer_message)
    if length < maximum_lenght_characters:
      await message.channel.send(answer_message)
    else:
      file = open(large_file_name,"w+")
      file.write(answer_message)
      file.close()
      with open(large_file_name, "rb") as file:
        await message.channel.send(text_large_result, file=discord.File(file, large_file_name))

keep_alive()
client.run(token)