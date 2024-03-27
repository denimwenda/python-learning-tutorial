requested_toppings = 'mushroom'

if requested_toppings != 'anchovies':
    print("Hold the anchovies!")

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your Pizza")

#assignment
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print("You earned 5 points")
if 'yellow' in alien_color:
    print("You earned 10 points.")
if 'red' in alien_color:
    print("You earned 15 points.")


#question
age = 1

if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are an elder")

#using if statements with list
#checking for special item
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding" + requested_topping + ".")

print("\nFinished making your pizza.")

#if the green peppers runs out of stock
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making our Pizza!")

#checking that a list is not empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding" + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza")