from util.constants import liches_search_url
from config.environment_keys import *
from util.constants import liches_base_url, liches_search_url

def remove_quote(text):
    return(text.replace("\"",""))

def remove_url_scheme(url):
    return(url.replace("https://", "").replace("http://", ""))

def remove_empty_spaces(text):
    return(text.replace(" ", ""))

def remove_comma(text):
    return(text.replace(",", ""))

def is_from_lichess_domain(text):
    if text.startswith(liches_base_url) or text.startswith(liches_search_url) or text.startswith("\"" + liches_base_url):
        return True
    else:
        return False
    
def get_arena_duration_info(hour):
    print(hour)
    duration_info = f""
    time = int(hour * 60)
    duration_info = f"{time}m"
    return duration_info