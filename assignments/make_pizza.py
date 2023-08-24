import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Importing specific functions
#from module_nmae import function_name
#from module_name import function_0, function_1, function_2
#Using as to give a function an Alias
#Importing make_pizza as mp
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

#The general syntax for providng an alias is:
#from module_name import function_name as fn

#Using as to give a module an alias
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#The general syntax for giving module an alais is:
#import module_name as nm

#Importing All Functions in a Module
#We import every function in a module using asterisk (*) operator
#from module_nae import *
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Styling functions
#should have descriptive names and should be lowwercase and underscores
#Functions should have a comment explaining what the function is doing
#this comment should appear immediately after the function and should use docstring format
#If you specify a default value for a parameter, no space should be o either side of the equal sign
#def function_name(parameter_0, parameter_1='default value')
