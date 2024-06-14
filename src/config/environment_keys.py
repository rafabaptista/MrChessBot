import os

token = os.environ['mrchesskey']
lichess_access_token = os.environ['mrchesslichessapiaccesstoken'] #The token for your Lichess acc bot must be placed in this OS environment
bot_mention = os.environ['botname'] #The BOT's name for your bot must be placed in this OS environment
bot_team_name = os.environ['bot_team_name']
bot_team_id = os.environ['bot_team_id']
administrators_role = os.environ['administrators_role']
team_tournaments_channel_id = os.environ['teamtournamentchannelid'] #Discord specific tournament channel ID

##Database##
db_client = os.environ['mrchessdbclient']
db_name = os.environ['mrchessdbname']