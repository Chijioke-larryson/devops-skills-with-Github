def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract two numbers"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def mod(a, b):
    """Get modulo of two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b


def pow(a, b):
    """Raise a to the power of b"""
    return a ** b


class Calculator:
    """Simple calculator class with basic operations"""
    
    def __init__(self):
        pass
    
    def add(self, a, b):
        return add(a, b)
    
    def subtract(self, a, b):
        return subtract(a, b)
    
    def multiply(self, a, b):
        return multiply(a, b)
    
    def divide(self, a, b):
        return divide(a, b)
    
    def mod(self, a, b):
        return mod(a, b)
    
    def pow(self, a, b):
        return pow(a, b)
