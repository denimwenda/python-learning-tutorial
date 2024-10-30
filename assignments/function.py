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