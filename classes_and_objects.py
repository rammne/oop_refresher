# Define the Greeting class
class Greeting:
    # Constructor for the Greeting class
    def __init__(self, name):
        # Initialize 'name' with the provided value
        self.name = name
        
    # Define our greeting method
    def say_hello(self):
    # Print a personalized greeting message
    # using the 'name' attribute
        print(f"Hello, {self.name}!")

# Create an object of the Greeting class,
# initializing it with the name 'John'
greeting = Greeting("John")
# Call the 'say_hello' method on the 'greeting'
# object to print the greeting message
greeting.say_hello()