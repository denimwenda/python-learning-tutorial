#Writing to a file
#Writing to an empty file
#to write text to a file you need to call function open() and second argument telling python to write
#You can open a file in read mode('r'), write mode('w'), append mode('a') or mode that allows read and write('r+')
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming")

#Writing multiple lines
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

#Appending to a file
#If you want to add a content to a file instead of over writing it use append mode
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love findings meanings in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

user_name = input("What's you name: ")

with open('guest.txt', 'w') as file_object:
    file_object.write(user_name)

print("Your name has been written in guest.txt file")

while True:

    user_name = input("What's your name or enter 'q' to quit")

    if user_name.lower() == 'q':
        break

    print(f"Hello, {user_name}! Welcome to guestbook")

    with open('guest_book.txt', 'w') as file_object:
        file_object.write(user_name + "\n")
