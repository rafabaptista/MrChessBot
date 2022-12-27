import os
#The token for your bot must be placed in this OS environment
token = os.environ['mrchesskey'] 
#token = os.environ['mrchesstestkey'] #for test
lichess_access_token = os.environ['mrchesslichessapiaccesstoken'] #The token for your Lichess acc bot must be placed in this OS environment
bot_mention = os.environ['botname'] #The BOT's name for your bot must be placed in this OS environment
bot_name_lower = "@mrchessbot"
bot_name_upper = "@MRCHESSBOT"
bot_name = "@MrChessBot"
bot_name_variant_1 = "@MrchessBot"
bot_name_variant_2 = "@Mrchessbot"
bot_name_variant_3 = "@MrchessBot"
bot_name_variant_4 = "@MrChessbot"
bot_name_variant_5 = "@mrChessbot"
bot_name_variant_6 = "@mrChessBot"
bot_name_variant_7 = "@mrChessBOT"
bot_team_id = "cxgr"
#bot_team_id = "ccmh" #for test
administrators_role = "Administradores"

##Database##
db_client = os.environ['mrchessdbclient']
db_name = os.environ['mrchessdbname']

##WhatsApp##
ultra_message_instance = os.environ['ultramessageinstance'] #The Ultra message Instance
ultra_message_token = os.environ['ultramessagetoken'] #The Ultra message Token
whatsapp_group_id = os.environ['whatsappgroupid'] #WhatsApp Group ID from the group to send the message
cxgr_tournaments_channel_id = os.environ['cxgrtournamentchannelid'] #Discord specific tournament channel ID