#tuple is reffered to as immutable because values cannot change
#in tuple we use parentheses()
#a rectangle of a certain size
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#attempt to change the above tuple
dimensions = (200, 50)
dimensions[0]

#looping through all values in a list
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#writing over a tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

buffets = ('Pilau', 'Chips', 'Githeri', 'Rice', 'Meat')
print("We offer the following foods:")
for buffet in buffets:
    print(buffet)

buffets = ('Pilau', 'Chips', 'Githeri', 'Rice', 'Meat')
buffets[1] = 'cake'
print(buffets)