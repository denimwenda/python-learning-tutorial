motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#adding element to a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

#inserting elements into a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

#removing elements from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

#removing an element using pop() method
motorcycles =['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle i owned was a " + last_owned.title() + ".")

#popping items from any position of the list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first car i owned was a " + first_owned.title() + ".")

#removing an item
motorcycles = ['honda', 'yamaha', 'suzui', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

friends = ['dan', 'rein', 'xaas']
first = 'dan'
second = 'rein'
third = 'xaas'
print("\n " + first.title() + " you are welcomwed for dinner.")
print("\n " + second.title() + " you are welcomed for the party")
print("\n " + third.title() + " you are welcomed for the party")

friends = ['dan', 'rein', 'xaas']
print(friends)
friends.insert(1, 'felix')
print(friends)
friends.append('toe')
print(friends)

#avoiding index errrors working with list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])

birds = ['hen', 'dove', 'pigeon', 'turkey']
print(birds)
print(birds[2])
print(birds[-2])
print(birds[0])
print(birds[3])