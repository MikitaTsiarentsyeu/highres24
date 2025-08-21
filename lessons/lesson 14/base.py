from abc import ABC, abstractmethod

class Stack(ABC):
    
    def __init__(self):
        # Consider attrs required for a stack, modify the args list if needed
        pass

    @abstractmethod
    def is_empty(self):
        # Returns True if the stack is empty, False otherwise
        pass

    @abstractmethod
    def push(self, item):
        # Pushes an item onto the top of the stack
        pass

    @abstractmethod
    def pop(self):
        # Removes and returns the item from the top of the stack
        # Raises an exception if the stack is empty
        pass

    @abstractmethod
    def peek(self):
        # Returns the item from the top of the stack without removing it
        # Raises an exception if the stack is empty
        pass