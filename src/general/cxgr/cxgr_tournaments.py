from network.api.lichess.lichess import create_swiss_tournament, create_arena_tournament
from network.api.lichess.lichess import send_message_to_team
from config.environment_keys import bot_team_id
from model.tournament import fix_hour
from model.arena import Arena, map_arena_tournament
from model.swiss import Swiss, map_swiss_tournament
from model.tournament import Tournament
from util.constants import swiss_tournament_link, arena_tournament_link
from datetime import datetime
from network.db.dal import *
import time
import discord

time_interval_sleep = 1

def create_tournament_arena(arena: Arena):
    arena.team_id = bot_team_id
    local_dt = datetime.now()
    duration_hours = str(round(arena.duration/60, 2)).replace('.0', '')
    tournament_hour = fix_hour(arena.hour)
    if (tournament_hour >= 0 and tournament_hour <= 2):
        new_date = datetime(local_dt.year, local_dt.month, local_dt.day + 1, tournament_hour, arena.minute, 0, 0) #Brazil's zone [Sao Paulo]
    else:
        new_date = datetime(local_dt.year, local_dt.month, local_dt.day, tournament_hour, arena.minute, 0, 0) #Brazil's zone [Sao Paulo]
    time_converted = new_date.strftime('%s')
    arena.starts_at = int(float(time_converted)*1000)
    response = create_arena_tournament(arena)
    if response != None:
        tournament_id = response["id"]
        return(f"[Arena] {arena.title} ({arena.clock}+{arena.increment}) - {duration_hours}h - {format(tournament_hour, '02d')}:{format(arena.minute, '02d')}:\n{arena_tournament_link}{tournament_id}")
    return(f"Não foi possível criar o torneio ***{arena.title}***. Desculpe =/")

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
    return("Algo não está certo.\nCertifique-se de que está mandando o comando exatamente assim:\n\n.arena _Nome do Torneio_, _Descrição do Torneio (pode ser o link de uma imagem .jpg)_, _Tempo do Relógio (em segundos)_, _Tempo de incremento por lance (em segundos)_, _Duração do Torneio (em minutos)_, _Hora de início do Torneio (em minutos)_, _Minutos de início do Torneio (em minutos)_")

def add_arena_tournament_to_list_with_params(tournament_params):
    params = tournament_params.split(',')
    size_list_params = len(params)
    print(params)
    if size_list_params == 8:
        arena = Arena()
        list_name = params[0].strip()
        arena.title = params[1].strip()
        print(f"title: {arena.title}")
        arena.description = params[2].strip()
        print(f"description: {arena.description}")
        arena.clock = int(params[3].strip())
        print(f"clock: {arena.clock}")
        arena.increment = int(params[4].strip())
        print(f"increment: {arena.increment}")
        arena.duration = int(params[5].strip())
        print(f"duration: {arena.duration}")
        arena.hour = int(params[6].strip())
        print(f"hour: {arena.hour}")
        arena.minute = int(params[7].strip())
        print(f"minute: {arena.minute}")
        addition = insert_new_arena_tournament(arena, list_name)
        if (addition):
            duration_hours = str(round(arena.duration/60, 2)).replace('.0', '')
            response_message = f"\nO torneio foi adicionado com sucesso à lista ***{list_name}*** de Torneios Diários.\n\n"
            response_message += f"• [Arena] {arena.title} ({arena.clock}+{arena.increment}) - {duration_hours}h - {format(arena.hour, '02d')}:{format(arena.minute, '02d')}"
            if (arena.description != ""):
                response_message += f" - {arena.description}"
            return discord.Embed(title=":white_check_mark:", description=response_message, color= discord.Color.green())
    response_error_message = f"\nNão foi possível adicionar o torneio ***[Arena] {arena.title}*** à lista ***{list_name}*** de Torneios Diários. Confira os parâmetros e tente novamente mais tarde."
    return discord.Embed(title=":exclamation:", description=response_error_message, color= discord.Color.red())

