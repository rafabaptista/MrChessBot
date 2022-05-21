from util.constants import liches_base_url

http_get_game_pgn = f"{liches_base_url}/game/export/"
http_export_game_gif = f"{liches_base_url}/game/export/gif/"
http_crosstable = f"{liches_base_url}/api/crosstable/"
http_get_user = f"{liches_base_url}/api/user/"

chess_pgn_header = {
    'Content-Type': "application/x-chess-pgn",
    'cache-control': "no-cache"
    }

json_header = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }