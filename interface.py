# imports needed for abstract classes
from abc import ABC, abstractmethod
# interface contract. Children will have to implement
# all of the abstract methods. In an interface methods
# have no implementations so we use ‘pass’
class MyInterface(ABC):
    @abstractmethod
    def my_method(self):
        pass

class MyClass(MyInterface):
    def my_method(self):
        print("my_method implementation in MyClass")

class AnotherClass(MyInterface):
    def my_method(self):
        print("my_method implementation in AnotherClass")


my_obj = MyClass()
my_obj.my_method()
another_obj = AnotherClass()
another_obj.my_method()