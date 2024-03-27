#CLASSES
#OOP object-oriented programming is one of the most effective approches of writing software
#In object-oriented programming you write classes which represent real-world things and situations

#Creating and Using a Class
#Creating a dog class
class Dog():
    """A simple attempt to model a dog"""
    def __int__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title() + " roll_over!")