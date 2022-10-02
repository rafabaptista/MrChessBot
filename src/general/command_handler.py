from config.environment_keys import *
from model.tournament import Tournament
from util.constants import *
from util.string_helper import is_from_lichess_domain, remove_tournament_keys
from general.answer import get_game_pgn
from general.answer import get_confronts
from general.answer import get_game_gif
from general.answer import get_user_status
from general.cxgr.cxgr_tournaments import create_tournament_list
from general.cxgr.cxgr_tournaments import create_swis_tournament_with_params
from general.cxgr.cxgr_tournaments import create_arena_tournament_with_params
from util.string_helper import remove_empty_spaces, remove_comma, remove_bot_mention
from config.strings import text_puzzle_command
from config.strings import text_puzzle_answer_command
from config.strings import bot_helper
from config.commands import *

def execute_command(message):
    message_to_send = ""
    if command_pgn_fix in message.lower() or command_pgn in message.lower():
        message_to_send = execute_command_pgn(message)
    elif command_cross_table_fix in message.lower() or command_cross_table in message.lower():
        message_to_send = execute_command_crosstable(message)
    elif command_profile_fix in message.lower() or command_profile in message.lower():
        message_to_send = execute_command_profile(message)
    elif command_tournament_list_p1 in message.lower():
        message_to_send = execute_command_tournament(Tournament.Type.P1, message)
    elif command_tournament_list_p2 in message.lower():
        message_to_send = execute_command_tournament(Tournament.Type.P2, message)
    elif command_tournament_list_p3 in message.lower():
        message_to_send = execute_command_tournament(Tournament.Type.P3, message)
    elif command_tournament_list_p4 in message.lower():
        message_to_send = execute_command_tournament(Tournament.Type.P4, message)
    elif command_swiss_tournament in message:
        message_to_send = execute_command_swiss(message)
    elif command_arena_tournament in message:
        message_to_send = execute_command_arena(message)
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
    return(bot_helper)

def execute_command_profile(message):
    user = remove_empty_spaces(remove_bot_mention(message).replace(command_profile_fix, "").replace(command_profile, ""))
    print(user)
    return(get_user_status(user))

def execute_command_swiss(message):
    print(message)
    tournament_params = remove_bot_mention(message).replace(command_swiss_tournament, "")
    return(create_swis_tournament_with_params(tournament_params))

def execute_command_arena(message):
    print(message)
    tournament_params = remove_bot_mention(message).replace(command_arena_tournament, "")
    return(create_arena_tournament_with_params(tournament_params))

def execute_command_tournament(type, message):
    print(type)
    print(message)
    if "," in message:
        message = remove_bot_mention(message)
        command = remove_tournament_keys(message)
        extra_message = command.replace(",", "", 1)
        return(create_tournament_list(type, extra_message))
    return(create_tournament_list(type))