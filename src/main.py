import discord
from discord.ext import commands
from config.environment_keys import token
from util.string_helper import is_from_lichess_domain
from version import __version__
from general.team.team_helper import is_user_has_permission_to_create_tournaments
from general.answer import *
from util.constants import *
from general.team.team_tournaments import *
from config.environment_keys import *

intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True

client = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(command_prefix= '.', intents= intents, case_insensitive= True)

@bot.event
async def on_ready(): 
  print(f"{bot.user} Logged in | Version: {__version__}")
  print(check_database())

@bot.command(name= "ajuda")
async def help(ctx):
    embed_info = get_embed_info(bot_helper)
    await ctx.send(embed= embed_info)

@bot.command(name= "v",)
async def version(ctx):
    embed = discord.Embed(title="Mr. Chess Bot", description=f"Versão: {__version__}", color= discord.Color.purple())
    await ctx.send(embed= embed)

@bot.command(name= "gif")
async def export_pgn(ctx, *, link_match = None):
    sintax = "Sintaxe: .gif <link da partida no Lichess>"
    if link_match == None:
        embed_info = get_embed_info(sintax)
        await ctx.send(embed= embed_info)
        return
    try:
        message_return = ""
        words = link_match.split()
        for word in words:
            print(word)
            if is_from_lichess_domain(word):
                message_return = get_game_gif(word)
                break
        await send_bot_simple_text_answer(ctx, message_return)
    except Exception as errh:
        print(errh)
        embed_error = get_embed_error(sintax)
        await ctx.send(embed= embed_error)

@bot.command(name= "pgn")
async def export_pgn(ctx, *, link_match = None):
    sintax = "Sintaxe: .pgn <link da partida no Lichess>"
    if link_match == None:
        embed_info = get_embed_info(sintax)
        await ctx.send(embed= embed_info)
        return
    try:
        response_message = get_game_pgn(link_match)
        await send_bot_simple_text_answer(ctx, response_message)
    except Exception as errh:
        print(errh)
        embed_error = get_embed_error(sintax)
        await ctx.send(embed= embed_error)

@bot.command(name= "confronto")
async def cross_table(ctx, *, message_received = None):
    sintax = "Sintaxe:\n.confronto <jogador_1>, <jogador_2>"
    if message_received == None:
        embed_info = get_embed_info(sintax)
        await ctx.send(embed= embed_info)
        return
    print(message_received)
    try:
        player_one, player_two = message_received.lower().split(",")
        response_message = get_confronts(player_one.strip(), player_two.strip())
        embed = discord.Embed(title="Confrontos", description=f"{response_message}", color= discord.Color.green())
        await ctx.send(embed= embed)
    except Exception as errh:
        print(errh)
        embed_error = get_embed_error(sintax)
        await ctx.send(embed= embed_error)

@bot.command(name= "perfil")
async def profile(ctx, profile = None):
    sintax = "Sintaxe:\n.perfil <usuário Lichess>"
    if profile == None:
        embed_info = get_embed_info(sintax)
        await ctx.send(embed= embed_info)
        return
    try:
        response_message = get_user_status(profile.strip().lower())
        embed = discord.Embed(title="Perfil do Usuário", description=f"{response_message}", color= discord.Color.green())
        await ctx.send(embed= embed)
    except Exception as errh:
        print(errh)
        embed_error = get_embed_error(sintax)
        await ctx.send(embed= embed_error)

@bot.command(name= "swiss")
async def custom_tournament_swiss(ctx, *, params = None):
    sintax = "Sintaxe:\n.swiss <título>, <descrição>, <relógio>, <incremento>, <nº de rodadas>, <intervalo entre rodadas (em segundos)>, <hora (0..23)>, <minutos (0..59)>"
    try:
        if params == None:
            embed_info = get_embed_info(sintax)
            await ctx.send(embed= embed_info)
            return    
        response_message = create_swis_tournament_with_params(params)
        await send_bot_simple_text_answer(ctx, response_message)
    except Exception as errh:
        print(errh)
        embed_error = get_embed_error(sintax)
        await ctx.send(embed= embed_error)

@bot.command(name= "arena")
async def custom_tournament_arena(ctx, *, params = None):
    sintax = "Sintaxe:\n.arena <título>, <descrição>, <relógio>, <incremento>, <duração (em minutos)>, <hora (0..23)>, <minutos (0..59)>"
    try:
        if params == None:
            embed_info = get_embed_info(sintax)
            await ctx.send(embed= embed_info)
            return    
        response_message = create_arena_tournament_with_params(params)
        await send_bot_simple_text_answer(ctx, response_message)
    except Exception as errh:
        print(errh)
        embed_error = get_embed_error(sintax)
        await ctx.send(embed= embed_error)

@bot.command(name= "torneio")
async def create_daily_tournament_list(ctx, *, params = None):
    if is_user_has_permission_to_create_tournaments(ctx.author.roles):
        sintax = 'Sintaxe:\n.torneio <nome da lista (p1, p2 ... pn)>, <Recado extra (se houver)>'
        try:
            if params == None:
                embed_info = get_embed_info(sintax)
                await ctx.send(embed= embed_info)
                return    
            response_message = create_tournament_list_from_db(params)
            await send_message_tournaments_channel(response_message)
            await send_bot_simple_text_answer(ctx, response_message)
        except Exception as errh:
            print(errh)
            embed_error = get_embed_error(sintax)
            await ctx.send(embed= embed_error)
        return
    await send_no_permission_embed(ctx)

