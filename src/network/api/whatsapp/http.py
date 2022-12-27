from config.environment_keys import ultra_message_instance
from util.constants import whatsapp_ultra_message_base_url

http_get_send_message_group = f"{whatsapp_ultra_message_base_url}/{ultra_message_instance}/messages/chat"

json_header = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }