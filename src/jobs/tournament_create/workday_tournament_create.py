import json

import requests

# Job scripts do not support global imports, must be in the same level as the script file
from config import *


def main():
    print("Sending signal to Discord Webhook")
    send_request_create_daily_tournament(get_workday_tournament_content_creation())

def get_workday_tournament_content_creation():
    command = command_tournament_create
    tournament_name = weekly_tournament_name
    team_name = bot_team_name
    data = f"{command} {tournament_name}, {team_name} Social:\n"
    if team_whatsapp is not None:
        data += f"WhatsApp: {team_whatsapp}"
    if team_discord is not None:
        data += f"\n\nDiscord: {team_discord}"
    return data

def send_request_create_daily_tournament(content):
    print("Send request to Discord Channel Webhook to create daily tournaments...")
    request_url = http_channel_webhook
    headers = json_header
    content = json.dumps(
        {
            content_param: str(content),
        }
    )
    try:
        print("Url: " + request_url)
        response = requests.post(request_url, headers=headers, data=content, timeout=5)
        response.raise_for_status()
        print("Response Status Code: " + str(response.status_code))
        result = response.text
        return result
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)
    return text_automate_webhook_not_work

if __name__ == '__main__':
    main()
