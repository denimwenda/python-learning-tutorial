#Defining a function
#Docstring """ """
def greet_user():
    """Display a simple greetings"""
    print("Hello!")

greet_user()

#Passing information to a function
def greet_user(username):
 """Display a simple greeting."""
 print("Hello, " + username.title() + "!")

greet_user('jesse')

#Functions are named blocks of code that are designed to do a specific job
#arguments and parameters
#Prameters is a piece of information that function needs to do it's job
#An argument is a piece of information that is passed from a funcion call to function
def display_message():
    """prints a message"""
    print("Am learnig about functions")

display_message()

def favorite_book(name):
    """prints a message"""
    print("One of my favorite books is, " + name.title() + ".")

favorite_book('Alice in Wonderland')

#Passing arguments
#You can pass arguments in number of ways: Positional or Keyword arguments

#Positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')

#Multiple functon calls
def describe_pet(animal_type, pet_name):
    """Displaying information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#Keyword Arguments is a name value pair that you pass to a function
def describe_pet(animal_type, pet_name):
    """Displaying information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='willie', animal_type='dog')

#Equivalent function calls
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#A dog named Willie
describe_pet('Willie')
describe_pet(pet_name='Willie')

#Ahamster named Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

def make_shirt(size, text):
    """Displaying information about a shirt"""
    print("\nMy shirt size is " + size + '.')
    print("My shirt should be printed the following: " + text.title() + ".")

make_shirt('27', 'i love python')
make_shirt(text='i love python', size='27')

#Returning value
#Returning a simple value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('ream', 'tarus')
print(musician)

def get_formatted_name(first_name, middle_name, last_name):
    """Display formatted name"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

magician = get_formatted_name('swan', 'alan', 'walker')
print(magician)

#Making an argument optional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted """
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

magician = get_formatted_name('ream', 'tarus')
print(magician)

musician = get_formatted_name('swan', 'alan', 'walker')
print(musician)

#Returning a dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information of a person"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('ream', 'tarus')
print(musician)

def build_person(first_name, last_name, age=None):
    """Return dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

magician = build_person('jimi', 'hendrix', age=27)
print(magician)

#Using a function with a while loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

#This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello " + formatted_name + "!")


def get_city_country(city, country):
    """Display a well formatted city"""
    countrys = city + ', ' + country
    return countrys.title()

countrys = get_city_country('Nairobi', 'kenya')
print(countrys)

def get_make_album(artist_name, album_title):
    """Display a dictionary of information"""
    celeb = {'artist': artist_name, 'album': album_title}
    return celeb

celeb = get_make_album('Otile', 'jeraha')
celeb = get_make_album('jason', 'make love not war')
print(celeb)

def get_make_album(artist_name, album_tittle):
    celeb = artist_name + ' ' + album_tittle
    return celeb.title()

while True:
    print("\nWhat is the name of your celeb: ")
    print("(Enter 'q' to quit)")
    a_name = input("What is your name: ")
    if a_name == 'q':
        break
    a_title = input("What is the title: ")
    if a_title == 'q':
        break

    celeb = get_make_album(a_name, a_title)
    print(celeb)