def create_tournament_swiss(swiss: Swiss):
    clock_time = swiss.clock
    swiss.clock = clock_time * 60
    swiss.team_id = bot_team_id
    local_dt = datetime.now()
    tournament_hour = fix_hour(swiss.hour)
    if (tournament_hour >= 0 and tournament_hour <= 2):
        new_date = datetime(local_dt.year, local_dt.month, local_dt.day + 1, tournament_hour,swiss. minute, 0, 0) #Brazil's zone [Sao Paulo]
    else:
        new_date = datetime(local_dt.year, local_dt.month, local_dt.day, tournament_hour, swiss.minute, 0, 0) #Brazil's zone [Sao Paulo]
    time_converted = new_date.strftime('%s')
    swiss.starts_at = int(float(time_converted)*1000)
    response = create_swiss_tournament(swiss)
    if response != None:
        if (response["status"] == "created"):
            tournament_id = response["id"]
            return(f"[Suiço] {swiss.title} ({clock_time}+{swiss.increment}) - {swiss.rounds} RD - {format(tournament_hour, '02d')}:{format(swiss.minute, '02d')}:\n{swiss_tournament_link}{tournament_id}")
    return(f"Não foi possível criar o torneio ***{swiss.title}***. Desculpe =/")

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

def add_swis_tournament_to_list_with_params(tournament_params):
    params = tournament_params.split(',')
    size_list_params = len(params)
    print(params)
    if size_list_params == 9:
        swiss = Swiss()
        list_name = params[0].strip()
        swiss.title = params[1].strip()
        print(f"title: {swiss.title}")
        swiss.description = params[2].strip()
        print(f"description: {swiss.description}")
        swiss.clock = int(params[3].strip())
        print(f"clock: {swiss.clock}")
        swiss.increment = int(params[4].strip())
        print(f"increment: {swiss.increment}")
        swiss.rounds = int(params[5].strip())
        print(f"rounds: {swiss.rounds}")
        swiss.interval = int(params[6].strip())
        print(f"interval: {swiss.interval}")
        swiss.hour = int(params[7].strip())
        print(f"hour: {swiss.hour}")
        swiss.minute = int(params[8].strip())
        print(f"minute: {swiss.minute}")
        addition = insert_new_swiss_tournament(swiss, list_name)
        if (addition):
            response_message = f"\nO torneio foi adicionado com sucesso à lista ***{list_name}*** de Torneios Diários.\n\n"
            response_message += f"• [Suiço] {swiss.title} ({swiss.clock}+{swiss.increment}) - {swiss.rounds} RD | {swiss.interval}s - {format(swiss.hour, '02d')}:{format(swiss.minute, '02d')}"
            if (swiss.description != ""):
                response_message += f" - {swiss.description}"
            return discord.Embed(title=":white_check_mark:", description=response_message, color= discord.Color.green())
    response_error_message = f"\nNão foi possível adicionar o torneio ***[Suiço] {swiss.title}*** à lista ***{list_name}*** de Torneios Diários. Confira os parâmetros e tente novamente mais tarde."
    return discord.Embed(title=":exclamation:", description=response_error_message, color= discord.Color.red())
        
def create_tournament_list_p1():
    tournaments_info = ""
    cafe_da_manha = Swiss(title= 'Café da Manhã', description= '', clock= 3, increment= 2, rounds= 7, interval= 5, hour= 11, minute= 0)
    tournaments_info += f"{create_tournament_swiss(cafe_da_manha)}\n\n"
    time.sleep(time_interval_sleep)
    forty_degrees = Swiss(title= '40 Graus', description= 'https://i.imgur.com/Uyw2HUT.jpg', clock= 7, increment= 2, rounds= 7, interval= 5, hour= 13, minute= 15)
    tournaments_info += f"{create_tournament_swiss(forty_degrees)}\n\n"
    time.sleep(time_interval_sleep)
    flash = Swiss(title= 'Flash', description= 'https://i.imgur.com/8FnNzis.jpg', clock= 5, increment= 3, rounds= 5, interval= 5, hour= 15, minute= 0)
    tournaments_info += f"{create_tournament_swiss(flash)}\n\n"
    time.sleep(time_interval_sleep)
    por_do_sol = Swiss(title= 'Por do Sol', description= 'https://i.imgur.com/IJ0OO6N.jpg', clock= 7, increment= 2, rounds= 7, interval= 5, hour= 18, minute= 5)
    tournaments_info += f"{create_tournament_swiss(por_do_sol)}\n\n"
    time.sleep(time_interval_sleep)
    aladdyn = Swiss(title= 'Aladdyn', description= '', clock = 3, increment= 2, rounds= 7, interval= 5, hour= 21, minute= 0)
    tournaments_info += f"{create_tournament_swiss(aladdyn)}\n\n"
    time.sleep(time_interval_sleep)
    lua_cheia = Swiss(title= 'Lua Cheia', description= '', clock= 7, increment= 2, rounds= 7, interval= 5, hour= 22, minute= 0)
    tournaments_info += f"{create_tournament_swiss(lua_cheia)}\n\n"
    time.sleep(time_interval_sleep)
    carlsen_lobisomen = Swiss(title= 'Carlsen Lobisomen', description= '', clock= 3, increment= 2, rounds= 7, interval= 5, hour= 0, minute= 0)
    tournaments_info += f"{create_tournament_swiss(carlsen_lobisomen)}\n\n"
    return(tournaments_info)

def create_tournament_list_p2():
    tournaments_info = ""
    cafe_da_manha = Swiss(title= 'Café da Manhã', description= '', clock= 3, increment= 2, rounds= 7, interval= 5, hour= 10, minute= 0)
    tournaments_info += f"{create_tournament_swiss(cafe_da_manha)}\n\n"
    time.sleep(time_interval_sleep)
    continental = Swiss(title= 'Continental', description= '', clock= 3, increment= 2, rounds= 9, interval= 5, hour= 13, minute= 0)
    tournaments_info += f"{create_tournament_swiss(continental)}\n\n"
    time.sleep(time_interval_sleep)
    iron_man = Swiss(title= 'Iron Man', description= '', clock= 10, increment= 0, rounds= 5, interval= 60, hour= 15, minute= 0)
    tournaments_info += f"{create_tournament_swiss(iron_man)}\n\n"
    time.sleep(time_interval_sleep)
    por_do_sol = Swiss(title= 'Pôr do Sol', description= '', clock= 7, increment= 2, rounds= 7, interval= 5, hour= 18, minute= 0)
    tournaments_info += f"{create_tournament_swiss(por_do_sol)}\n\n"
    time.sleep(time_interval_sleep)
    aladdyn = Swiss(title= 'Aladdyn', description= '', clock= 3, increment= 2, rounds= 7, interval= 5, hour= 21,minute= 0)
    tournaments_info += f"{create_tournament_swiss(aladdyn)}\n\n"
    time.sleep(time_interval_sleep)
    lua_cheia = Swiss(title= 'Lua Cheia', description= '', clock= 7, increment= 2, rounds= 7, interval= 5, hour= 22, minute= 5)
    tournaments_info += f"{create_tournament_swiss(lua_cheia)}\n\n"
    time.sleep(time_interval_sleep)
    carlsen_lobisomen = Swiss(title= 'Carlsen Lobisomen', description= '', clock= 3, increment= 2, rounds= 7, interval= 5, hour= 0, minute= 5)
    tournaments_info += f"{create_tournament_swiss(carlsen_lobisomen)}\n\n"
    return(tournaments_info)

