# imports needed for abstract classes
from abc import ABC, abstractmethod
# interface contract. Children will have to
# implement all of the abstract methods.
# Methods have no implementations: use ‘pass’
class MyInterface(ABC):
    @abstractmethod
    def my_method(self):
        pass


class MyClass(MyInterface):
    def my_method(self):
        print("my_method implementation in MyClass")


class NotImplementingInterface:
    def some_method(self):
        print("I am not implementing MyInterface")


# This method expects to be passed an object that
# implements the MyInterface methods.
def process_my_interface(obj: MyInterface):
    obj.my_method()
    print("Correct implementation of MyInterface")

    
my_obj = MyClass()
process_my_interface(my_obj)
bad_interface = NotImplementingInterface()
process_my_interface(bad_interface)
