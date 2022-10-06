from model.tournament import Tournament
from config.environment_keys import bot_team_id

class Swiss(Tournament):
    def __init__(self, title="", description="", clock=0, increment=0, hour=0, minute=0, rounds=0, interval=0):
        super().__init__(title, description, clock, increment, hour, minute, bot_team_id, 0)
        self.rounds = rounds
        self.interval = interval

def map_swiss_tournament(tournament):
    swiss = Swiss()
    swiss.title = tournament["title"]
    swiss.description = tournament["description"]
    swiss.clock = tournament["clock"]
    swiss.increment = tournament["increment"]
    swiss.hour = tournament["hour"]
    swiss.minute = tournament["minute"]
    swiss.rounds = tournament["rounds"]
    swiss.interval = tournament["interval"]
    return(swiss)