import json

#Load the username, if it had been stored previously.
#Otherwise, prompt for the username and store it.
def get_stored_username():
    """Get stored name if available"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def greet_user():
    """Greet the user by name"""
    username = input("What is your name? ")
    with open('filename', 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back " + username + "!")

greet_user()