@bot.command(name= "adicionar-torneio-swiss")
async def add_tournament_swiss(ctx, *, params = None):
    if is_user_has_permission_to_create_tournaments(ctx.author.roles):
        sintax = 'Sintaxe:\n.adicionar-torneio-swiss <nome da lista (p1, p2 ... pn)>, <título>, <descrição>, '\
            '<tempo relógio (em minutos)>, <incremento (em segundos)>, <nº de rodadas>, <intervalo entre rodadas (em segundos)>, '\
            '<hora (0..23)>, <minutos (0..60)>'
        try:
            if params == None:
                embed_info = get_embed_info(sintax)
                await ctx.send(embed= embed_info)
                return    
            response_embed = add_swis_tournament_to_list_with_params(params)
            await ctx.send(embed= response_embed)
        except Exception as errh:
            print(errh)
            embed_error = get_embed_error(sintax)
            await ctx.send(embed= embed_error)
        return
    await send_no_permission_embed(ctx)

@bot.command(name= "adicionar-torneio-arena")
async def add_tournament_arena(ctx, *, params = None):
    if is_user_has_permission_to_create_tournaments(ctx.author.roles):
        sintax = 'Sintaxe:\n.adicionar-torneio-arena <nome da lista (p1, p2 ... pn)>, <título>, <descrição>, <tempo relógio (em minutos)>, '\
            '<incremento (em segundos)>, <duração (em minutos)>, <hora (0..23)>, <minutos (0..59)>'
        try:
            if params == None:
                embed_info = get_embed_info(sintax)
                await ctx.send(embed= embed_info)
                return    
            response_embed = add_arena_tournament_to_list_with_params(params)
            await ctx.send(embed= response_embed)
        except Exception as errh:
            print(errh)
            embed_error = get_embed_error(sintax)
            await ctx.send(embed= embed_error)
        return
    await send_no_permission_embed(ctx)

@bot.command(name= "listar-torneio")
async def list_tournament(ctx, *, list_name = None):
    sintax = "Sintaxe:\n.listar-torneio <nome da lista (p1, p2 ... pn)>"
    try:
        if list_name == None:
            embed_info = get_embed_info(sintax)
            await ctx.send(embed= embed_info)
            return    
        response_embed = get_tournament_list(list_name.strip())
        await ctx.send(embed= response_embed)
    except Exception as errh:
        print(errh)
        embed_error = get_embed_error(sintax)
        await ctx.send(embed= embed_error)

@bot.command(name= "remover-torneio")
async def remove_tournament(ctx, *, params = None):
    sintax = "Sintaxe:\n.remover-torneio <nome da lista (p1, p2 ... pn)>, <título do torneio (exatamente igual ao torneio inserido)>"
    try:
        if params == None:
            embed_info = get_embed_info(sintax)
            await ctx.send(embed= embed_info)
            return    
        response_embed = remove_tournament_by_title(params, sintax)
        await ctx.send(embed= response_embed)
    except Exception as errh:
        print(errh)
        embed_error = get_embed_error(sintax)
        await ctx.send(embed= embed_error)

@bot.command(name= "remover-lista-torneio")
async def remove_all_tournaments_by_list(ctx, *, list_name = None):
    sintax = "Sintaxe:\n.remover-lista-torneio <nome da lista (p1, p2 ... pn)>"
    try:
        if list_name == None:
            embed_info = get_embed_info(sintax)
            await ctx.send(embed= embed_info)
            return    
        response_embed = remove_tournament_by_list_name(list_name, sintax)
        await ctx.send(embed= response_embed)
    except Exception as errh:
        print(errh)
        embed_error = get_embed_error(sintax)
        await ctx.send(embed= embed_error)

@bot.command(name="bot")
async def challenge_bot(ctx, *, params=None):
    answer = 'Para me desafiar no Lichess, basta clicar no link abaixo:\nhttps://lichess.org/?user=MrChessTheBot#friend'
    await send_bot_simple_text_answer(ctx, answer)

async def send_bot_simple_text_answer(ctx, text):
    length = len(text)
    if length < maximum_lenght_characters:
      await ctx.send(text)
    else:
      file = open(large_file_name,"w+")
      file.write(text)
      file.close()
      with open(large_file_name, "rb") as file:
        await ctx.send("O resultado é muito grande. Tive que gerar um arquivo:", file=discord.File(file, large_file_name))

async def send_no_permission_embed(ctx):
    embed_error = discord.Embed(
        title="Sem permissão", 
        description="Você não pode executar este comando.\nPara criação de torneios é necessário ter o cargo de **Administrador**.\n\n", 
        color= discord.Color.red())
    await ctx.send(embed= embed_error)

async def send_message_tournaments_channel(text):
    channel_id = int(team_tournaments_channel_id)
    channel = bot.get_channel(channel_id)
    length = len(text)
    if length < maximum_lenght_characters:
      await channel.send(text)
    else:
      file = open(large_file_name,"w+")
      file.write(text)
      file.close()
      with open(large_file_name, "rb") as file:
        await channel.send("O resultado é muito grande. Tive que gerar um arquivo:", file=discord.File(file, large_file_name))
    

def get_embed_info(text): 
    return discord.Embed(title=":information_source: \n\n", description=text, color= discord.Color.blue())

def get_embed_error(sintax): 
    return discord.Embed(title=":exclamation: \n\nErro ao executar comando", description=f"Tente novamente mais tarde ou verifique o comando digitado:\n{sintax}", color= discord.Color.red())

bot.run(token)