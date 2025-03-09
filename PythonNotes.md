# Python Fundamentals Guide

## Index
- **Beginner Topics**
  1. [Basic Syntax](#1-basic-syntax--data-types)
  2. [Control Flow](#2-control-flow)
  3. [Functions](#3-functions)
  4. [Error Handling](#4-error-handling)
  5. [File IO](#5-file-io)
  6. [Modules/Packages](#6-modulespackages)

- **Intermediate Topics**
  7. [OOP](#7-object-oriented-programming-oop)
  8. [Advanced Data Structures](#8-advanced-data-structures)
  9. [Decorators](#9-decorators)
  10. [Generators](#10-generators)
  11. [Functional Programming](#11-functional-programming)
  12. [Context Managers](#12-context-managers)
  13. [Testing](#13-testing)
  14. [Concurrency](#14-concurrency)

---

### 1. Basic Syntax & Data Types
```python
# Variables and basic data types
name = "Alice"          # String
age = 30                # Integer
height = 5.9            # Float
is_student = False      # Boolean
fruits = ["apple", "banana"]  # List
person = {"name": "Bob"}      # Dictionary

print(f"{name} is {age} years old.")  # f-strings for formatting
```

---

### 2. Control Flow
```python
# If-else and loops
num = 10

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

for fruit in fruits:
    print(fruit)

count = 0
while count < 3:
    print(count)
    count += 1
```

---

### 3. Functions
```python
def add(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

---

### 4. Error Handling
```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution complete.")
```

---

### 5. File I/O
```python
with open("demo.txt", "w") as file:
    file.write("Hello, World!")

with open("demo.txt", "r") as file:
    content = file.read()
    print(content)  # Output: Hello, World!
```

---

### 6. Modules/Packages
```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"

# main.py
import my_module
print(my_module.greet("Alice"))  # Output: Hello, Alice!
```

---

### 7. Object-Oriented Programming (OOP)
```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "Generic sound"

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

dog = Dog("Buddy")
print(dog.speak())  # Output: Woof!
```

---

### 8. Advanced Data Structures
```python
from collections import namedtuple, defaultdict

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x)  # Output: 10

word_counts = defaultdict(int)
words = ["apple", "apple", "banana"]
for word in words:
    word_counts[word] += 1
print(word_counts)  # Output: defaultdict(<class 'int'>, {'apple': 2, 'banana': 1})
```

---

### 9. Decorators
```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Calling greet → Hello, Alice!
```

---

### 10. Generators
```python
def count_up_to(n: int):
    count = 1
    while count <= n:
        yield count
        count += 1

counter = count_up_to(3)
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
```

---

### 11. Functional Programming
```python
numbers = [1, 2, 3, 4]

squared = list(map(lambda x: x ** 2, numbers))  # [1, 4, 9, 16]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

print(squared, evens)
```

---

### 12. Context Managers
```python
import time

class Timer:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        print(f"Elapsed: {time.time() - self.start:.2f}s")

with Timer():
    time.sleep(1)  # Output: Elapsed: 1.00s
```

---

### 13. Testing
```python
def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
```

---

### 14. Concurrency
```python
import threading

def print_numbers():
    for i in range(3):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()  # Output: 0 1 2
```

---
