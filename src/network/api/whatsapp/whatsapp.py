import requests
from network.api.whatsapp.http import http_get_send_message_group, json_header
from config.environment_keys import whatsapp_group_id, ultra_message_token

def send_whatsapp_group_mesage(message):
    requestUrl = f"{http_get_send_message_group}"
    headers = json_header
    params = {
            'to': whatsapp_group_id,
            'body': message,
            'token': ultra_message_token
            }
    try:
        print("Url: " + requestUrl)
        response = requests.get(requestUrl, headers=headers, params=params, timeout=5)
        response.raise_for_status()
        print("Response Status Code: " + str(response.status_code))
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)