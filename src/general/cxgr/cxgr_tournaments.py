from tokenize import String
from turtle import title
from api.lichess.lichess import create_swiss_tournament, create_arena_tournament
from api.lichess.lichess import send_message_to_team
from config.environment_keys import bot_team_id
from model.arena import Arena
from model.swiss import Swiss
from model.tournament import Tournament
from util.constants import swiss_tournament_link, arena_tournament_link
from datetime import datetime
import time

time_interval_sleep = 5

def create_tournament_arena(arena: Arena):
    arena.team_id = bot_team_id
    local_dt = datetime.now()
    duration_hours = str(round(arena.duration/60, 2)).replace('.0', '')
    if (arena.hour >= 0 and arena.hour <= 2):
        new_date = datetime(local_dt.year, local_dt.month, local_dt.day + 1, arena.hour, arena.minute, 0, 0) #Brazil's zone [Sao Paulo]
    else:
        new_date = datetime(local_dt.year, local_dt.month, local_dt.day, arena.hour, arena.minute, 0, 0) #Brazil's zone [Sao Paulo]
    time_converted = new_date.strftime('%s')
    arena.starts_at = int(float(time_converted)*1000)
    response = create_arena_tournament(arena)
    if response != None:
        tournament_id = response["id"]
        return(f"[Arena] {arena.title} ({arena.clock}+{arena.increment}) - {duration_hours}h - {format(arena.hour, '02d')}:{format(arena.minute, '02d')}:\n{arena_tournament_link}{tournament_id}")
    return(f"Não foi possível criar o torneio {arena.title}. Desculpe =/")

def create_arena_tournament_with_params(tournament_params):
    params = tournament_params.split(',')
    size_list_params = len(params)
    print(params)
    if size_list_params == 7:
        arena = Arena()
        arena.title = params[0].strip()
        print(f"title: {arena.title}")
        arena.description = params[1].strip()
        print(f"description: {arena.description}")
        arena.clock = int(params[2].strip())
        print(f"clock: {arena.clock}")
        arena.increment = int(params[3].strip())
        print(f"increment: {arena.increment}")
        arena.duration = int(params[4].strip())
        print(f"duration: {arena.duration}")
        arena.hour = int(params[5].strip())
        print(f"hour: {arena.hour}")
        arena.minute = int(params[6].strip())
        print(f"minute: {arena.minute}")
        return(create_tournament_arena(arena))
    return("Algo não está certo.\nCertifique-se de que está mandando o comando exatamente assim:\n\n.swiss _Nome do Torneio_, _Descrição do Torneio (pode ser o link de uma imagem .jpg)_, _Tempo do Relógio (em segundos)_, _Tempo de incremento por lance (em segundos)_, _Duração do Torneio (em minutos)_, _Hora de início do Torneio (em minutos)_, _Minutos de início do Torneio (em minutos)_")

def create_tournament_swiss(swiss: Swiss):
    clock_time = swiss.clock
    swiss.clock = clock_time * 60
    swiss.team_id = bot_team_id
    local_dt = datetime.now()
    if (swiss.hour >= 0 and swiss.hour <= 2):
        new_date = datetime(local_dt.year, local_dt.month, local_dt.day + 1, swiss.hour,swiss. minute, 0, 0) #Brazil's zone [Sao Paulo]
    else:
        new_date = datetime(local_dt.year, local_dt.month, local_dt.day, swiss.hour, swiss.minute, 0, 0) #Brazil's zone [Sao Paulo]
    time_converted = new_date.strftime('%s')
    swiss.starts_at = int(float(time_converted)*1000)
    response = create_swiss_tournament(swiss)
    if response != None:
        if (response["status"] == "created"):
            tournament_id = response["id"]
            return(f"[Suiço] {swiss.title} ({clock_time}+{swiss.increment}) - {swiss.rounds} RD - {format(swiss.hour, '02d')}:{format(swiss.minute, '02d')}:\n{swiss_tournament_link}{tournament_id}")
    return(f"Não foi possível criar o torneio {swiss.title}. Desculpe =/")

