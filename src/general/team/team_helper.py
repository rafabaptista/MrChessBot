from config.environment_keys import administrators_role, daily_tournament_channel_webhook

def is_user_has_permission_to_create_tournaments(roles) -> bool:
    result = next((x for x in roles if x.name == administrators_role), None)
    if result is not None:
        return True
    return False

def is_tournament_webhook(author_id):
    webhook_id = int(daily_tournament_channel_webhook.split("/")[0])
    return author_id == webhook_id