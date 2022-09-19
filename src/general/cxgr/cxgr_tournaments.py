from api.lichess.lichess import create_swiss_tournament
from api.lichess.lichess import send_message_to_team
from config.environment_keys import bot_team_id
from util.constants import swiss_tournament_link
from datetime import datetime
import pytz

def create_tournament_cafe():
    title = "Torneio de teste - 16h"
    clock_limit = 180
    increment = 2
    rounds = 7
    interval_rounds = 5
    team_id = bot_team_id
    local_dt = datetime.now()
    new_date = datetime(local_dt.year, local_dt.month, local_dt.day, 10, 15, 0, 0) #Brazil's zone [Sao Paulo]
    time_converted = new_date.strftime('%s')
    starts_at = int(float(time_converted)*1000)
    response = create_swiss_tournament(title, clock_limit, increment, rounds, starts_at, interval_rounds, team_id)
    if response != None:
        if (response["status"] == "created"):
            tournament_id = response["id"]
            return(f"O torneio foi criado com Sucesso!\n\nO link para acessá-lo é: {swiss_tournament_link}{tournament_id}")
        else:
            return("Não consegui criar o Torneio. Favor tentar novamente mais tarde =/")


def create_tournament_cafe_da_manha():
    title = "Café da Manhã"
    clock_limit = 180
    increment = 2
    rounds = 7
    interval_rounds = 5
    team_id = bot_team_id
    local_dt = datetime.now()
    new_date = datetime(local_dt.year, local_dt.month, local_dt.day, 11, 0, 0, 0) #Brazil's zone [Sao Paulo]
    time_converted = new_date.strftime('%s')
    starts_at = int(float(time_converted)*1000)
    response = create_swiss_tournament(title, clock_limit, increment, rounds, starts_at, interval_rounds, team_id)
    if response != None:
        if (response["status"] == "created"):
            tournament_id = response["id"]
            return(f"*{title} 3+2 {rounds} RD 11:00*:\n{swiss_tournament_link}{tournament_id}")
        else:
            return(f"Não foi possível criar o torneio {title} hoje. Desculpe =/")

def create_tournament_continental():
    title = "Continental"
    clock_limit = 180
    increment = 2
    rounds = 9
    interval_rounds = 5
    team_id = bot_team_id
    local_dt = datetime.now()
    new_date = datetime(local_dt.year, local_dt.month, local_dt.day, 13, 0, 0, 0) #Brazil's zone [Sao Paulo]
    time_converted = new_date.strftime('%s')
    starts_at = int(float(time_converted)*1000)
    response = create_swiss_tournament(title, clock_limit, increment, rounds, starts_at, interval_rounds, team_id)
    if response != None:
        if (response["status"] == "created"):
            tournament_id = response["id"]
            return(f"*{title} 3+2 {rounds} RD 13:00*:\n{swiss_tournament_link}{tournament_id}")
        else:
            return(f"Não foi possível criar o torneio {title} hoje. Desculpe =/")

def create_tournament_iron_man():
    title = "Iron Man"
    clock_limit = 600
    increment = 0
    rounds = 5
    interval_rounds = 60
    team_id = bot_team_id
    local_dt = datetime.now()
    new_date = datetime(local_dt.year, local_dt.month, local_dt.day, 15, 0, 0, 0) #Brazil's zone [Sao Paulo]
    time_converted = new_date.strftime('%s')
    starts_at = int(float(time_converted)*1000)
    response = create_swiss_tournament(title, clock_limit, increment, rounds, starts_at, interval_rounds, team_id)
    if response != None:
        if (response["status"] == "created"):
            tournament_id = response["id"]
            return(f"*{title} 10+0 {rounds} RD 13:00*:\n{swiss_tournament_link}{tournament_id}")
        else:
            return(f"Não foi possível criar o torneio {title} hoje. Desculpe =/")

def create_tournament_por_do_sol():
    title = "Por do Sol"
    clock_limit = 420
    increment = 2
    rounds = 7
    interval_rounds = 5
    team_id = bot_team_id
    local_dt = datetime.now()
    new_date = datetime(local_dt.year, local_dt.month, local_dt.day, 18, 0, 0, 0) #Brazil's zone [Sao Paulo]
    time_converted = new_date.strftime('%s')
    starts_at = int(float(time_converted)*1000)
    response = create_swiss_tournament(title, clock_limit, increment, rounds, starts_at, interval_rounds, team_id)
    if response != None:
        if (response["status"] == "created"):
            tournament_id = response["id"]
            return(f"*{title} 7+2 {rounds} RD 18:00*:\n{swiss_tournament_link}{tournament_id}")
        else:
            return(f"Não foi possível criar o torneio {title} hoje. Desculpe =/")

def create_tournament_aladdyn():
    title = "Aladdyn"
    clock_limit = 180
    increment = 2
    rounds = 7
    interval_rounds = 5
    team_id = bot_team_id
    local_dt = datetime.now()
    new_date = datetime(local_dt.year, local_dt.month, local_dt.day, 21, 0, 0, 0) #Brazil's zone [Sao Paulo]
    time_converted = new_date.strftime('%s')
    starts_at = int(float(time_converted)*1000)
    response = create_swiss_tournament(title, clock_limit, increment, rounds, starts_at, interval_rounds, team_id)
    if response != None:
        if (response["status"] == "created"):
            tournament_id = response["id"]
            return(f"*{title} 3+2 {rounds} RD 21:00*:\n{swiss_tournament_link}{tournament_id}")
        else:
            return(f"Não foi possível criar o torneio {title} hoje. Desculpe =/")

def create_tournament_lua_cheia():
    title = "Lua Cheia"
    clock_limit = 480
    increment = 2
    rounds = 7
    interval_rounds = 5
    team_id = bot_team_id
    local_dt = datetime.now()
    new_date = datetime(local_dt.year, local_dt.month, local_dt.day, 21, 5, 0, 0) #Brazil's zone [Sao Paulo]
    time_converted = new_date.strftime('%s')
    starts_at = int(float(time_converted)*1000)
    response = create_swiss_tournament(title, clock_limit, increment, rounds, starts_at, interval_rounds, team_id)
    if response != None:
        if (response["status"] == "created"):
            tournament_id = response["id"]
            return(f"*{title} 7+2 {rounds} RD 22:05*:\n{swiss_tournament_link}{tournament_id}")
        else:
            return(f"Não foi possível criar o torneio {title} hoje. Desculpe =/")

def create_tournament_carlsen_lobisomen():
    title = "Carlsen Lobisomen"
    clock_limit = 180
    increment = 2
    rounds = 7
    interval_rounds = 5
    team_id = bot_team_id
    local_dt = datetime.now()
    new_date = datetime(local_dt.year, local_dt.month, local_dt.day + 1, 00, 5, 0, 0) #Brazil's zone [Sao Paulo]
    time_converted = new_date.strftime('%s')
    starts_at = int(float(time_converted)*1000)
    response = create_swiss_tournament(title, clock_limit, increment, rounds, starts_at, interval_rounds, team_id)
    if response != None:
        if (response["status"] == "created"):
            tournament_id = response["id"]
            return(f"*{title} 3+2 {rounds} RD 00:05*:\n{swiss_tournament_link}{tournament_id}")
        else:
            return(f"Não foi possível criar o torneio {title} hoje. Desculpe =/")

def create_tournament_list_p1():
    message_to_send = "Bom dia, CXGR. Os torneios de hoje são:\n\n"
    message_to_send += f"{create_tournament_cafe_da_manha()}\n\n"
    message_to_send += f"{create_tournament_continental()}\n\n"
    message_to_send += f"{create_tournament_iron_man()}\n\n"
    message_to_send += f"{create_tournament_por_do_sol()}\n\n"
    message_to_send += f"{create_tournament_aladdyn()}\n\n"
    message_to_send += f"{create_tournament_lua_cheia()}\n\n"
    message_to_send += f"{create_tournament_carlsen_lobisomen()}\n\n"
    message_to_send += "Obrigado e até a próxima!   o/"
    response = send_message_to_team(message_to_send)
    if response != None:
        if (response["status"] == "created"):
            return(message_to_send)
        else:
            return(f"Ocorreu um erro.\n\n{response}")
    