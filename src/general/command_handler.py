from config.environment_keys import *
from util.constants import *
from util.string_helper import is_from_lichess_domain
from general.answer import get_game_pgn
from general.answer import get_game_id
from general.answer import get_confronts
from general.answer import get_game_gif
from general.answer import get_user_status, create_tournament_cafe
from util.string_helper import remove_bot_mention
from util.string_helper import remove_empty_spaces
from config.strings import text_puzzle_command
from config.strings import text_puzzle_answer_command
from config.strings import text_bot_mentioned_reply
from config.commands import *

def execute_command(message):
    message_to_send = ""
    if command_pgn_fix in message.lower() or command_pgn in message.lower():
        message_to_send = execute_command_pgn(message)
    elif command_cross_table_fix in message.lower() or command_cross_table in message.lower():
        message_to_send = execute_command_crosstable(message)
    elif command_profile_fix in message.lower() or command_profile in message.lower():
        message_to_send = execute_command_profile(message)
    elif command_tournament_cafe in message.lower():
        message_to_send = execute_command_tournament_cafe()
    elif liches_search_url in message:
        message_to_send = execute_command_gif(message)
    elif command_puzzle in message:
        message_to_send = execute_command_puzzle()
    elif command_puzzle_answer in message:
        message_to_send = execute_command_puzzle_answer()
    else:
        message_to_send = standard_bot_mention_reply()
    return(message_to_send)

def execute_command_pgn(message):
    text_message = remove_empty_spaces(remove_bot_mention(message).replace(command_pgn_fix, "").replace(command_pgn, ""))
    return(get_game_pgn(text_message))

def execute_command_crosstable(message):
    text_message = remove_empty_spaces(remove_bot_mention(message).replace(command_cross_table_fix, "").replace(command_cross_table, "")).lower()
    length = len(text_message)
    index_comma = text_message.find(",")
    player_one = text_message[0:index_comma]
    player_two = text_message[index_comma + 1:length]
    return(get_confronts(player_one, player_two))

def execute_command_gif(message):
    message_return = ""
    words = message.split()
    for word in words:
        print(word)
        if is_from_lichess_domain(word):
            message_return = get_game_gif(word)
            break
    return(message_return)

def execute_command_puzzle():
    return(text_puzzle_command)

def execute_command_puzzle_answer():
    return(text_puzzle_answer_command)

def standard_bot_mention_reply():
    return(text_bot_mentioned_reply)

def execute_command_profile(message):
    user = remove_empty_spaces(remove_bot_mention(message).replace(command_profile_fix, "").replace(command_profile, ""))
    print(user)
    return(get_user_status(user))

def execute_command_tournament_cafe():
    return(create_tournament_cafe())