def create_tournament_list_p3():
    tournaments_info = ""
    cafe = Swiss(title= 'Café', description= 'https://i.imgur.com/pqEs4vY.jpg', clock= 3, increment= 2, rounds= 7, interval= 5, hour= 10, minute= 15)
    tournaments_info += f"{create_tournament_swiss(cafe)}\n\n"
    time.sleep(time_interval_sleep)
    almoco = Swiss(title= 'Almoço', description= 'https://i.imgur.com/h5VYBrO.jpg',clock= 7, increment= 2, rounds= 5, interval= 5, hour= 13, minute= 0)
    tournaments_info += f"{create_tournament_swiss(almoco)}\n\n"
    time.sleep(time_interval_sleep)
    sessao_da_tarde = Swiss(title= 'Sessão da Tarde', description= 'https://i.imgur.com/sTtNzHs.jpg', clock= 5, increment= 3, rounds= 7, interval= 5, hour= 15, minute= 30)
    tournaments_info += f"{create_tournament_swiss(sessao_da_tarde)}\n\n"
    time.sleep(time_interval_sleep)
    cidade_alerta = Swiss(title= 'Cidade Alerta', description= 'https://i.imgur.com/XZlJzrK.jpg', clock= 7, increment= 2, rounds= 5, interval= 5, hour= 18, minute= 15)
    tournaments_info += f"{create_tournament_swiss(cidade_alerta)}\n\n"
    time.sleep(time_interval_sleep)
    torre_na_setima = Swiss(title= 'Torre na Sétima', description= 'https://i.imgur.com/xHdBRN1.jpg', clock= 5, increment= 3, rounds= 7, interval= 5, hour= 21, minute= 0)
    tournaments_info += f"{create_tournament_swiss(torre_na_setima)}\n\n"
    time.sleep(time_interval_sleep)
    lua_cheia = Swiss(title= 'Lua Cheia', description= 'https://i.imgur.com/BasYzhK.jpg', clock= 7, increment= 2, rounds= 5, interval= 5, hour= 22, minute= 15)
    tournaments_info += f"{create_tournament_swiss(lua_cheia)}\n\n"
    time.sleep(time_interval_sleep)
    carlsen_lobisomen = Swiss(title= 'Carlsen Lobisomen', description= 'https://i.imgur.com/b4TXEzM.jpg', clock= 3, increment= 2, rounds= 7, interval= 5, hour= 0, minute= 15)
    tournaments_info += f"{create_tournament_swiss(carlsen_lobisomen)}\n\n"
    return(tournaments_info)

def create_tournament_list_p4():
    tournaments_info = ""
    despertador = Arena(title= 'Despertador', description= 'https://i.imgur.com/G7Jsm2A.jpg', clock= 5, increment= 3, duration= 60,hour= 8, minute= 30)
    tournaments_info += f"{create_tournament_arena(despertador)}\n\n"
    time.sleep(time_interval_sleep)
    cafe_da_manha = Swiss(title= 'Café da Manhã', description= 'https://i.imgur.com/pqEs4vY.jpg', clock= 3, increment= 2, rounds= 7, interval= 5, hour= 10, minute= 15)
    tournaments_info += f"{create_tournament_swiss(cafe_da_manha)}\n\n"
    time.sleep(time_interval_sleep)
    almoco = Swiss(title= 'Parmegiana', description= 'https://i.imgur.com/amHPhqi.jpg',clock= 10, increment= 0, rounds= 5, interval= 5, hour= 13, minute= 10)
    tournaments_info += f"{create_tournament_swiss(almoco)}\n\n"
    time.sleep(time_interval_sleep)
    forty_degrees = Swiss(title= '40 Graus', description= 'https://i.imgur.com/Uyw2HUT.jpg', clock= 7, increment= 2, rounds= 7, interval= 5, hour= 15, minute= 30)
    tournaments_info += f"{create_tournament_swiss(forty_degrees)}\n\n"
    time.sleep(time_interval_sleep)
    caldeirao = Arena(title= 'Caldeirão',description= 'https://i.imgur.com/sCfQU7V.jpg', clock= 5, increment= 3, duration= 90,hour= 18, minute= 0)
    tournaments_info += f"{create_tournament_arena(caldeirao)}\n\n"
    time.sleep(time_interval_sleep)
    torre_na_setima = Swiss(title= 'Bobby Fischer', description= 'https://i.imgur.com/H6TSF3Z.jpg', clock= 15, increment= 10, rounds= 3, interval= 20, hour= 20, minute= 15)
    tournaments_info += f"{create_tournament_swiss(torre_na_setima)}\n\n"
    time.sleep(time_interval_sleep)
    lua_cheia = Swiss(title= 'Lua Cheia', description= 'https://i.imgur.com/FL35J8p.jpg', clock= 7, increment= 2, rounds= 5, interval= 5, hour= 23, minute= 30)
    tournaments_info += f"{create_tournament_swiss(lua_cheia)}\n\n"
    return(tournaments_info)

