#working with a part of a list
#slicing a list
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[0:3])

players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[1:4])

players =['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[:4])

players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[2:])

players =['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[-3:])

#looping through a slice
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print("Here are the first three players in my list:")
for player in players[:3]:
    print(player.title())
