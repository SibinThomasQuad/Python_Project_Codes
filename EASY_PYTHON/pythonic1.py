# README_Examples.py

# Lambda Functions
square = lambda x: x ** 2
print("Lambda Function Example:", square(5))

# List Comprehensions
squares = [x**2 for x in range(1, 6)]
print("List Comprehension Example:", squares)

# Generators and Generator Expressions
def square_generator(n):
    for i in range(n):
        yield i**2

gen = square_generator(5)
print("Generator Example:", list(gen))

# Decorators
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

print("Decorator Example:")
result = add(3, 5)

# Context Managers
with open('file.txt', 'r') as file:
    data = file.read()

# Destructuring Assignment
a, b, c = (1, 2, 3)
print("Destructuring Assignment Example:", a, b, c)

# Namedtuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print("Namedtuple Example:", p)

# Set and Dictionary Comprehensions
unique_characters = {char for char in 'hello'}
squared_dict = {x: x**2 for x in range(1, 6)}
print("Set Comprehension Example:", unique_characters)
print("Dictionary Comprehension Example:", squared_dict)

# Contextlib Module
from contextlib import contextmanager

@contextmanager
def custom_context_manager():
    print("Entering the context")
    yield
    print("Exiting the context")

with custom_context_manager():
    print("Inside the context")

# Regular Expressions (re module)
import re

text = "Sample text with 10-10-2023 date and 12-05-2024 date."
matches = re.findall(r'\d{2}-\d{2}-\d{4}', text)
print("Regular Expressions Example:", matches)

# Defaultdict and Counter (collections module)
from collections import defaultdict, Counter

d = defaultdict(int)
c = Counter([1, 2, 2, 3, 3, 3, 4])
print("Defaultdict Example:", d)
print("Counter Example:", c)

# F-strings (Python 3.6+)
name = 'Alice'
age = 30
message = f"Hello, my name is {name} and I am {age} years old."
print("F-string Example:", message)
