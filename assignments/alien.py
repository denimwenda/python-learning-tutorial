#dictionary in python is a collection of key-value pairs
#dictionary is wrapped in braces{}
alien_0 = {'color' : 'green', 'points' : 5}

print(alien_0['color'])
print(alien_0['points'])

#accessing value in a dictionary
alien_0 = {'color' : 'green'}
print(alien_0['color'])

alien_0 = {'color' : 'green', 'points' : 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

#adding new key-value pairs
alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#starting with an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

#modifying value in a dictionary
alien_0 = {'color' : 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien color now is " + alien_0['color'] + ".")

alien_0 ={'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

#Move the alien to the right.
#Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #this must be a faster alien
    x_increment = 3

#The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

#using del statement to delete key-value pairs
alien_0 = {'color' : 'green' , 'points' : 5}
print(alien_0)

del alien_0['points']
print(alien_0)

number = input("Enter a number, and i will tell you whether it's even or old: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even")
else:
    print("\nThe number " + str(number) + " is odd")

car = input("Which type of car do you want: ")
print("Let me see if i can find you a " + str(car) + ".")

group = input("How many people are in the dinner group: ")
group = int(group)

if group <= 8:
    print("The table is ready.")
else:
    print("You will have to wait.")

prompt = "\nTell me something, and i will tell it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

#using break to exit a loop
prompt = "\nPlease enter the name of the city you have ever visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

