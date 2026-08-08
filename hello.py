#!/usr/bin/env python3



def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b



if __name__ == "__main__":
    print("Addition:", add(5, 3))
    print("Subtraction:", sub(5, 3))
    print("Multiplication:", mul(5, 3))
    print("Division:", div(5, 3))