def create_tournament_list_p5():
    tournaments_info = ""
    despertador = Arena(title= 'Despertador', description= 'https://i.imgur.com/G7Jsm2A.jpg', clock= 5, increment= 3, duration= 60,hour= 8, minute= 30)
    tournaments_info += f"{create_tournament_arena(despertador)}\n\n"
    time.sleep(time_interval_sleep)
    almoco = Swiss(title= 'Parmegiana', description= 'https://i.imgur.com/amHPhqi.jpg',clock= 10, increment= 2, rounds= 5, interval= 5, hour= 13, minute= 10)
    tournaments_info += f"{create_tournament_swiss(almoco)}\n\n"
    time.sleep(time_interval_sleep)
    naka = Arena(title= 'Naka', description= 'https://i.imgur.com/RyrXllx.jpg', clock= 3, increment= 2, duration= 60, hour= 18, minute= 10)
    tournaments_info += f"{create_tournament_arena(naka)}\n\n"
    time.sleep(time_interval_sleep)
    torre_na_setima = Swiss(title= 'Bobby Fischer', description= 'https://i.imgur.com/H6TSF3Z.jpg', clock= 10, increment= 0, rounds= 5, interval= 10, hour= 20, minute= 0)
    tournaments_info += f"{create_tournament_swiss(torre_na_setima)}\n\n"
    time.sleep(time_interval_sleep)
    carlsen_lobisomen = Swiss(title= 'Carlsen Lobisomen', description= 'https://i.imgur.com/b4TXEzM.jpg', clock= 3, increment= 2, rounds= 7, interval= 5, hour= 23, minute= 30)
    tournaments_info += f"{create_tournament_swiss(carlsen_lobisomen)}\n\n"
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
        case Tournament.Type.P5:
            message_to_send += create_tournament_list_p5()
    if (extra_message != None):
        message_to_send += f"{extra_message.strip()}\n\n"
    message_to_send += "Obrigado e até a próxima!   o/ \n\n🏁🏁🏁♟️🐎🐎🐎♟️🏁🏁🏁"
    time.sleep(time_interval_sleep)
    response = send_message_to_team(message_to_send)
    if response != None:
        if (response["ok"] == True):
            return(message_to_send)
    return(f"Ocorreu um erro ao enviar mensagem para os membros da Equipe no Lichess. Contudo, os torneios foram criados.\n\n{message_to_send}")

def get_tournament_list(list_name):
    response = load_tournament_list(list_name)
    if (response == None):
        response_error_message = f"Ocorreu um erro ao listar os torneios da lista ***{list_name}***. Tente novamente mais tarde."
        return discord.Embed(title=":exclamation: Falha! :exclamation:", description=response_error_message, color= discord.Color.red())
    response_message = f"\n"
    print(response)
    for tournament in response:
        type = tournament["type"]
        title = tournament["title"]
        description = tournament["description"]
        clock = tournament["clock"]
        increment = tournament["increment"]
        hour = fix_hour(tournament["hour"])
        minute = tournament["minute"]
        if (type == "S"):
            type_tournament = "Suiço"
            rounds = tournament["rounds"]
            interval = tournament["interval"]
            response_message += f"• [{type_tournament}] {title} ({clock}+{increment}) - {rounds} RD | {interval}s - {format(hour, '02d')}:{format(minute, '02d')}"
        else:
            type_tournament = "Arena"
            duration = tournament["duration"]
            duration_hours = str(round(duration/60, 2)).replace('.0', '')
            response_message += f"• [{type_tournament}] {title} ({clock}+{increment}) - {duration_hours}h - {format(hour, '02d')}:{format(minute, '02d')}"
        if (description != ""):
            response_message += f" - {description}"
        response_message += f"\n\n"
    return discord.Embed(title=f"Torneios Diários - {list_name}", description=response_message, color= discord.Color.green())

