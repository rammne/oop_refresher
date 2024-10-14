from abc import ABC, abstractmethod
# Define an abstract class 'Shape'
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
    
    def description(self):
        print(f"{self.__class__.__name__} has the color: {self.color}")

# Define a concrete class 'Rectangle' that
# inherits from 'Shape'
class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    
# Create instances of concrete classes and use
# their methods
rectangle = Rectangle(4, 5, "red")
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")
print(f"Rectangle color: {rectangle.color}")
rectangle.description()
