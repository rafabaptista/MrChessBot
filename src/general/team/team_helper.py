from config.environment_keys import administrators_role

def is_user_has_permission_to_create_tournaments(roles) -> bool:
    result = next((x for x in roles if x.name == administrators_role), None)
    if (result != None):
        return(True)
    return(False)