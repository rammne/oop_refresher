# Abstract Classes

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     def __init__(self, color):
#         # Initialize the color property
        
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, color, length, width):
#         # Call the parent constructor and initialize the length and width properties

#     def area(self):
#         # Calculate and return the area of the rectangle

#     def perimeter(self):
#         # Calculate and return the perimeter of the rectangle

# class Circle(Shape):
#     def __init__(self, color, radius):
#         # Call the parent constructor and initialize the radius property

#     def area(self):
#         # Calculate and return the area of the circle

#     def perimeter(self):
#         # Calculate and return the perimeter of the circle


# # Test your implementation
# rectangle1 = Rectangle("red", 4, 5)
# print(rectangle1.area())  # Should output 20
# print(rectangle1.perimeter())  # Should output 18

# circle1 = Circle("blue", 3)
# print(circle1.area())  # Should output approximately 28.274333882308138
# print(circle1.perimeter())  # Should output approximately 18.84955592153876

# ANSWER

# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     def __init__(self, color):
#         self.color = color

#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, color, length, width):
#         super().__init__(color)
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return (self.length + self.width) * 2

# class Circle(Shape):
#     def __init__(self, color, radius):
#         super().__init__(color)
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

#     def perimeter(self):
#         return 2 * math.pi * self.radius


# # Test your implementation
# rectangle1 = Rectangle("red", 4, 5)
# print(rectangle1.area())  # Should output 20
# print(rectangle1.perimeter())  # Should output 18

# circle1 = Circle("blue", 3)
# print(circle1.area())  # Should output approximately 28.274333882308138
# print(circle1.perimeter())  # Should output approximately 18.84955592153876
