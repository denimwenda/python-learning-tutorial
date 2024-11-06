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

# Accessing elements from the list
# Creating a List with the use of multiple values
List = ["Geeks", "For", "Geeks"]

# Accessing a element from the list using index number
print("Accessing a element from the list")
print(List[0])
print(List[2])

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Geeks', 'For'], ['Geeks']]

# Accessing an element from the Multi-Dimensional list using index number
print("Accessing a element from a Multi-Dimenional list")
print(List[0][1])
print(List[1][0])

# Negative indexing
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("Accessing element using negative indexing")

# Print the last element of the list
print(List[-1])

# Print the third last element of list
print(List[-3])

# Taking input of a python list
# input the list as string
string = input("Enter elements (Space-Separated): ")

# Split the string and store it to a list
lst = string.split()
print('The list is', lst)

# Adding Elements to a list
# Create a list
List = []
print("Initial blank List: ")
print(List)

# Addition of Elements in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addiction of three elements: ")
print(List)

# Adding elements to the list using iterator
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)

# Adding Tuples to the list
List.append((5, 6))
print("\nLiast addition of a Tuple: ")
print(List)

# Addition of a List to List
List2 = ['For', 'Geeks']
List.append("\nList after addition of a List: ")
print(List)

# Adding element using insert() method
# Creating a List
List = [1,2,3,4]
print("Intial List: ")
print(List)

# Additon of Element at specific position using insert method
List.insert(3, 12)
List.insert(0, 'Geeks')
print("\nList after performing insert operation: ")
print(List)

# Additon of Element at specific position using extend method
# Creating a List
List = [1, 2, 3, 4]
print("Initial List: ")
print(List)

# Addition of multiple elements to the list usint extend method
List.extend[8, 'Geeks', 'Always']
print("\nList after performing Extend Operation: ")
print(List)

# Reversing a list
mylist = [1, 2, 3, 4, 5, 'Geek', 'Python']
mylist.reverse()
print(mylist)

my_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(my_list))
print(reversed_list)

# Removing elements in a list
# Creating a list
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(List)

# Removing elements from a list using Remove() method
List.remove(5)
List.remove(6)
print("\nList after removal of two elements: ")
print[List]

# Creating a list
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Removing elements from list using iterator method
for i in range(1, 5):
    print("\nList after removing a range of elements: ")
    print(List)

# Using pop() method
List = [1, 2, 3, 4, 5]

# Removing element from the set using pop() method
List.pop()
print("\nList after popping an element: ")
print(List)

# Removng element at a specific location from the set using the pop() method
List.pop(2)
print("\nList after popping a specifc element: ")
print(List)

# TUPLE
# Creating an empty tuple
Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)

# Creating a tuple with the use of string
Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of string: ")
print(Tuple1)

# Creating a tuple with the use of a list
list1 = [1, 2, 3, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

# Creating a tuple with the use of built-infunction
Tuple1 = tuple('Geeks')
print("\nTuple with the use of functions: ")
print(Tuple1)

# Creating a Tuple
# with Mixed Datatype
Tuple1 = (5, 'Welcome', 7, 'Geeks')
print("\nTuple with Mixed Datatypes: ")
print(Tuple1)

# Creating a Tuple
# with nested tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

# Creating a Tuple
# with repetition
Tuple1 = ('Geeks',) * 3
print("\nTuple with repetition: ")
print(Tuple1)

# Creating a Tuple
# with the use of loop
Tuple1 = ('Geeks')
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1)# Accessing Tuple

# with Indexing
Tuple1 = tuple("Geeks")
print("\nFirst element of Tuple: ")
print(Tuple1[0])


# Tuple unpacking
Tuple1 = ("Geeks", "For", "Geeks")

# This line unpack
# values of Tuple1
a, b, c = Tuple1
print("\nValues after unpacking: ")
print(a)
print(b)
print(c)

# Concatenation of tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Geeks', 'For', 'Geeks')

Tuple3 = Tuple1 + Tuple2

# Printing first tuple
print("Tuple 1: ")
print(Tuple1)

# printing second tuple
print("\nTuple 2: ")
print(Tuple2)

# Printng final tuple
print("\nTuples after concatenation: ")
print(Tuple3)

# Slicing of Tuples
# Slicing with numbers
Tuple1 = tuple('GEEKSFORGEEKS')

# Removing first element
print('Removal of first element: ')
print(Tuple1[1:])

# Reversing the tuple
print("\nTuple after sequenceof Element is reversed: ")
print(Tuple1[::-1])

# Printing elements of a range
print("\nPrinting elements between Range 4-9: ")
print(Tuple1[4:9])

# Deleting  a tuple
Tuple1 = (0, 1, 2, 3, 4)
del Tuple1

print(Tuple1)

