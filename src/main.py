import discord
from discord.ext import commands
from config.environment_keys import token
from model.tournament import Tournament
from util.string_helper import is_from_lichess_domain
from version import __version__
from general.cxgr.cxgr_helper import is_user_has_permission_to_create_tournaments
from general.answer import *
from util.constants import *
from config.commands import *
from general.cxgr.cxgr_tournaments import *
from config.environment_keys import *

bot = commands.Bot(command_prefix='.', intents=discord.Intents.default(), case_insensitive=True)

@bot.event
async def on_ready(): 
  print(f"{bot.user} Logged in | Version: {__version__}")

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
    sintax = "Sintaxe:\n.swiss <título>, <descrição>, <relógio>, <incremento>, <nº de rodadas>, <intervalo entre rodadas>, <hora>, <minutos>"
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
    sintax = "Sintaxe:\n.arena <título>, <descrição>, <tempo relógio>, <incremento>, <duração>, <hora>, <minutos>"
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

@bot.command(name= "torneio-p1")
async def tournament_list_p1(ctx, *, extra_message = None):
    await create_tournament(ctx, Tournament.Type.P1, extra_message)

@bot.command(name= "torneio-p2")
async def tournament_list_p2(ctx, *, extra_message = None):
    await create_tournament(ctx, Tournament.Type.P2, extra_message)

@bot.command(name= "torneio-p3")
async def tournament_list_p3(ctx, *, extra_message = None):
    await create_tournament(ctx, Tournament.Type.P3, extra_message)

@bot.command(name= "torneio-p4")
async def tournament_list_p4(ctx, *, extra_message = None):
    await create_tournament(ctx, Tournament.Type.P4, extra_message)

async def create_tournament(ctx, type: Tournament.Type, extra_message = None):
    if is_user_has_permission_to_create_tournaments(ctx.author.roles):
        await ctx.send("Criação de vários Torneios é um pouco demorada.\nFavor aguardar.\n\n")
        response_message = create_tournament_list(type, extra_message)
        await send_bot_simple_text_answer(ctx, response_message)
        return
    await send_no_permission_embed(ctx)

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
    embed_error = discord.Embed(title="Sem permissão", description="Você não pode executar este comando.\nPara criação de torneios é necessário ter o cargo de Administrador.\n\n", color= discord.Color.red())
    await ctx.send(embed= embed_error)

def get_embed_info(text): 
    return discord.Embed(title=":information_source: \n\n", description=text, color= discord.Color.blue())

def get_embed_error(sintax): 
    return discord.Embed(title=":exclamation: \n\nErro ao executar comando", description=f"Favor verificar o comando digitado.\n{sintax}", color= discord.Color.red())

bot.run(token)