import json

import requests

from config.strings import text_automate_webhook_not_work
from network.api.discord_webhook.http import http_channel_webhook, json_header, content_param


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
