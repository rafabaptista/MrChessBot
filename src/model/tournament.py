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

def fix_hour(hour):
    fixed_hour = 0
    match hour:
        case 24:
            fixed_hour = 0
        case 25:
            fixed_hour = 1
        case 26:
            fixed_hour = 2
        case other:
            fixed_hour = hour
    return(fixed_hour)