# for loop
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

for num in nums:
    for letter in 'abc':
        print(num, letter)

for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)


#while loop
x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1


# Creating functions
def hello_func():
    print('Hello Function!')

hello_func()
hello_func()
hello_func()
hello_func()

def hello_func():
    return 'Hello Fuction.'

print(hello_func().upper())

def hello_func(greeting, name):
    return '{}, {}'.format(greeting, name)

print(hello_func('Hi', name = 'Dennis'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='john', age=22)


# Month Days
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False foe none leap years"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of das in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid month'
    
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

print(days_in_month(2017, 2))