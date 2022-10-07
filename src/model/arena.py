from model.tournament import Tournament
from config.environment_keys import bot_team_id

class Arena(Tournament):
    def __init__(self, title="", description="", clock=0, increment=0, hour=0, minute=0, duration=0):
        super().__init__(title, description, clock, increment, hour, minute, bot_team_id, 0)
        self.duration = duration

def map_arena_tournament(tournament):
    arena = Arena()
    arena.title = tournament["title"]
    arena.description = tournament["description"]
    arena.clock = tournament["clock"]
    arena.increment = tournament["increment"]
    arena.hour = tournament["hour"]
    arena.minute = tournament["minute"]
    arena.duration = tournament["duration"]
    return(arena)