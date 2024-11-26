amount = 10000
if(amount > 2999):
    print("You eligible to purchase Dsa Self Paced.")

marks = 10000
a = marks / 2
print(a)

x = 5
y = "hello"
try:
    z = x + y
except TypeError:
    print("Error: cannot add an int and a string")
    
a = [1, 2, 3]
try:
    print("Second element = %d" %(a[1]))
    print("Fourth element = %d" %(a[3]))
except:
    print("An error occurred")
    
def fun(a):
    if a < 4:
        
        b = a/(a-3)
    print("Value of b = ", b)
    
try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError occurred and handled")
except NameError:
    print("NameError occurred and Handled")
    
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

try:
    k = 5//0
    print(k)
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    print('This is always executed')
    
try:
    raise NameError("Hi there")
except NameError:
    print("An exception")
    raise

# Open function to open the file "MyFile1.txt" 
# (same directory) in read mode and 
file1 = open("MyFile.txt", "r") 

# store its reference in the variable file1 
# and "MyFile2.txt" in D:\Text in file2 
file2 = open(r"D:\Text\MyFile2.txt", "r+") 

# Opening and Closing a file "MyFile.txt" 
# for object name file1. 
file1 = open("MyFile.txt", "r") 
file1.close() 

# Program to show various ways to 
# read data from a file. 

# Creating a file
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Writing data to a file
file1.write("Hello \n") 
file1.writelines(L)
file1.close() # to change file access modes

file1 = open("myfile.txt", "r+")

print("Output of Read function is ")
print(file1.read())
print()

# seek(n) takes the file handle to the nth
# byte from the beginning. 
file1.seek(0)

print("Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0)

# To show difference between read and readline 
print("Output of Read(9) function is ")
print(file1.read(9))
print()

file1.seek(0)

print("Output of Readline(9) function is ")
print(file1.readline(9))
print()

file1.seek(0)

# readlines function 
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close() 
