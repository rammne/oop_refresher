# Base (parent) class
class Animal:
 def __init__(self, name):
    self.name = name
 def speak(self):
    print(f"{self.name} makes a sound.")
    
# Derived (child) class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

# Derived (child) class
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

        
# Create objects of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
# Call the 'speak' method on the derived class objects
dog.speak()
cat.speak()
