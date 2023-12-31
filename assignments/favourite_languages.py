favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'ptyhon',
    }

print("Sarah's favourite language is " +
      favourite_languages['sarah'].title() + ".")

person = {'fisrt_name' : 'jason', 'last_name' : 'grort', 'age' : 34, 'city': 'mombasa'}
print(person)

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + ".")

for name in favourite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() + " i see your favourite language is " + favourite_languages[name].title() + "!")

if 'enrin' not in favourite_languages.keys():
    print("Enrin, please take our poll!")

#looping through a dictionary's keys in order
#use sorted() function
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'ptyhon',
    }

for name in sorted(favourite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

#looping through all values in a dictionary
print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    }

for name, language in favourite_languages.items():
    print("\n" + name.title() + "'s favorite language are:")
    for language in favourite_languages:
        print("\t" + language.title())

from collections import OrderedDict

favourite_languages = OrderedDict()

favourite_languages['jen'] = 'python'
favourite_languages['sarah'] = 'c'
favourite_languages['edward'] = 'ruby'
favourite_languages['phil'] = 'python'

for name, language in favourite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + '.')