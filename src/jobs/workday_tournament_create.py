from config.environment_keys import weekly_tournament_name, bot_team_name, team_whatsapp, team_discord
from config.strings import command_tournament_create
from network.api.discord_webhook.daily_tournament_creation import send_request_create_daily_tournament

def main():
    print("Sending signal to Discord Webhook")
    send_request_create_daily_tournament(get_workday_tournament_content_creation())

def get_workday_tournament_content_creation():
    command = command_tournament_create
    tournament_name = weekly_tournament_name
    team_name = bot_team_name
    data = f"{command} {tournament_name}, {team_name} Social:\n"
    if team_whatsapp is not None:
        data += f"WhatsApp: {team_whatsapp}"
    if team_discord is not None:
        data += f"\n\nDiscord: {team_discord}"
    return data

if __name__ == '__main__':
    main()