def create_tournament_list(tournament_params):
    if ("," in tournament_params):
        params = tournament_params.split(",")
        size_list_params = len(params)
        if (size_list_params == 2):
            list_name = params[0].strip()
            extra_message = params[1]
        else:
            return(f"Erro ao executar o comando. Confira a sintaxe e tente novamente mais tarde\n\nSintaxe:\n.torneio <nome da lista (p1, p2 ... pn)>, <Recado extra (se houver)>")
    else:
        list_name = tournament_params.strip()
        extra_message = None
    response = load_tournament_list(list_name)
    if (response == None):
        return(f"Ocorreu um erro ao criar os torneios da lista ***{list_name}***. Tente novamente mais tarde.")
    print(response)
    local_dt = datetime.now()
    formatted_date = f"{local_dt.day}/{local_dt.month}/{local_dt.year}"
    message_to_send = f"Bom dia, CXGR ♟️\nOs torneios de hoje (__**{formatted_date}**__) são:\n\n"
    for tournament in response:
        if (tournament["type"] == "S"):
            swiss = map_swiss_tournament(tournament)
            message_to_send += f"{create_tournament_swiss(swiss)}\n\n"
        else:
            arena = map_arena_tournament(tournament)
            message_to_send += f"{create_tournament_arena(arena)}\n\n"
    if (extra_message != None):
        message_to_send += f"{extra_message.strip()}\n\n"
    message_to_send += "Obrigado e até a próxima!   o/ \n\n🏁🏁🏁♟️🐎🐎🐎♟️🏁🏁🏁"
    response = send_message_to_team(message_to_send)
    if response != None:
        if (response["ok"] == True):
            return(message_to_send)
    return(f"Ocorreu um erro ao enviar mensagem para os membros da Equipe no Lichess. Contudo, os torneios foram criados.\n\n{message_to_send}")

def remove_tournament_by_title(tournament_params, sintax):
    params = tournament_params.split(',')
    size_list_params = len(params)
    print(params)
    if size_list_params == 2:
        list_name = params[0].strip()
        title_tournament = params[1].lstrip()
        deletion = delete_tournament(list_name, title_tournament)
        if (deletion):
            response_message = f"\nO torneio foi removido com sucesso da lista ***{list_name}*** de Torneios Diários.\n\n"
            return discord.Embed(title=":white_check_mark:", description=response_message, color= discord.Color.green())
    response_error_message = f"\nNão foi possível remover o torneio. Confira os parâmetros e tente novamente mais tarde.\n\n{sintax}"
    return discord.Embed(title=":exclamation:", description=response_error_message, color= discord.Color.red())

def remove_tournament_by_list_name(list_name, sintax):
    list_name = list_name.strip()
    deletion = delete_all_tournaments_by_pattern_namet(list_name)
    if (deletion):
        response_message = f"\nTodos os torneios da lista ***{list_name}*** de Torneios Diários foram removidos com sucesso.\n\n"
        return discord.Embed(title=":white_check_mark:", description=response_message, color= discord.Color.green())
    response_error_message = f"\nNão foi possível remover os torneios. Confira os parâmetros e tente novamente mais tarde.\n\n{sintax}"
    return discord.Embed(title=":exclamation:", description=response_error_message, color= discord.Color.red())