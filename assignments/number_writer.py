#Storing data
#Storing data using json
#JSON(Javascript Object Notation)
#Using json.dump() and json.load()
import json

numbers = [2, 3, 5, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)