#A list is a collection of items in a particular order
#A list is indicated using square brackects []

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Accessing elements in a list
bicycles = ['trek', 'cannondale', 'redline', 'spcialized']
print(bicycles[0])

#Index position starts from zero
bicycles = ['trek', 'cannondale', 'redline', 'spcialized']
print(bicycles[1])
print(bicycles[3])

#Use individual values from a list
bicycles = ['trek', 'cannondale', 'redline', 'spcialized']
message = "My first bicycle was " + bicycles[0].title() + "."
print(message)