def create_swis_tournament_with_params(tournament_params):
    params = tournament_params.split(',')
    size_list_params = len(params)
    print(params)
    if size_list_params == 8:
        swiss = Swiss()
        swiss.title = params[0].strip()
        print(f"title: {swiss.title}")
        swiss.description = params[1].strip()
        print(f"description: {swiss.description}")
        swiss.clock = int(params[2].strip())
        print(f"clock: {swiss.clock}")
        swiss.increment = int(params[3].strip())
        print(f"increment: {swiss.increment}")
        swiss.rounds = int(params[4].strip())
        print(f"rounds: {swiss.rounds}")
        swiss.interval = int(params[5].strip())
        print(f"interval: {swiss.interval}")
        swiss.hour = int(params[6].strip())
        print(f"hour: {swiss.hour}")
        swiss.minute = int(params[7].strip())
        print(f"minute: {swiss.minute}")
        return(create_tournament_swiss(swiss))
    return("Algo não está certo.\nCertifique-se de que está mandando o comando exatamente assim:\n\n.swiss _Nome do Torneio_, _Descrição do Torneio (pode ser o link de uma imagem .jpg)_, _Tempo do Relógio (em segundos)_, _Tempo de incremento por lance (em segundos)_, _Número de rodadas_, _Tempo de intervalo entre rodadas (em segundos)_, _Hora de início do Torneio (em minutos)_, _Minutos de início do Torneio (em minutos)_")
        

def create_tournament_list_p1():
    tournaments_info = ""
    cafe_da_manha = Swiss(
        title= 'Café da Manhã', 
        description = '', 
        clock = 3, 
        increment = 2, 
        rounds = 7, 
        interval = 5, 
        hour = 11, 
        minute = 0
    )
    tournaments_info += f"{create_tournament_swiss(cafe_da_manha)}\n\n"
    time.sleep(time_interval_sleep)
    forty_degrees = Swiss(
        title= '40 Graus', 
        description = 'https://i.imgur.com/Uyw2HUT.jpg', 
        clock = 7, 
        increment = 2, 
        rounds = 7, 
        interval = 5, 
        hour = 13, 
        minute = 15
    )
    tournaments_info += f"{create_tournament_swiss(forty_degrees)}\n\n"
    time.sleep(time_interval_sleep)
    flash = Swiss(
        title= 'Flash', 
        description = 'https://i.imgur.com/8FnNzis.jpg', 
        clock = 5, 
        increment = 3, 
        rounds = 5, 
        interval = 5, 
        hour = 15, 
        minute = 0
    )
    tournaments_info += f"{create_tournament_swiss(flash)}\n\n"
    time.sleep(time_interval_sleep)
    por_do_sol = Swiss(
        title= 'Por do Sol', 
        description = 'https://i.imgur.com/IJ0OO6N.jpg', 
        clock = 7, 
        increment = 2, 
        rounds = 7, 
        interval = 5, 
        hour = 18, 
        minute = 5
    )
    tournaments_info += f"{create_tournament_swiss(por_do_sol)}\n\n"
    time.sleep(time_interval_sleep)
    aladdyn = Swiss(
        title= 'Aladdyn', 
        description = '', 
        clock = 3, 
        increment = 2, 
        rounds = 7, 
        interval = 5, 
        hour = 21, 
        minute = 0
    )
    tournaments_info += f"{create_tournament_swiss(aladdyn)}\n\n"
    time.sleep(time_interval_sleep)
    lua_cheia = Swiss(
        title= 'Lua Cheia', 
        description = '', 
        clock = 7, 
        increment = 2, 
        rounds = 7, 
        interval = 5, 
        hour = 22, 
        minute = 0
    )
    tournaments_info += f"{create_tournament_swiss(lua_cheia)}\n\n"
    time.sleep(time_interval_sleep)
    carlsen_lobisomen = Swiss(
        title= 'Carlsen Lobisomen', 
        description = '', 
        clock = 3, 
        increment = 2, 
        rounds = 7, 
        interval = 5, 
        hour = 0, 
        minute = 0
    )
    tournaments_info += f"{create_tournament_swiss(carlsen_lobisomen)}\n\n"
    return(tournaments_info)

