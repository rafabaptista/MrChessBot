from enum import Enum

class Tournament:

    def __init__(self, title, description, clock, increment, hour, minute, team_id, starts_at):
        self.title = title
        self.description = description
        self.clock = clock
        self.increment = increment
        self.hour = hour
        self.minute = minute
        self.team_id = team_id
        self.starts_at = starts_at

    class Type(Enum):
        P1 = 1
        P2 = 2
        P3 = 3
        P4 = 4