# SETS
# Creatng a set
set1 = set()
print("Initial blank set: ")
print(set1)

# Creating a set with the use of a string
set1 = set("GEEKSFORGEEKS")
print("\nSet with the use of string: ")
print(set1)

String = 'GeeksForGeeks'
set1 = set(String)
print("\nSet with the use of an object: ")
print(set1)

# Creating set with the use of a list
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with use of list:")
print(set1)

# Creating set with the use of a tuple
t = ("Geeks", "for", "Geeks")
print("\nSet with the use of tuple: ")
print(set(t))

# Creating a set with the use of a dictionary
d = {"Geeks": 1, "for": 2, "Geeks": 3}
print("\nSet with the use of Dctionary: ")
print(set(d))

# Adding elements to a set.
# Creating a list
set1 = set()
print("Initial blank set: ")
print(set1)

# Adding element and tuple to the set.
set1.add(8)
set1.add(9)
set1.add((6, 7))
print("\nSet after addition of three elements: ")
print(set1)

# Adding elements to the set using iterator
for i in range(1, 6):
    set1.add(i)
print("\nSet after addition of elements from 1-5: ")

# Addition of elements to the set using update function
set1 = set([4, 5, (6, 7)])
set1.update([10, 11])
print("\nSet after Addition of elements using update: ")
print(set1)

# Accessing a set
# Create a set
set1 = set(["Geeks", "For", "Geeks"])
print("\nInitial set")
print(set1)

# Accessing element using for loop
print("\nElements of set: ")
for i in set1:
    print(i, end=" ")
    
# Checking the element using keyworld
print("\n")
print("Geeks" in set1)

# Removing elements from a set
# Creating a set
set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Initial set: ")
print(set1)

# Removing elements from set using Remove() method
set1.remove(5)
set1.remove(6)
print("\nSet after removal of two elements: ")
print(set1)

# Removing elements from set using Discard() method
set1.discard(8)
set1.discard(9)
print("\nSet after discarding two elements: ")
print(set1)

# Removing elements from set using iterator method
for i in range(1, 5):
    set1.remove(i)
    print("\nSet after removing a range of elements: ")
    print(set1)
    
# DICTIONARY
Dict = {}
print("Empty Dictionary: ")
print(Dict)

Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionar with the use of dict(): ")
print(Dict)

Dict = dict([(1, 'Geeks'), 2, 'For'])
print("\nDictionar with each item as apair: ")
print(Dict)

Dict = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

# Adding elements to a dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding three elements: ")
print(Dict)

Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)

Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)
Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print("\nAdding a Nested key: ")
print(Dict)

# Accessing elements of a dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print("Accessing an element using key: ")
print(Dict['name'])
print("Accessing a element using key: ")
print(Dict[1])

Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

print("Accesssing a element using get: ")
print(Dict.get(3))

# Accessing an element of a Nested Dictionary
Dict = {'Dict': {1: 'Geeks'}, 'Dict2': {'Name': 'For'}}
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])

# Deleting elements in a dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

print("Dctionary =")
print(Dict)
del(Dict[1])
print("Data after deletion Dictionary=")
print(Dict)

dict1 = {1: "python", 2: "Java", 3: "Ruby", 4: "Scala"}
dict2 = dict1.copy()
print(dict2)
dict1.clear()
print(dict1)
print(dict2.get(1))
print(dict2.items())
print(dict2.keys())
dict2.pop(4)
print(dict2)
dict2.popitem()
print(dict2)
dict2.update({3: "Scala"})
print(dict2)
print(dict2.values())

