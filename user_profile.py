def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about the user"""
    profile = {}
    profile['first name'] = first
    profile['last'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location ='princeton',
                             field='phycics')
print(user_profile)