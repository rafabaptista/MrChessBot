from util.constants import liches_search_url
from config.environment_keys import *
from util.constants import liches_base_url, liches_search_url

def remove_quote(text):
    return(text.replace("\"",""))

def remove_url_scheme(url):
    return(url.replace("https://", "").replace("http://", ""))

def remove_bot_mention(text):
    return(
        text.replace(bot_mention, "")
        .replace(bot_name, "")
        .replace(bot_name_lower, "")
        .replace(bot_name_upper, "")
        .replace(bot_name_variant_1, "")
        .replace(bot_name_variant_2, "")
        .replace(bot_name_variant_3, "")
        .replace(bot_name_variant_4, "")
        .replace(bot_name_variant_5, "")
        .replace(bot_name_variant_6, "")
        .replace(bot_name_variant_7, "")
    )

def remove_empty_spaces(text):
    return(text.replace(" ", ""))

def is_from_lichess_domain(text):
    if text.startswith(liches_base_url) or text.startswith(liches_search_url) or text.startswith("\"" + liches_base_url):
        return True
    else:
        return False