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