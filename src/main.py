import discord
#from general.keep_alive import keep_alive
from general.command_handler import execute_command
from config.environment_keys import *
from util.constants import *
from config.strings import text_large_result
from config.commands import command_initial

client = discord.Client()
  
@client.event
async def on_ready(): 
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): 
  if message.author == client.user: 
    return
  message_received = message.content
  print(message_received)
  if message_received.startswith(command_initial) or bot_mention in message_received or bot_name in message_received.lower():
    answer_message = str(execute_command(message_received))
    length = len(answer_message)
    if length < maximum_lenght_characters:
      await message.channel.send(answer_message)
    else:
      file = open(large_file_name,"w+")
      file.write(answer_message)
      file.close()
      with open(large_file_name, "rb") as file:
        await message.channel.send(text_large_result, file=discord.File(file, large_file_name))

#keep_alive()
client.run(token)