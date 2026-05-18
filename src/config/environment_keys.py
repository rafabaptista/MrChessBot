import os

token = os.environ['mrchesskey']
lichess_access_token = os.environ['mrchesslichessapiaccesstoken'] #The token for your Lichess acc bot must be placed in this OS environment
bot_mention = os.environ['botname'] #The BOT's name for your bot must be placed in this OS environment
bot_team_name = os.environ['bot_team_name']
bot_team_id = os.environ['bot_team_id']
administrators_role = os.environ['administrators_role']
team_tournaments_channel_id = os.environ['teamtournamentchannelid'] #Discord specific tournament channel ID
daily_tournament_channel_webhook = os.environ['dailytournamentchannelwebhook'] #Discord specific channel Webhook. i.e.: "1505865903470000000/LqNaQB3yxvy2AB-6muk11j_hklYIZ58ctrUdbN3-tPry0FRvF_wFyhBeirwRVbBw7-gE"
team_whatsapp = os.environ['teamwhatsapp'] #WhatsApp Url for Group Invite
team_discord = os.environ['teamdiscord'] #Discord Url for Group Invite
weekly_tournament_name = os.environ['weeklytournamentname'] #Name of Tournament Weekly List

##Database##
db_client = os.environ['mrchessdbclient']
db_name = os.environ['mrchessdbname']
