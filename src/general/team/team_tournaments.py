from network.api.lichess.lichess import create_swiss_tournament, create_arena_tournament
from network.api.lichess.lichess import send_message_to_team
from config.environment_keys import bot_team_id, bot_team_name
from model.tournament import fix_hour
from model.arena import Arena, map_arena_tournament
from model.swiss import Swiss, map_swiss_tournament
from model.tournament import Tournament
from util.constants import swiss_tournament_link, arena_tournament_link
from datetime import datetime
from dateutil.relativedelta import relativedelta
from network.db.dal import *
import discord

time_interval_sleep = 1

def create_tournament_arena(arena: Arena):
    arena.team_id = bot_team_id
    local_dt = datetime.now()
    duration_hours = str(round(arena.duration/60, 2)).replace('.0', '')
    tournament_hour = fix_hour(arena.hour)
    arena.starts_at = get_tournament_start_time(arena)
    response = create_arena_tournament(arena)
    if response != None:
        tournament_id = response["id"]
        return(f"[Arena] {arena.title} ({arena.clock}+{arena.increment}) - {duration_hours}h - {format(tournament_hour, '02d')}:{format(arena.minute, '02d')}:\n{arena_tournament_link}{tournament_id}")
    return(f"Não foi possível criar o torneio {arena.title} hoje. Desculpe =/")

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
    tournament_hour = fix_hour(swiss.hour)
    swiss.starts_at = get_tournament_start_time(swiss)
    response = create_swiss_tournament(swiss)
    if response != None:
        if (response["status"] == "created"):
            tournament_id = response["id"]
            return(f"[Suiço] {swiss.title} ({clock_time}+{swiss.increment}) - {swiss.rounds} RD - {format(tournament_hour, '02d')}:{format(swiss.minute, '02d')}:\n{swiss_tournament_link}{tournament_id}")
    return(f"Não foi possível criar o torneio {swiss.title} hoje. Desculpe =/")

def get_tournament_start_time(tournament: Tournament):
    local_dt = datetime.now()
    tournament_hour = fix_hour(tournament.hour)
    if (tournament_hour >= 0 and tournament_hour <= 2):
        if (local_dt.month == 12 and local_dt.day == 31): #las day of the year
            new_date = datetime(local_dt.year + 1, 1, 1, tournament_hour,tournament. minute, 0, 0) #Jannuary 1 from the next year
        else:
            last_date_of_month = local_dt + relativedelta(day=31)
            if (local_dt.day == last_date_of_month.day): #las day of the month
                new_date = datetime(local_dt.year, local_dt.month + 1, 1, tournament_hour,tournament. minute, 0, 0) #Brazil's zone [Sao Paulo]
            else:
                new_date = datetime(local_dt.year, local_dt.month, local_dt.day + 1, tournament_hour,tournament. minute, 0, 0) #Brazil's zone [Sao Paulo]
    else:
        new_date = datetime(local_dt.year, local_dt.month, local_dt.day, tournament_hour, tournament.minute, 0, 0) #Brazil's zone [Sao Paulo]
    time_converted = new_date.strftime('%s')
    return int(float(time_converted)*1000)

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

def create_tournament_list_from_db(tournament_params):
    if ("," in tournament_params):
        params = tournament_params.split(",")
        list_name = params[0].strip()
        extra_message = tournament_params.replace(f"{list_name}", "").replace(",", "", 1)
    else:
        list_name = tournament_params.strip()
        extra_message = None
    response = load_tournament_list(list_name)
    if (response == None):
        return(f"Ocorreu um erro ao criar os torneios da lista ***{list_name}***. Tente novamente mais tarde.")
    print(response)
    local_dt = datetime.now()
    formatted_date = f"{local_dt.day}/{local_dt.month}/{local_dt.year}"
    message_to_send = f"Bom dia, {bot_team_name} ♟️\nOs torneios de hoje ({formatted_date}) são:\n\n"
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
    response_message = send_message_to_team(message_to_send)
    if response_message != None:
        if (response_message["ok"] == True):
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

def check_database():
    response = check_db_connection()
    if (response == True):
        response_message = "====> D.B. Check: > SUCCESS < ..."
    else:
        response_message = "#### Error to connect to D.B."
    return response_message