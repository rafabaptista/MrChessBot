from api.lichess.lichess import create_swiss_tournament
from api.lichess.lichess import send_message_to_team
from config.environment_keys import bot_team_id
from util.constants import swiss_tournament_link
from datetime import datetime
import pytz

def create_tournament_swiss(title, description, clock, increment, rounds, interval, hour, minute):
    title = title
    description = description
    clock_limit = clock * 60
    increment = increment
    rounds = rounds
    interval_rounds = interval
    team_id = bot_team_id
    local_dt = datetime.now()
    if (hour == 0):
        new_date = datetime(local_dt.year, local_dt.month, local_dt.day + 1, hour, minute, 0, 0) #Brazil's zone [Sao Paulo]
    else:
        new_date = datetime(local_dt.year, local_dt.month, local_dt.day, hour, minute, 0, 0) #Brazil's zone [Sao Paulo]
    time_converted = new_date.strftime('%s')
    starts_at = int(float(time_converted)*1000)
    response = create_swiss_tournament(title, description, clock_limit, increment, rounds, starts_at, interval_rounds, team_id)
    if response != None:
        if (response["status"] == "created"):
            tournament_id = response["id"]
            return(f"* ♟️ {title} ({clock}+{increment}) - {rounds} RD - {format(hour, '02d')}:{format(minute, '02d')} ♟️ *:\n{swiss_tournament_link}{tournament_id}")
        else:
            return(f"Não foi possível criar o torneio {title}. Desculpe =/")
    else:
        return(f"Não foi possível criar o torneio {title}. Desculpe =/")

def create_swis_tournament_with_params(tournament_params):
    params = tournament_params.split(',')
    size_list_params = len(params)
    if size_list_params == 8:
        title= params[0]
        description = params[1]
        clock = params[2]
        increment = params[3]
        rounds = params[4]
        interval = params[5]
        hour = params[6]
        minute = params[7]
        return(create_tournament_swiss(title, description, clock, increment, rounds, interval, hour, minute))
    else:
        return("Algo não está certo.\nCertifique-se de que está mandando o comando exatamente assim:\n\n.swiss _Nome do Torneio_, _Tempo do Relógio (em segundos)_, _Tempo de incremento por lance (em segundos)_, _Número de rodadas_, _Horário de início do Torneio (timestamp com milisegundos)_, _Tempo de intervalo entre rodadas (em segundos)_, _Código da Equipe (está no final da URL da página da Equipe no Lichess)_\n\nPara gerar o Timestamp do horário do torneio, pode entrar nesse site: https://www.epochconverter.com/")
        

def create_tournament_list_p1():
    local_dt = datetime.now()
    formatted_date = f"{local_dt.day}/{local_dt.month}/{local_dt.year}"
    message_to_send = f"Bom dia, CXGR. Os torneios de hoje ({formatted_date}) são:\n\n"
    message_to_send += f"{create_tournament_swiss(title= 'Café da Manhã', description = '', clock = 3, increment = 2, rounds = 7, interval = 5, hour = 10, minute = 0)}\n\n"
    message_to_send += f"{create_tournament_swiss(title= 'Continental', description = '', clock = 3, increment = 2, rounds = 9, interval = 5, hour = 13, minute = 0)}\n\n"
    message_to_send += f"{create_tournament_swiss(title= 'Iron Man', description = '', clock = 10, increment = 0, rounds = 5, interval = 60, hour = 15, minute = 0)}\n\n"
    message_to_send += f"{create_tournament_swiss(title= 'Pôr do Sol', description = '', clock = 7, increment = 2, rounds = 7, interval = 5, hour = 18, minute = 0)}\n\n"
    message_to_send += f"{create_tournament_swiss(title= 'Aladdyn', description = '', clock = 3, increment = 2, rounds = 7, interval = 5, hour = 21, minute = 0)}\n\n"
    message_to_send += f"{create_tournament_swiss(title= 'Lua Cheia', description = '', clock = 7, increment = 2, rounds = 7, interval = 5, hour = 22, minute = 5)}\n\n"
    message_to_send += f"{create_tournament_swiss(title= 'Carlsen Lobisomen', description = '', clock = 3, increment = 2, rounds = 7, interval = 5, hour = 0, minute = 5)}\n\n"
    message_to_send += "Obrigado e até a próxima!   o/ \n\n🏁🏁🏁🐎🐎🐎🏁🏁🏁"
    response = send_message_to_team(message_to_send)
    if response != None:
        if (response["ok"] == True):
            return(message_to_send)
        else:
            return(f"Ocorreu um erro.\n\n{response}")
    else:
        return(f"Ocorreu um erro. Desculpe.")

def create_tournament_list_p2():
    local_dt = datetime.now()
    formatted_date = f"{local_dt.day}/{local_dt.month}/{local_dt.year}"
    message_to_send = f"Bom dia, CXGR. Os torneios de hoje ({formatted_date}) são:\n\n"
    message_to_send += f"{create_tournament_swiss(title= 'Café da Manhã', clock = 3, increment = 2, rounds = 7, interval = 5, hour = 11, minute = 0)}\n\n"
    message_to_send += f"{create_tournament_swiss(title= '40 Graus', description = 'https://i.imgur.com/Uyw2HUT.jpg', clock = 7, increment = 2, rounds = 7, interval = 5, hour = 13, minute = 15)}\n\n"
    message_to_send += f"{create_tournament_swiss(title= 'Flash', description = 'https://i.imgur.com/8FnNzis.jpg', clock = 5, increment = 3, rounds = 5, interval = 5, hour = 15, minute = 0)}\n\n"
    message_to_send += f"{create_tournament_swiss(title= 'Por do Sol', description = 'https://i.imgur.com/IJ0OO6N.jpg', clock = 7, increment = 2, rounds = 7, interval = 5, hour = 18, minute = 5)}\n\n"
    message_to_send += f"{create_tournament_swiss(title= 'Por do Sol', description = 'https://i.imgur.com/IJ0OO6N.jpg', clock = 7, increment = 2, rounds = 7, interval = 5, hour = 18, minute = 5)}\n\n"
    message_to_send += f"{create_tournament_swiss(title= 'Aladdyn', description = '', clock = 3, increment = 2, rounds = 7, interval = 5, hour = 21, minute = 0)}\n\n"
    message_to_send += f"{create_tournament_swiss(title= 'Lua Cheia', description = '', clock = 7, increment = 2, rounds = 7, interval = 5, hour = 22, minute = 0)}\n\n"
    message_to_send += f"{create_tournament_swiss(title= 'Carlsen Lobisomen', description = '', clock = 3, increment = 2, rounds = 7, interval = 5, hour = 0, minute = 0)}\n\n"
    message_to_send += "Obrigado e até a próxima!   o/ \n\n🏁🏁🏁🐎🐎🐎🏁🏁🏁"
    response = send_message_to_team(message_to_send)
    if response != None:
        if (response["ok"] == True):
            return(message_to_send)
        else:
            return(f"Ocorreu um erro.\n\n{response}")
    else:
        return(f"Ocorreu um erro. Desculpe.")
    