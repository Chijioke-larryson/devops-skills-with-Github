def add(a, b):
    """Add two numbers"""
    return a + b


def sub(a, b):
    """Subtract two numbers"""
    return a - b


def mul(a, b):
    """Multiply two numbers"""
    return a * b


def div(a, b):
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
    
    def sub(self, a, b):
        return sub(a, b)
    
    def mul(self, a, b):
        return mul(a, b)
    
    def div(self, a, b):
        return div(a, b)
    
    def mod(self, a, b):
        return mod(a, b)
    
    def pow(self, a, b):
        return pow(a, b)
