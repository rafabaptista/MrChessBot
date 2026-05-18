from util.constants import discord_webhook_url
from config.environment_keys import daily_tournament_channel_webhook

http_channel_webhook = f"{discord_webhook_url}{daily_tournament_channel_webhook}"
content_param = "content"

json_header = {
    'Content-Type': "application/json"
}
