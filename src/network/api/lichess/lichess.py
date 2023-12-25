import json
import requests
from model.arena import Arena
from model.swiss import Swiss
from util.constants import *
from network.api.lichess.http import *
from util.string_helper import remove_quote
from util.string_helper import remove_url_scheme
from config.strings import text_match_not_found

def export_game_pgn(game_id):
    requestUrl = f"{http_get_game_pgn}{game_id}"
    headers = chess_pgn_header
    try:
        print("Url: " + requestUrl)
        response = requests.get(requestUrl, headers=headers, timeout=5)
        response.raise_for_status()
        print("Response Status Code: " + str(response.status_code))
        pgn = response.text
        return(pgn)
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)
    return(text_match_not_found)

def export_game_gif(game_id):
    return(f"{http_export_game_gif}{game_id}.gif")

def get_game_id(url_game):
    url_text = handle_url_game(url_game)
    game_id = url_text[0:8]
    print(game_id)
    return(game_id)

def handle_url_game(url_game):
    url_no_quotes = remove_quote(url_game)
    url_no_scheme = remove_url_scheme(url_no_quotes)
    url = url_no_scheme.replace(liches_search_url + "/", "")
    return(url)

def get_confronts_between_two_players(player_one, player_two):
    requestUrl = f"{http_crosstable}{player_one}/{player_two}"
    headers = json_header
    try:
        print("Url: " + requestUrl)
        response = requests.get(requestUrl, headers=headers, timeout=5)
        response.raise_for_status()
        print("Response Status Code: " + str(response.status_code))
        json_response = response.json()
        print(json_response)
        print(json_response["users"])
        return(json_response)
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)
    return(None)

def get_user_status_response(user_name):
    request_url = f"{http_get_user}{user_name}"
    headers = json_header
    try:
        print("Url: " + request_url)
        response = requests.get(request_url, headers=headers, timeout=5)
        response.raise_for_status()
        print("Response Status Code: " + str(response.status_code))
        json_response = response.json()
        print(json_response)
        print(json_response["perfs"])
        return(json_response)
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)
    return(None)

def create_swiss_tournament(swiss: Swiss):
    request_url = f"{http_post_new_swiss_tournament}{swiss.team_id}"
    body = {
        'name': swiss.title,
        'description': swiss.description,
        'clock.limit': swiss.clock,
        'clock.increment': swiss.increment,
        'nbRounds': swiss.rounds,
        'startsAt': swiss.starts_at,
        'roundInterval': swiss.interval
    }
    headers = json_header_post_with_authorization_bot
    try:
        print("Url: " + request_url)
        response = requests.post(request_url, headers=headers, data=body, timeout=5)
        response.raise_for_status()
        print("Response Status Code: " + str(response.status_code))
        json_response = response.json()
        print(json_response)
        if response.status_code == 200:
            return(json_response)
        else:
            return(None)
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)
    return(None)

def send_message_to_team(message):
    request_url = f"{http_post_team}"
    body = {
        'message': message
    }
    headers = json_header_post_with_authorization_bot
    try:
        print("Url: " + request_url)
        response = requests.post(request_url, headers=headers, data=body, timeout=5)
        response.raise_for_status()
        print("Response Status Code: " + str(response.status_code))
        if response.status_code == 200:
            return("OK")
        else:
            return(None)
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)
    return(None)


def create_arena_tournament(arena: Arena):
    request_url = f"{http_post_new_arena_tournament}"
    body = {
        'name': arena.title,
        'description': arena.description,
        'clockTime': arena.clock,
        'clockIncrement': arena.increment,
        'minutes': arena.duration,
        'startDate': arena.starts_at,
        'conditions.teamMember.teamId': arena.team_id
    }
    headers = json_header_post_with_authorization_bot
    try:
        print("Url: " + request_url)
        response = requests.post(request_url, headers=headers, data=body, timeout=5)
        response.raise_for_status()
        print("Response Status Code: " + str(response.status_code))
        json_response = response.json()
        print("Response jSon: " + str(json_response))
        arena_url = arena_tournament_link + json_response["id"]
        print("Arena URL created: " + arena_url)
        if response.status_code == 200:
            return(arena_url)
        else:
            return(None)
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)
    return(None)