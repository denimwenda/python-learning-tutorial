age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

#if-else statements
#evaluates two situations
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as you turn 18!")

#if-elif-else statements
#evaluates more than two situations
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission is $5.")
else:
    print("Your admission is $10.")


age = 21
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")

#using multiple elif blocks
age = 81

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 70:
    price = 10
else:
    price = 6

print("Your admission cost is $" + str(price) + ".")

#omitting elif statement
age = 77

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 70:
    price = 10
elif age >= 70:
    price = 7

print("Your admission price will be" + str(price) + ".")