# ARRAYS
# Creating an array
import array as arr
a = arr.array('i', [1, 2, 3])
print("The new craeted array is: ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()
b = arr.array('d', [2.5, 3.2, 3.3])
print("\nThe new created array is: ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
    
# Adding an Element to a python array.
import array as arr
a = arr.array('i', [1, 2, 3])
print("Array before insertion: ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()
a.insert(1, 4)
print("Array after insertion: ", end=" ")
for i in (a):
    print(i, end=" ")
b = arr.array('d', [2.5, 3.2, 3.3])
print("Array before insertion: ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
b.append(4.4)
print("Array after insertion: ", end=" ")
for i in (b):
    print(i, end=" ")
print()

# Accessing an array
import array as arr
a.arr.array('i', [1, 2, 3, 4, 5, 6])
print("Access element is: ", a[0])
print("Access element is: ", a[3])
b = arr.array('d', [2.5, 3.2, 3.3])
print("Access element is: ", b[1])
print("Access element is: ", b[2])

# PYTHON OPERATORS
# Addition operator(+)
val1 = 2
val2 = 3

# using the addition operator
res = val1 + val2
print(res)

# Subtraction operator
val1 = 2
val2 = 3

# using subtraction operator
res = val1 - val2
print(res)

# Multiplication operator
val1 = 2
val2 = 3

# using the multipication operator
res = val1 * val2
print(res)

# Division operator
val1 = 3
val2 = 2

# using division operator
res = val1 / val2
print(res)

# Floor Division operator
val1 = 3
val2 = 2

# using floor divisin operator
res = val1 // val2
print(res)

# Modulus operator
val1 = 3
val2 = 2

# using the modulus operator
res = val1 % val2

# Exponentian operatoer
val1 = 2
val2 = 3

# using exponentian operator
res = val1 ** val2

# Comparison Operators
a = 9
b = 5
c = 9

# Output
print(a == b)
print(a == c)

print(a != b)
print(a != c)

print(a > b)
print(b > a)

print(a < b)
print(b < a)

print(a >= b)
print(a >= c)
print(b >= a)

print(a <= b)
print(a <= c)
print(b <= b)

# LOGICAL OPERATORS
# AND Operator
a = 10
b = 10
c = -10
if a > 0 and b > 0:
    print("The numbers are greater than 0.")
else:
    print("Atleast one number is greater than 0.")
    
a = 10
b = 12
c = 0
if a and b and c:
    print("All numbers have boolean value as True")
else:
    print("Atleast one number has boolean value as False")
    
# OR Operator
a = 10
b = -10
c = 0
if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
    
if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
    
a = 10
b = 12
c = 0
if a or b or c:
    print("All the numbers have boolean value as True")
else:
    print("Atleast one number has boolean value as False")
    
# NOT Operator
a = 10
if not a:
    print("Boolean value of a is True")
if not (a % 3 == 0 or a % 5 == 0):
    print("10 is not divisible by 3 or 5")
else:
    print("10 is divible by either 3 0r 5")
    
a = 10
b = 4

# print bitwise AND operation
print("a & b=", a & b)

a = 10
b = 4

# Print bitwise OR operation
print("a | b =", a | b)

a = 10
b = 4

# print bitwise XOR operation
print("a ^ =", a ^ b)

a = 10
b = 4

# Print bitwise NOT operation
print("~a =", a)

a = 10
b = -10

# print bitwise right shift operator
print("a >> 1 =", a >> 1)
print("b >> 1 =", b >> 1)

a = 5
b = -10

# print bitwise left operator
print("a << 1 =", a << 1)
print("b >> 1 =", b << 1)

# Python program to demonstrate operator overloading
class Geek():
    def __init__(self, value):
        self.value = value
        
    def __and__(self, obj):
        print("And operator overloaded")
        if isinstance(obj, Geek):
            return self.value & obj.value
        else:
            raise ValueError("Must be a object of class Geek")
        
    def __or__(self, obj):
        print("Or operator overloaded")
        if isinstance(obj, Geek):
            return self.value | obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __xor__(self, obj):
        print("Xor operator overloaded")
        if isinstance(obj, Geek):
            return self.value ^ obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __lshift__(self, obj):
        print("lshift operator overloaded")
        if isinstance(obj, Geek):
            return self.value << obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __rshift__(self, obj):
        print("shift operator overloaded")
        if isinstance(obj, Geek):
            return self.value >> obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __invert__(self):
        print("Invert operator overloaded")
        return ~self.value


# Driver's code
if __name__ == "__main__":
    a = Geek(10)
    b = Geek(12)
    print(a & b)
    print(a | b)
    print(a ^ b)
    print(a << b)
    print(a >> b)
    print(~a)
    
# cONDITIONAL STATEMENT
# python program to illustrate if statement
i = 10

if (i > 15):
    print("10 is less than 15")
print("I am not in if")


# Python program to illustrate else if in python statement
#!/usr/bin/python

i = 20
if (i < 15):
    print("i is smaller than 15")
    print("i'm in if block")
else:
    print("i is greater than 15")
    print("i'm in else statement")
print("i'm not in if and not in else block")

# list comprehension
# Explicit function
def digitSum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum


# Initializing list
List = [367, 111, 562, 945, 6726, 873]

# Using the function on odd elements of the list
newList = [digitSum(i) for i in List if i & 1]

# Displaying new list
print(newList)

# Python program to illustrate nested if statement
i = 10
if (i == 10):
    
    # First if statement
    if (i < 15):
        print("i is smaller than 15")
        
    # Nested - if statement will only be excuted if statement above it is true
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
        
        
# Python program to illustrate if-elif-else ladder
#!/usr/bin/python

i = 25
if (i == 10):
    print("is is 10")
elif (1 == 15):
    print("i is 15")
elif (i == 20):
    print("i is 20")
else:
    print("i is nor present")
    
# Python code to demonstrate the syntax of if statement

gfg = 9

# If statement with true condition
if gfg < 10:
    print(f"{gfg} is less than 10")

# If statement with with false condition
if gfg > 20:
    print(f"{gfg} is greater than 20")
    
# Python program to demonstrate nested if with multiple if statements
i = -15

# conditin 1
if i != 0:
    # condition 2
    if i > 0:
        print("positive")
    # condition 3
    if i < 0:
        print("negative")

i = 0

# if condition 1
if i != 0:
    # condition 1
    if i > 0:
        print("Positive")
    
    # condition 2
    if i < 0:
        print("Negative")
else:
    print("Zero")
    
# FOR LOOPS

# Iterating over a string
print("String Iteration")

s = "Geeks"
for i in s:
    print(i)

# Range() in for loop
for i in range(0, 10, 2):
    print(i)

# for loop Enumerate
l1 = ["eat", "sleep", "repeat"]

for count, ele in enumerate(l1):
    print(count, ele)
    
# Nested For Loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
        
# for loop in one line
Numbers = [x for x in range(11)]
print(Numbers)

# for loop with Dictionary
# iterating over a dictionary
print("Dictionary Iteration")

d = dict()

d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("% s % d" % (i, d[i]))

# Control Statements with For Loop
# continue for loop
# prints all letters except 'e' and 's'
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)

# break in for loop
for letter in 'geeksforgeeks':
    
    # break the loop as soon it sees 'e' or 's'
    if letter == 'e' or letter == 's':
        break
    print('Current Letter :', letter)

# pass statement in for loop
# An empt loop
for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)

# Pthon program to demonstrate for-else loop
for i in range(1, 4):
    print(i)
else:
    print("NO BREAK\n")
    
# For Loop Exercise
# Cotinue statement in for-loop
clothes = ["shirt", "sock", "pants", "sock", "towel"]
paired_socks = []
for item in clothes:
    if item == "sock":
        continue
    else:
        print(f"Washing {item}")
paired_socks.append("socks")
print(f"Washing {paired_socks}")

# range() function in for-loop
for day in range(1, 8):
    distance = 3 + (day - 1) * 0.5
    print(f"Day {day}: Run {distance:.1f} miles")
    
# WHILE LOOP
# python code to illustrate while loop
count = 0
while (count < 3):
    count = count + 1
    print("Hello Greek")
    
age = 28

# the test condition is always true
while age > 19:
    print('Ininite Loop')
    
# while loop with continue statement
# Prints all letters except 'a' and 's'
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
    
    print('current Letter :', a[i])
    i += 1
    
# while loop with break statement
# break the loop s soon it sees 'e' or 's'
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break
    
    print('current letter: ', a[i])
    i += 1
    
# while loop with pass statement
# An empty loop
a = 'geeksforgeeks'
i = 0

while i < len(a):
    i += 1
    pass

print('Value of i :', i)

# python program to demonstrate while-else loop
i = 0
while i < 4:
    i += 1
    print(i)
else: # Executed because no break
    print("No Break\n")
    
i = 0
while i < 4:
    i += 1
    print(i)
    break 
else: # Not executed as there is a break
    print("No Break")
    
# checks if list still contains any element
a = [1, 2, 3, 4]

while a:
    print(a.pop())
    
# Python program to illustrate single statement while block
count = 0
while (count < 5):
    count += 1
    print("Hello Geek")
    
initial_height = 10
bounce_factor = 0.5
height = initial_height
while height > 0.1:
    print("The ball is at a height of ", height, "meters.")
    height *= bounce_factor
print("The ball has stopped bouncing")

countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off!")

# BREAK, CONTINUE, PASS
# python program to demonstrete break statement
s = 'geeksforgeeks'

# Using for loop
for letter in s:
    print(letter)
    
    # break the loop it sees 'e' or 's'
    if letter == 'e' or letter == 's':
        break

print("Out of for loop")
print()

i = 0

# Using while loop
while True:
    print(s[i])
    
    # break the loop as soon it seees 'e' or 's'
    if s[i] == 'e' or s[i] == 's':
        break
    i += 1
    
print("Out of while loop")

# Python program to demonstrate break statement with nested for loop
# first for loop
for i in range(1, 5):
    
    # second for loop
    for j in range(2, 6):
        
        # break the loop if j is divisible by i
        if j%i == 0:
            break
        
        print(i, " ", j)

# Python program to demonstrate continue statement
# Loop from 1 to 5
for i in range(1, 11):
    
    #If i is equals to 6, continue to next iteration without printing
    if i == 6:
        continue
    else:
        # otherwise print the value of i
        print(i, end=" ")
        
# Python program to demonstrate pass statement
s = "geeks"

# Empty loop
for i in s:
    # No error will be raised
    pass

# Empty function
def fun():
    pass

#No error will be raised
fun()

# Pass statement
for i in s:
    if i == 'k':
        print('Pass executed')
        pass
    print(i)