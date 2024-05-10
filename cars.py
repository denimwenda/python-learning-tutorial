cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

#sorting a list temporarily with sorted() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#printing a list in the reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)

#seeing the world tutorial
locations = ['masai mara', 'tanzania', 'bogoria', 'tsavo', 'amboseli']
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)
print(locations)
locations.sort()
print(locations)

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())