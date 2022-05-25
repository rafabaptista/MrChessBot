from util.constants import liches_base_url
from config.environment_keys import lichess_access_token

http_get_game_pgn = f"{liches_base_url}/game/export/"
http_export_game_gif = f"{liches_base_url}/game/export/gif/"
http_crosstable = f"{liches_base_url}/api/crosstable/"
http_get_user = f"{liches_base_url}/api/user/"
http_post_new_swiss_tournament = f"{liches_base_url}/api/swiss/new/"

chess_pgn_header = {
    'Content-Type': "application/x-chess-pgn",
    'cache-control': "no-cache"
    }

json_header = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

json_header_post_with_authorization_bot = {
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Authorization': f"Bearer {lichess_access_token}"
}