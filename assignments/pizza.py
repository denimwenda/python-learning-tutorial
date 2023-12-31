#A list in a dictionary
#Store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

#Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

#Using continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

#Avoiding infinite loops
x = 1
while x <= 5:
    print(x)
    x += 1

#Using while loop with Lists and Dictionary
#Moving one list from one list to Another

#Start with users that want to be verified
#and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#Verify each user until there are no more unconfirmed users.
#Move each confirmed user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_number)

#Display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user)

#Passing an arbitray number of arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')

#Storing your functions in modules
#Modules makes it easy to import a program
#Ways of importing module

#1. Importing an entire module
#We need first to create a module. A module is a file ending with .py that contains code to import
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)