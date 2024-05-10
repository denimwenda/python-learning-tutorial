message = 'Hello World'

print(message)

print(len(message))

print(message[5])

print(message[0:5])

print(message[:5])

print(message[4:])

# print lower method
print(message.lower())

# print upper method.
print(message.upper())

# count method
print(message.count('World'))

# replace method
new_message = message.replace('World', 'Universe')
print(new_message)

greeting = 'Hello'
name = 'Macheal'

message = greeting + ', ' + name + '. Welcome!'
print(message)



# Integer and float
# Arithmetic Operators:
# Addition +
# Subtraction -
# Multiplication *
# Division /
# Floor Division //
# Exponent **
# Modulus

# Comparisons:
# Equal ==
# Not Equal !=
# Greater Than >
# Less Than <
# Greater or Equal >=
# Less or Equal <=

num_1 = 3
num_2 = 3

print(num_1 == num_2)

num_3 = 3
num_4 = 2

print(num_3 > num_4)


# Casting
num_5 = '100'
num_6 = '200'

num_5 = int(num_5)
num_6 = int(num_6)

print(num_6 + num_5)


# Working with list
# list is created using square brackects []
# Slicing
courses = ['History', 'Math', 'physics', 'CompSci']
print(courses[2:])

# Modifying List
courses = ['History', 'Math', 'physics', 'CompSci']
courses_2 = ['Art', 'Education']

courses.append(courses_2)
print(courses)

courses.extend(courses_2)
print(courses)

# Remove
courses = ['History', 'Math', 'physics', 'CompSci']

courses.remove('Math')

print(courses)

courses.pop()
print(courses)

# Sorting list
courses = ['History', 'Math', 'physics', 'CompSci']
nums = [1, 4, 2, 5, 3]

courses.sort()
nums.sort()

print(courses)
print(nums)

nums = [1, 4, 2, 5, 3]

print(max(nums))
print(min(nums))
print(sum(nums))

# Looping through values
courses = ['History', 'Math', 'physics', 'CompSci']

for course in courses:
    print(course)

for index, course in enumerate(courses):
    print(index, course)

course_str = ', '.join(courses)

print(course_str)

# Tuples
# Mutable
list_1 = ['History', 'Math', 'physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

# Sets
cs_courses = {'History', 'Math', 'physics', 'CompSci'}

print(cs_courses)

cs_courses = {'History', 'Math', 'physics', 'CompSci'}
art_courses = {'Math', 'History', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))


# Dictionaries
student = {'name': 'john', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student['courses'])

student = {'name': 'john', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student.get('phone', 'Not Found'))

student = {'name': 'john', 'age': 25, 'courses': ['Math', 'CompSci']}

student['phone'] = '555-5555'
student['name'] = 'jane'

student = {'name': 'john', 'age': 25, 'courses': ['Math', 'CompSci']}

del student['age']

print(student)

student = {'name': 'john', 'age': 25, 'courses': ['Math', 'CompSci']}

print(len(student))

student = {'name': 'john', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student.keys())

student = {'name': 'john', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student.values())

student = {'name': 'john', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student.items())

student = {'name': 'john', 'age': 25, 'courses': ['Math', 'CompSci']}

for key, value in student.items():
    print(key, value)


# Conditionals
language = 'Python'

if language == 'Python':
    print('language is Pthon')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match')


user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad Creds')

if not logged_in:
    print('log in')
else:
    print('Welcome')


condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evacuated to False')