usernames = ['denny', 'kenneth', 'admin', 'tony', 'sharon']
for username in usernames:
    print("Hello " + username + ".")

usernames = ['denny', 'kenneth', 'admin', 'tony', 'sharon']
if usernames == 'admin':
    print("Hello" + username + ".")

usernames = []
if usernames:
    for username in usernames:
        print("Thank you, users")
else:
    print("We need to look for users")

#Removing all instances of a specific value in a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

#Filling a dictionary with user input
responses = {}

#Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    #Prompt for the persons name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    #Store the response in the dictionary
    responses[name] = response

    #Find out if anyone is going to take the poll
    repeat = input("Would you like to let another person to respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

#Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")