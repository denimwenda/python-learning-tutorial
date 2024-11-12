# Object Oriented Programing(OOP)
# creating a class
class Dog:
    sound = "bark"
    
# python program to demonstrate instantiating a class
class Dog:
    # A simple class attribute
    attr1 = "mammal"
    attr2 = "dog"
    
    # A sample fault
    def fun(self):
        print("I,m a", self.attr1)
        print("i,m a", self.attr2)
        
# Driver code object instantiation
Rodger = Dog()

# A ccessing class attributes and method through objects
print(Rodger.attr1)
Rodger.fun()

class GFG:
    def __init__(self, name, company):
        self.name = name
        self.company = company
        
    def show(self):
        print("Hello my name is " + self.name+" and i" + " work in "+self.company)
        
obj = GFG("John", "GeeksForGeeks")
obj.show()

class CFG:
    def __init__(somename, name, company):
        somename.name = name
        somename.company = company
        
        def show(somename):
            print("Hello my name is " + somename.name+" and i" + " work in "+somename.company)
        
obj = CFG("John", "GeeksForGeeks")
obj.show()

# A sample class with init method
class Person:
    
    # init method or constructor
    def __init__(self, name):
        self.name = name
        
    # Sample method
    def say_hi(self):
        print('Hello, m name is', self.name)
        
p = Person('Dennis')
p.say_hi()
