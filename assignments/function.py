# creating a function
# A simple python function
def fun():
    print("welcome to GFG")
    
# callin a function
def fun():
    print("Welcome to GFG")

# Driver code to call a function
fun()

# python function with parameters
def add(num1: int , num2: int):
    """Add two numbers"""
    num3 = num1 + num2
    
    return num3

# Driver code
num1 , num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

# some more functions
def is_prime(n):
    if n in [2, 3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True
print(is_prime(78), is_prime(79))

# A simple python function to check whether x is even or odd
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
        
# Driver code to call the function
evenOdd(2)
evenOdd(3)

# python program to demonstrate default arguments
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
    
# Driver code (We call myFun() with only argument)
myFun(10)

# python program to demonstrate keyword arguments
def student(firstname, lastname):
    print(firstname, lastname)
    
# Keywords arguments
student(firstname='Geeks', lastname='Practice')
student(firstname='Practice', lastname='Geeks')

# positional arguments
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is", age)
    
# You will get correct output because argument is given in order
print("Case-1:")
nameAge("Suraj", 27)
# You will get incorrect output because argument is not in order
print("\nCase-2:")
nameAge(27, "Suraj")

# python program to illustrate *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)
        
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
    
# Python program to illustrate
# *kwargs for variable number of keyword arguments


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

# A simple Python function to check
# whether x is even or odd


def evenOdd(x):
    """Function to check if the number is even or odd"""
    
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")


# Driver code to call the function
print(evenOdd.__doc__)

# Python program to
# demonstrate accessing of
# variables of nested functions

def f1():
    s = 'I love GeeksforGeeks'
    
    def f2():
        print(s)
        
    f2()

# Driver's code
f1()

# Python code to illustrate the cube of a number
# using lambda function
def cube(x): return x*x*x

cube_v2 = lambda x : x*x*x

print(cube(7))
print(cube_v2(7))

def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))

def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2


print(square_value(2))
print(square_value(-4))

# Here x is a new reference to same list lst
def myFun(x):
    x[0] = 20


# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)

def myFun(x):

    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = [20, 30, 40]


# Driver Code (Note that lst is not modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)

def myFun(x):

    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = 20


# Driver Code (Note that x is not modified
# after function call.
x = 10
myFun(x)
print(x)

def swap(x, y):
    temp = x
    x = y
    y = temp

# Driver code
x = 2
y = 3
swap(x, y)
print(x)
print(y)

# python program to illustrate nested functions
def outerFunction(text):
    
    def innerFunction():
        print(text)
        
    innerFunction()
    

if __name__ == '__name__':
    outerFunction('Hey!')
    
# python program to illustrate closures
def outerFunction(text):
    
    def innerFunction():
        print(text)
        
    # Note we are returning function without parenthesis
    return innerFunction

if __name__ == '__main__':
    myFunction = outerFunction('Hey!')
    myFunction()
    
# Python program to illustrate closures 
import logging 
logging.basicConfig(filename='example.log',
                    level=logging.INFO) 
 
def logger(func): 
    def log_func(*args): 
        logging.info( 
            'Running "{}" with arguments {}'.format(func.__name__,
                                                    args)) 
        print(func(*args)) 
         
    # Necessary for closure to work (returning WITHOUT parenthesis) 
    return log_func             
 
def add(x, y): 
    return x+y 
 
def sub(x, y): 
    return x-y 
 
add_logger = logger(add) 
sub_logger = logger(sub)

add_logger(3, 3) 
add_logger(4, 5) 
 
sub_logger(10, 5) 
sub_logger(20, 10)

class GeeksforGeeks:
    def __init__(self, topic):
        self.topic = topic

    def display_topic(self):
        print("&quot;Topic:&quot;, self.topic")

# Creating an instance of GeeksforGeeks
gfg_instance = GeeksforGeeks("&quot;Python&quot;")

# Calling the display_topic method
gfg_instance.display_topic()

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * self.radius ** 2
        return area

# Creating an instance of Circle
circle_instance = Circle(5)

# Calling the calculate_area method
print("&quot;Area of the circle:&quot;, circle_instance.calculate_area()")

# python program to illustrate functions can be treated as objects
def shout(text):
    return text.upper()

print(shout('Hello'))

yell = shout

print(yell('Hello'))

# python program to illustrate functions can be passed as arguments to other functions
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a funtion passed as an argument.""")
    print(greeting)
    
greet(shout)
greet(whisper)

# Python program to illustrate functions Functions can return another function 

def create_adder(x): 
    def adder(y): 
        return x+y 

    return adder 

add_15 = create_adder(15) 

print(add_15(10)) 

# defining a decorator
def hello_decorator(func):

    # inner1 is a Wrapper function in 
    # which the argument is called
    
    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")
        
    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)


# calling the function
function_to_be_used()

# importing libraries
import time
import math

# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):

        # storing time before function execution
        begin = time.time()
        
        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1



# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):

    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))

# calling the function.
factorial(10)

def hello_decorator(func):
    def inner1(*args, **kwargs):
        
        print("before Execution")
        
        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")
        
        # returning the value to the original frame
        return returned_value
        
    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b

a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))

# code for testing decorator chaining 
def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 

def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 

@decor1
@decor
def num(): 
    return 10

@decor
@decor1
def num2():
    return 10
  
print(num()) 
print(num2())

# using map() function to convert a list of strings into a list of integers
s = ['1', '2', '3', '4']
res = map(int, s)
print(list(res))

a = [1, 2, 3, 4]

# Using custom function in "function" parameter
# This function is simply doubles the provided number
def double(val):
  return val*2

res = list(map(double, a))
print(res)

a = [1, 2, 3, 4]

# Using lambda function in "function" parameter
# to double each number in the list
res = list(map(lambda x: x * 2, a))
print(res)

a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)
print(list(res))

# map() to convert a list of strings to uppercase
fruits = ['apple', 'banana', 'cherry']
res = map(str.upper, fruits)
print(list(res))
