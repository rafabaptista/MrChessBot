import os

bot_team_name = os.environ['bot_team_name']
weekly_tournament_name = os.environ['weeklytournamentname']
team_whatsapp = os.environ['teamwhatsapp']
team_discord = os.environ['teamdiscord']
daily_tournament_channel_webhook = os.environ['dailytournamentchannelwebhook']
command_tournament_create = ".torneio"
text_automate_webhook_not_work = "Não foi possível executar Webhook"
discord_webhook_url = "https://discord.com/api/webhooks/"
http_channel_webhook = f"{discord_webhook_url}{daily_tournament_channel_webhook}"
content_param = "content"
json_header = {
    'Content-Type': "application/json"
}