def create_tournament_list_p2():
    tournaments_info = ""
    cafe_da_manha = Swiss(
        title= 'Café da Manhã', 
        description = '', 
        clock = 3, 
        increment = 2, 
        rounds = 7, 
        interval = 5, 
        hour = 10, 
        minute = 0
    )
    tournaments_info += f"{create_tournament_swiss(cafe_da_manha)}\n\n"
    time.sleep(time_interval_sleep)
    continental = Swiss(
        title= 'Continental', 
        description = '', 
        clock = 3, 
        increment = 2, 
        rounds = 9, 
        interval = 5, 
        hour = 13, 
        minute = 0
    )
    tournaments_info += f"{create_tournament_swiss(continental)}\n\n"
    time.sleep(time_interval_sleep)
    iron_man = Swiss(
        title= 'Iron Man', 
        description = '', 
        clock = 10, 
        increment = 0, 
        rounds = 5, 
        interval = 60, 
        hour = 15, 
        minute = 0
    )
    tournaments_info += f"{create_tournament_swiss(iron_man)}\n\n"
    time.sleep(time_interval_sleep)
    por_do_sol = Swiss(
        title= 'Pôr do Sol', 
        description = '', 
        clock = 7, 
        increment = 2, 
        rounds = 7, 
        interval = 5, 
        hour = 18, 
        minute = 0
    )
    tournaments_info += f"{create_tournament_swiss(por_do_sol)}\n\n"
    time.sleep(time_interval_sleep)
    aladdyn = Swiss(
        title= 'Aladdyn', 
        description = '', 
        clock = 3, 
        increment = 2, 
        rounds = 7, 
        interval = 5, 
        hour = 21,
        minute = 0
    )
    tournaments_info += f"{create_tournament_swiss(aladdyn)}\n\n"
    time.sleep(time_interval_sleep)
    lua_cheia = Swiss(
        title= 'Lua Cheia', 
        description = '', 
        clock = 7, 
        increment = 2, 
        rounds = 7, 
        interval = 5, 
        hour = 22, 
        minute = 5
    )
    tournaments_info += f"{create_tournament_swiss(lua_cheia)}\n\n"
    time.sleep(time_interval_sleep)
    carlsen_lobisomen = Swiss(
        title= 'Carlsen Lobisomen', 
        description = '', 
        clock = 3, 
        increment = 2, 
        rounds = 7, 
        interval = 5, 
        hour = 0, 
        minute = 5
    )
    tournaments_info += f"{create_tournament_swiss(carlsen_lobisomen)}\n\n"
    return(tournaments_info)
    

def create_tournament_list_p3():
    tournaments_info = ""
    cafe = Swiss(
        title= 'Café', 
        description = 'https://i.imgur.com/pqEs4vY.jpg', 
        clock = 3, 
        increment = 2, 
        rounds = 7, 
        interval = 5, 
        hour = 10, 
        minute = 15
    )
    tournaments_info += f"{create_tournament_swiss(cafe)}\n\n"
    time.sleep(time_interval_sleep)
    almoco = Swiss(
        title= 'Almoço', 
        description = 'https://i.imgur.com/h5VYBrO.jpg',
        clock = 7, 
        increment = 2, 
        rounds = 5, 
        interval = 5, 
        hour = 13, 
        minute = 0
    )
    tournaments_info += f"{create_tournament_swiss(almoco)}\n\n"
    time.sleep(time_interval_sleep)
    sessao_da_tarde = Swiss(
        title= 'Sessão da Tarde', 
        description = 'https://i.imgur.com/sTtNzHs.jpg', 
        clock = 5, 
        increment = 3, 
        rounds = 7, 
        interval = 5, 
        hour = 15, 
        minute = 30
    )
    tournaments_info += f"{create_tournament_swiss(sessao_da_tarde)}\n\n"
    time.sleep(time_interval_sleep)
    cidade_alerta = Swiss(
        title= 'Cidade Alerta',
        description = 'https://i.imgur.com/XZlJzrK.jpg', 
        clock = 7, 
        increment = 2, 
        rounds = 5, 
        interval = 5, 
        hour = 18, 
        minute = 15
    )
    tournaments_info += f"{create_tournament_swiss(cidade_alerta)}\n\n"
    time.sleep(time_interval_sleep)
    torre_na_setima = Swiss(
        title= 'Torre na Sétima', 
        description = 'https://i.imgur.com/xHdBRN1.jpg', 
        clock = 5, 
        increment = 3, 
        rounds = 7, 
        interval = 5, 
        hour = 21, 
        minute = 0
    )
    tournaments_info += f"{create_tournament_swiss(torre_na_setima)}\n\n"
    time.sleep(time_interval_sleep)
    lua_cheia = Swiss(
        title= 'Lua Cheia', 
        description = 'https://i.imgur.com/BasYzhK.jpg', 
        clock = 7, 
        increment = 2, 
        rounds = 5, 
        interval = 5, 
        hour = 22, 
        minute = 15
    )
    tournaments_info += f"{create_tournament_swiss(lua_cheia)}\n\n"
    time.sleep(time_interval_sleep)
    carlsen_lobisomen = Swiss(
        title= 'Carlsen Lobisomen', 
        description = 'https://i.imgur.com/b4TXEzM.png', 
        clock = 3, 
        increment = 2, 
        rounds = 7, 
        interval = 5, 
        hour = 0, 
        minute = 15
    )
    tournaments_info += f"{create_tournament_swiss(carlsen_lobisomen)}\n\n"
    return(tournaments_info)

