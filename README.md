# MrChessBot

<p>
<a href="https://top.gg/bot/976038110540496976"><img alt="Bot status widget" src="https://top.gg/api/widget/status/976038110540496976.svg"></a>
<a href="https://github.com/UltiRequiem/python-projects-for-intermediates/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
</p>
   
A Discord BOT integrated with Lichess Platform

## Description
This bot integrates with the lichess.org chess website. 
All the Discord BOT messages are only in pt-BR at this moment.

## Default prefix
Mention the BOT in Discord along with the command

## GENERAL COMMANDS 
* `.ajuda` → show list of commands
* `.gif <url_lichess_game>` → Show a GIF from the the match (the match must be ended already).
* `.pgn <url_lichess_game>` → show the PGN from the match.
* `.perfil <user_name_from_lichess>` → show the statiscs from the user.
* `.confronto <user_name_1>, <user_name_2>` → show the statistics from the matches between two players.
* `.swiss <title>, <description>, <clock>, <increment>, <rounds>, <interval>, <hour>, <minutes>` → create Swiss tournament based
* `.arena <title>, <description>, <clock>, <increment>, <duration>, <hour>, <minutes>` → create Swiss tournament
* `.bot` → Receives a link to challenge MrChessTheBot Lichess BOT

## TOURNAMENT MANAGEMENT COMMANDS
* `.adicionar-torneio-swiss <tournament list name>, <Tournament name>, <Tournament description>, <clock time (minutes)>, <increment (seconds)>, <number of rounds>, <interval between rounds (seconds)>, <hour of the tournament's start (0..23)>, <minuts of the tournament's start (0..60)>` → Register SWISS tournament in the tournament list specified
* `.adicionar-torneio-arena <tournament list name>, <Tournament name>, <Tournament description>, <clock time (minutes)>, <increment (seconds)>, <duration of the tournament (minutes)>, <hour of the tournament's start (0..23)>, <minuts of the tournament's start (0..60)>` → Register ARENA tournament in the tournament list specified
* `.remover-torneio <tournament list name>, <Tournament name>` → Remove the tournament from the specified list
* `.listar-torneio <tournament list name>` → Display tornaments from a list
* `.torneio <tournament list name>, <Aditional description>` → Create tournaments from a list in the Lichess team. Aditional desription is optional

## Help / Contact / Issues / Requests / Collaboration
Questions, issues and requests can be posted as an issue in this repository or send in the Discord below:
[Mr Chess, the Bot Discord Server](https://discord.gg/TpDQkekzfX)

## HOW TO SETUP
1) Clone this repo
2) Create a Mongo DB database
    * Create collection with name `torneios`
3) Create your own branch
4) Setup Environment Variables:
    1. `botname`: Discord bot ID
    2. `mrchesskey`: Discord bot key
    3. `mrchesslichessapiaccesstoken`: Lichess user token (will be the user responsible to create the tournaments)
    4. `PORT`(Server production only, no need for local): 8080
    5. `TZ`(Server production only, no need for local): Server Time Zone. i.e. -> America/Sao_Paulo
    6. `mrchessdbclient`: Mongo DB uri
    7. `mrchessdbname`: Mongo DB Database ID
    8. `teamtournamentchannelid`: Discord Channel to post tournament messages after creation
    9. `bot_team_id`: Lichess team name (as displayed in the team URL)
    10. `bot_team_name`: Name of the Lichess team to be displayed in the messages
    11. `administrators_role`: Discord rule name, allowd to execute commands to create tournaments. i.e. -> `Administrators`

## PULL REQUESTS
* All changes must be submitted as Pull Request.
* All Pull Requests will be reviewed by `rafabaptista`.

## CONTACT
* Send email to rafabapdev@gmail.com

## Screenshots
![Mr Chess, the Bot](/media/MrChessBotProfImage.png)
