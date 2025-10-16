def user_is_auth(user):
    if user.is_authenticated:
        return 0 
    return 1