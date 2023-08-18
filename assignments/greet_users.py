def greet_users(names):
    """Print a simple greeting to each user"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['Ken', 'Den', 'Eta']
greet_users(usernames)

def show_magicians(names):
    """Show magicians names"""

magicians = ['wewert', 'qwerty', 'asdfg']
show_magicians(magicians)