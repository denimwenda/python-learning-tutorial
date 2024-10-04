# Taking input in python
# Python code showing a use of input()
val = input("Enter your value: ")
print(val)


name = input('What is your name?\n')
print(name)

# Program to check input
# Tpe in python
num = input("Enter number: ")
print(num)
name1 = input("Enter name: ")
print(name1)

# Printing type of input value
print("type of number", type(num))
print("type of name", type(name1))

# Taking multiple inputs from user in Python
# Using split() method to get multiple inputs from the user
# Multiple inputs using split
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

# Taking three inputs at a time
x, y, z = input("Enter three value: ").split()
print("Total number of students: ", x)
print("Number of boys is: ", y)
print("Number of girls is: ", z)

# Taking two inputs at a time
a, b = input("Enter two values: ").split()
print("First number is {} and second number is {}".format(a, b))

# Taking multiple inputs at a time and type casting using list() function
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)

# DATA TYPES
# String data type
string_0 = "A Computer Science portal for geeks"
print(string_0)
print(type(string_0))

# Creating a string in several ways
# Create a string in single quotes
string1 = 'Welcome to the Geeks world'
print("String with the use of single quotes")
print(string1)

# Create string with double quotes
string1 = "I'M a Geek"
print("\nString with the use of double quotes")
print(string1)

# Creating a string with triple quotes
string1 = '''I'm a geek and i live in a world of "Geeks"'''
print("\nString with the use of triple quotes")
print(string1)

# Creating string with triple quotes that allows multiple lines
string1 = '''Geeks
            For
            Life'''
print("\nCreating a multiline string")
print(string1)

# Slicing in python
string1 = "GeekForGeeks"
print("Initial String: ")
print(string1)

# Print the 3rd 12th character
print("\nSlicing characters from 3-12: ")
print(string1[3:12])

# Printing characters from 3rd to second last characters
print("\nSlicing characters betweeen " + "3rd and 2nd last chararcter: ")
print(string1[3:-2])

# Creating int and checking type
num = -8

# print the data type
print(type(num))

a = 5
b = 6

# Addition 
c = a + b
print("Addition:",c)

d = 9
e = 6

# Subtraction
f = d - e
print("Subtraction:", f)

# Division
g = 8
h = 2
i = g // 2
print("Division:",i)

# Multiplication
j = 3
k =5
l = j * k
print("Multiplication:",l)

# Booleans
# Pytho program to illutrate built-in method bool()

# Returns False as x s not equal to y
x = 5
y = 10
print(bool(x==y))

# Returns False as x is none
x = None
print(bool(x))

# Returns False as x is an empty sequence
x = ()
print(bool(x))

# Returns False as x is an empty mapping
x = {}
print(bool(x))

# LIST
# Create a list in python
List = []
print("Blank List: ")
print(List)

# Creating a list of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)

# Creating a List of strings and accessing using index
List = ["Geeks", "For", "Geeks"]
print("\nList items: ")
print(List[0])
print(List(2))

# Creating a list with the use of numbers
# Haiving duplicate values
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of numbers: ")
print(List)

# Create a list with mixed data type
# Having numbers and strings
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with the use of mixed values: ")
print(List)

# Getting length of a list
# Creating list
List1 = []
print(len(List1))

#Creating a list of numbers
List2 = [10, 20, 14]
print(len(List2))