def create_tournament_list_p4():
    tournaments_info = ""
    despertador = Arena(
        title = 'Despertador', 
        description = 'https://i.imgur.com/dwov4dA.jpg', 
        clock = 5, 
        increment = 3, 
        duration = 60,
        hour = 8, 
        minute = 30
    )
    tournaments_info += f"{create_tournament_arena(despertador)}\n\n"
    time.sleep(time_interval_sleep)
    cafe_da_manha = Swiss(
        title = 'Café da Manhã', 
        description = 'https://i.imgur.com/pqEs4vY.jpg', 
        clock = 3, 
        increment = 2, 
        rounds = 7, 
        interval = 5, 
        hour = 10, 
        minute = 15
    )
    tournaments_info += f"{create_tournament_swiss(cafe_da_manha)}\n\n"
    time.sleep(time_interval_sleep)
    almoco = Swiss(
        title= 'Parmegiana', 
        description = 'https://i.imgur.com/amHPhqi.jpg',
        clock = 10, 
        increment = 0, 
        rounds = 5, 
        interval = 5, 
        hour = 13, 
        minute = 10
    )
    tournaments_info += f"{create_tournament_swiss(almoco)}\n\n"
    time.sleep(time_interval_sleep)
    forty_degrees = Swiss(
        title= '40 Graus', 
        description = 'https://i.imgur.com/Uyw2HUT.jpg', 
        clock = 7, 
        increment = 2, 
        rounds = 7, 
        interval = 5, 
        hour = 15, 
        minute = 30
    )
    tournaments_info += f"{create_tournament_swiss(forty_degrees)}\n\n"
    time.sleep(time_interval_sleep)
    caldeirao = Arena(
        title= 'Caldeirão',
        description = 'https://i.imgur.com/sCfQU7V.jpg', 
        clock = 5, 
        increment = 3, 
        duration = 90,
        hour = 18, 
        minute = 00
    )
    tournaments_info += f"{create_tournament_arena(caldeirao)}\n\n"
    time.sleep(time_interval_sleep)
    torre_na_setima = Swiss(
        title= 'Bobby Fischer', 
        description = 'https://i.imgur.com/H6TSF3Z.jpg', 
        clock = 15, 
        increment = 10, 
        rounds = 3, 
        interval = 20, 
        hour = 20, 
        minute = 15
    )
    tournaments_info += f"{create_tournament_swiss(torre_na_setima)}\n\n"
    time.sleep(time_interval_sleep)
    lua_cheia = Swiss(
        title= 'Lua Cheia', 
        description = 'https://i.imgur.com/FL35J8p.jpg', 
        clock = 7, 
        increment = 2, 
        rounds = 5, 
        interval = 5, 
        hour = 23, 
        minute = 30
    )
    tournaments_info += f"{create_tournament_swiss(lua_cheia)}\n\n"
    return(tournaments_info)

def create_tournament_list(type: Tournament.Type, extra_message = None):
    local_dt = datetime.now()
    formatted_date = f"{local_dt.day}/{local_dt.month}/{local_dt.year}"
    message_to_send = f"Bom dia, CXGR ♟️\nOs torneios de hoje ({formatted_date}) são:\n\n"
    match type:
        case Tournament.Type.P1:
            message_to_send += create_tournament_list_p1()
        case Tournament.Type.P2:
            message_to_send += create_tournament_list_p2()
        case Tournament.Type.P3:
            message_to_send += create_tournament_list_p3()
        case Tournament.Type.P4:
            message_to_send += create_tournament_list_p4()
    if (extra_message != None):
        message_to_send += f"{extra_message.strip()}\n\n"
    message_to_send += "Obrigado e até a próxima!   o/ \n\n♟️🏁🏁🏁🐎🐎🐎🏁🏁🏁♟️"
    time.sleep(time_interval_sleep)
    response = send_message_to_team(message_to_send)
    if response != None:
        if (response["ok"] == True):
            return(message_to_send)
    return(f"Ocorreu um erro ao enviar mensagem para os membros da Equipe no Lichess. Contudo, os torneios foram criados.\n\n{message_to_send}")