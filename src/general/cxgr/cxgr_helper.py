from config.commands import command_swiss_tournament, command_arena_tournament
from util.constants import torneio_word
from config.environment_keys import administrators_role

def is_user_has_permission_to_create_tournaments(roles) -> bool:
    result = next((x for x in roles if x.name == administrators_role), None)
    if (result != None):
        return(True)
    return(False)

def is_message_for_tournament_creation(message) -> bool:
    if ((f".{torneio_word}" in message) or (command_swiss_tournament in message) or (command_arena_tournament in message)):
        return(True)
    return(False)