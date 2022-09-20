import requests
from api.lichess.lichess import get_confronts_between_two_players, export_game_gif, get_user_status_response, export_game_pgn, get_game_id
from util.constants import *
from api.lichess.http import *
from config.strings import *


def get_game_pgn(text_message):
    game_id = get_game_id(text_message)
    pgn = export_game_pgn(game_id)
    return(pgn)
  
def get_game_gif(url):
    game_id = get_game_id(url)
    url_gif =  export_game_gif(game_id)
    return(url_gif)

def number_of_matches_played(number_matches):
  result = "**" + str(number_matches)
  if number_matches != 1:
    result += "** vezes."
  else:
    result += "** vez."
  return(result)

def get_confronts(player_one, player_two):
    response = get_confronts_between_two_players(player_one, player_two)
    if response != None:
        json_users = response["users"]
        result = export_confronts_result(player_one, player_two, response, json_users)
        return(result)
    else:
        return(text_no_info_found)

def export_confronts_result(player_one, player_two, json_response, json_users):
    player_one_score = json_users[player_one]
    player_two_score = json_users[player_two]
    number_matches = json_response["nbGames"]
    return(
        f"{text_the_players} **" 
        + player_one 
        + f"** {text_and} **" 
        + player_two 
        + f"** {text_already_played_plural} " 
        + number_of_matches_played(number_matches) 
        + "\n\n" 
        + f"*{text_result}:*\n" 
        + "**" 
        + player_one + "** [" + str(player_one_score) + "] x [" + str(player_two_score) + "] **" + player_two + "**"
    )

def get_user_status(user_name):
    response = get_user_status_response(user_name)
    if response != None:
        result = export_user_status(user_name, response)
        return(result)
    else:
        return(text_no_info_found)
    
def export_user_status(user_name, response):
    categories = response["perfs"]

    bullet = categories["bullet"]
    bullet_mathes = bullet["games"]
    bullet_rating = bullet["rating"]

    blitz = categories["blitz"]
    blitz_mathes = blitz["games"]
    blitz_rating = blitz["rating"]

    rapid = categories["rapid"]
    rapid_mathes = rapid["games"]
    rapid_rating = rapid["rating"]
    
    classical = categories["classical"]
    classical_mathes = classical["games"]
    classical_rating = classical["rating"]

    correspondence = categories["correspondence"]
    correspondence_mathes = correspondence["games"]
    correspondence_rating = correspondence["rating"]

    all_matches = response["count"]
    total_matches = all_matches["all"]
    won_mathes = all_matches["win"]
    lose_mathes = all_matches["loss"]
    draw_mathes = all_matches["draw"]

    url_user = response["url"]

    return(
        f"**{user_name}** {text_already_played} **{total_matches}** {text_matches_on_lichess}:\n"
        + f"**{text_voctories}:** {won_mathes}\n"
        + f"**{text_loses}:** {lose_mathes}\n"
        + f"**{text_draw}:** {draw_mathes}"
        + "\n\n"
        + f"**__{text_classical_matches}__**\n"
        + f"**{text_total_matches_played}:** {classical_mathes}\n"
        + f"**Rating:** {classical_rating}"
        + "\n\n"
        + f"**__{text_rapid_matches}__**\n"
        + f"**{text_total_matches_played}:** {rapid_mathes}\n"
        + f"**Rating:** {rapid_rating}"
        + "\n\n"
        + f"**__{text_blitz_matches}__**\n"
        + f"**{text_total_matches_played}:** {blitz_mathes}\n"
        + f"**Rating:** {blitz_rating}"
        + "\n\n"
        + f"**__{text_bullet_matches}__**\n"
        + f"**{text_total_matches_played}:** {bullet_mathes}\n"
        + f"**Rating:** {bullet_rating}"
        + "\n\n"
        + f"**__{text_correspondence_matches}__**\n"
        + f"**{text_total_matches_played}:** {correspondence_mathes}\n"
        + f"**Rating:** {correspondence_rating}"
        + "\n\n"
        + f"{text_profile_lichess}: {url_user}"
    )