# UNIT 2 — PYTHON DATA STRUCTURES AND FUNCTIONS

This unit is a self-contained knowledge base chapter covering strings, lists, tuples, sets, dictionaries, comprehensions, and functions. Each section is independently retrievable.

---

## 1. Strings

A string (`str`) is an **immutable** sequence of characters, enclosed in single, double, or triple quotes.

```python
s1 = 'Hello'
s2 = "World"
s3 = """Multi
line"""
print(s1, s2)
print(s3)
```
**Output:**
```
Hello World
Multi
line
```

**Immutability:** once a string is created, it cannot be changed in place. Any "modification" creates a new string object.

```python
s = "Python"
# s[0] = "J"   # This raises TypeError: 'str' object does not support item assignment
s = "J" + s[1:]
print(s)
```
**Output:**
```
Jython
```

---

## 2. String Indexing

Each character has a position (index), starting at `0` from the left and `-1` from the right.

```python
word = "Python"
print(word[0])    # first character
print(word[5])    # last character
print(word[-1])   # last character using negative indexing
print(word[-6])   # first character using negative indexing
```
**Output:**
```
P
n
n
P
```

**Common mistake:** `word[6]` raises `IndexError: string index out of range` since valid indices for a 6-character string are 0–5.

---

## 3. String Slicing

Syntax: `string[start:stop:step]` — `start` is inclusive, `stop` is exclusive.

```python
word = "Programming"
print(word[0:6])    # 'Progra'
print(word[:4])     # 'Prog'
print(word[4:])     # 'ramming'
print(word[::-1])   # reversed string
print(word[::2])    # every 2nd character
```
**Output:**
```
Progra
Prog
ramming
gnimmargorP
Pormig
```

---

## 4. String Methods

```python
text = "  Hello Python World  "
print(text.strip())
print(text.strip().upper())
print(text.strip().lower())
print(text.strip().replace("Python", "Java"))
print(text.strip().split())
print("-".join(["a", "b", "c"]))
print(text.strip().startswith("Hello"))
print(text.strip().endswith("World"))
print(text.count("o"))
print(text.strip().find("Python"))
```
**Output:**
```
Hello Python World
HELLO PYTHON WORLD
hello python world
Hello Java World
['Hello', 'Python', 'World']
a-b-c
True
True
2
6
```

| Method | Purpose |
|---|---|
| `.strip()` | Remove leading/trailing whitespace |
| `.upper()` / `.lower()` | Change case |
| `.replace(old, new)` | Replace substring |
| `.split(sep)` | Split into a list |
| `.join(iterable)` | Join list into a string |
| `.find(sub)` | Return index of substring or -1 |
| `.count(sub)` | Count occurrences |
| `.startswith()` / `.endswith()` | Boolean check |

---

## 5. String Formatting

Three main ways to format strings:

```python
name, age = "Asha", 22

# 1. % formatting (old style)
print("%s is %d years old" % (name, age))

# 2. .format()
print("{} is {} years old".format(name, age))

# 3. f-strings (modern, preferred)
print(f"{name} is {age} years old")
```
**Output:**
```
Asha is 22 years old
Asha is 22 years old
Asha is 22 years old
```

---

## 6. f-strings

Introduced in Python 3.6, f-strings allow embedding expressions directly inside string literals using `{}`.

```python
price = 499.5
qty = 3
print(f"Total: {price * qty}")
print(f"Total: {price * qty:.2f}")   # 2 decimal places
print(f"{price=}")                    # debugging shortcut, shows variable name and value
```
**Output:**
```
Total: 1498.5
Total: 1498.50
price=499.5
```

**Best practice:** Prefer f-strings over `%` or `.format()` for readability and performance.

---

## 7. Lists

A `list` is an **ordered, mutable** collection that can hold mixed data types.

```python
fruits = ["apple", "banana", "cherry"]
mixed = [1, "two", 3.0, True]
print(fruits)
print(mixed)
print(type(fruits))
```
**Output:**
```
['apple', 'banana', 'cherry']
[1, 'two', 3.0, True]
<class 'list'>
```

---

## 8. List Indexing

Same indexing rules as strings.

```python
nums = [10, 20, 30, 40, 50]
print(nums[0])
print(nums[-1])
nums[1] = 99   # lists are mutable — this is allowed
print(nums)
```
**Output:**
```
10
50
[10, 99, 30, 40, 50]
```

---

## 9. List Slicing

```python
nums = [10, 20, 30, 40, 50, 60]
print(nums[1:4])
print(nums[:3])
print(nums[::2])
print(nums[::-1])
nums[1:3] = [200, 300]   # replace a slice
print(nums)
```
**Output:**
```
[20, 30, 40]
[10, 20, 30]
[10, 30, 50]
[60, 50, 40, 30, 20, 10]
[10, 200, 300, 40, 50, 60]
```

---

## 10. List Methods

```python
nums = [3, 1, 4, 1, 5]
nums.append(9)
print(nums)
nums.insert(0, 100)
print(nums)
nums.remove(1)          # removes first occurrence of value 1
print(nums)
popped = nums.pop()     # removes and returns last item
print(popped, nums)
nums.sort()
print(nums)
nums.reverse()
print(nums)
print(nums.count(1))
print(len(nums))
nums.extend([7, 8])
print(nums)
```
**Output:**
```
[3, 1, 4, 1, 5, 9]
[100, 3, 1, 4, 1, 5, 9]
[100, 3, 4, 1, 5, 9]
9 [100, 3, 4, 1, 5]
[1, 3, 4, 5, 100]
[100, 5, 4, 3, 1]
1
5
[100, 5, 4, 3, 1, 7, 8]
```

**Common mistake:** Confusing `.remove(value)` (removes by value) with `.pop(index)` (removes by index).

**Shallow copy trap:**
```python
a = [1, 2, 3]
b = a          # b refers to the SAME list
b.append(4)
print(a)       # a is also changed!
```
**Output:**
```
[1, 2, 3, 4]
```
To create an independent copy, use `b = a.copy()` or `b = a[:]`.

---

## 11. Tuples

A `tuple` is an **ordered, immutable** collection.

```python
point = (3, 4)
single = (5,)     # comma needed for a single-element tuple
print(point, type(point))
print(single, type(single))
```
**Output:**
```
(3, 4) <class 'tuple'>
(5,) <class 'tuple'>
```

---

## 12. Tuple Operations

```python
t = (1, 2, 3, 4)
print(t[0], t[-1])
print(t[1:3])
print(t + (5, 6))       # concatenation creates a new tuple
print(t * 2)             # repetition
a, b, c, d = t            # unpacking
print(a, b, c, d)

# t[0] = 100   # TypeError: 'tuple' object does not support item assignment
```
**Output:**
```
1 4
(2, 3)
(1, 2, 3, 4, 5, 6)
(1, 2, 3, 4, 1, 2, 3, 4)
1 2 3 4
```

**Why use a tuple instead of a list?** Tuples are faster, use less memory, and their immutability protects data from accidental modification — useful for fixed collections like coordinates or database records.

---

## 13. Sets

A `set` is an **unordered collection of unique elements**.

```python
s = {1, 2, 3, 2, 1}
print(s)               # duplicates automatically removed
s.add(4)
print(s)
s.remove(2)
print(s)
print(3 in s)
```
**Output:**
```
{1, 2, 3}
{1, 2, 3, 4}
{1, 3, 4}
True
```

---

## 14. Set Operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))          # or a | b
print(a.intersection(b))   # or a & b
print(a.difference(b))     # or a - b
print(a.symmetric_difference(b))  # or a ^ b
```
**Output:**
```
{1, 2, 3, 4, 5, 6}
{3, 4}
{1, 2}
{1, 2, 5, 6}
```

**Real-world use:** finding common elements between two datasets, removing duplicates, membership testing (very fast — O(1) average).

---

## 15. Dictionaries

A `dict` stores data as **key-value pairs**. Keys must be unique and immutable (str, int, tuple); values can be anything.

```python
student = {"name": "Rohan", "age": 21, "course": "CS"}
print(student)
print(student["name"])
student["age"] = 22          # update
student["grade"] = "A"       # add new key
print(student)
```
**Output:**
```
{'name': 'Rohan', 'age': 21, 'course': 'CS'}
Rohan
{'name': 'Rohan', 'age': 22, 'course': 'CS', 'grade': 'A'}
```

---

## 16. Dictionary Methods

```python
student = {"name": "Rohan", "age": 22, "course": "CS"}
print(student.keys())
print(student.values())
print(student.items())
print(student.get("age"))
print(student.get("marks", "N/A"))   # default if key missing
student.pop("course")
print(student)
for key, value in student.items():
    print(key, "->", value)
```
**Output:**
```
dict_keys(['name', 'age', 'course'])
dict_values(['Rohan', 22, 'CS'])
dict_items([('name', 'Rohan'), ('age', 22), ('course', 'CS')])
22
N/A
{'name': 'Rohan', 'age': 22}
name -> Rohan
age -> 22
```

**Common mistake:** Using `student["marks"]` for a non-existent key raises `KeyError`. Use `.get()` to avoid this.

---

## 17. Nested Data Structures

```python
students = [
    {"name": "Asha", "marks": [85, 90, 78]},
    {"name": "Ravi", "marks": [70, 65, 80]}
]

for s in students:
    avg = sum(s["marks"]) / len(s["marks"])
    print(f"{s['name']}: average = {avg:.2f}")
```
**Output:**
```
Asha: average = 84.33
Ravi: average = 71.67
```

---

## 18. List Comprehension

A compact way to build a list from an iterable.

```python
squares = [x**2 for x in range(1, 6)]
print(squares)

evens = [x for x in range(1, 20) if x % 2 == 0]
print(evens)

words = ["hi", "world", "python"]
lengths = [len(w) for w in words]
print(lengths)
```
**Output:**
```
[1, 4, 9, 16, 25]
[2, 4, 6, 8, 10, 12, 14, 16, 18]
[2, 5, 6]
```

Equivalent loop form (for comparison):
```python
squares = []
for x in range(1, 6):
    squares.append(x**2)
```

---

## 19. Set Comprehension

```python
nums = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {x**2 for x in nums}
print(unique_squares)
```
**Output:**
```
{1, 4, 9, 16, 25}
```

---

## 20. Dictionary Comprehension

```python
nums = [1, 2, 3, 4, 5]
square_map = {x: x**2 for x in nums}
print(square_map)

words = ["apple", "bat", "cat"]
lengths = {w: len(w) for w in words}
print(lengths)
```
**Output:**
```
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
{'apple': 5, 'bat': 3, 'cat': 3}
```

---

## 21–24. Functions, Definition, Parameters, Arguments

A function is a reusable, named block of code.

```python
def greet(name):
    """Greets a person by name."""
    return f"Hello, {name}!"

message = greet("Meera")
print(message)
```
**Output:**
```
Hello, Meera!
```

- `def` declares a function.
- `name` is a **parameter** (placeholder in the definition).
- `"Meera"` is an **argument** (actual value passed when calling).
- `return` sends a value back to the caller. A function without `return` returns `None`.

---

## 25. Positional Arguments

Arguments matched to parameters by their order.

```python
def describe_pet(animal, name):
    print(f"{name} is a {animal}")

describe_pet("dog", "Rex")
```
**Output:**
```
Rex is a dog
```

## 26. Keyword Arguments

Arguments passed by explicitly naming the parameter — order doesn't matter.

```python
describe_pet(name="Rex", animal="dog")
```
**Output:**
```
Rex is a dog
```

## 27. Default Arguments

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Tom")
greet("Tom", "Welcome")
```
**Output:**
```
Hello, Tom!
Welcome, Tom!
```

**Common mistake:** Using a mutable default argument (like a list) causes it to be shared across calls:
```python
def add_item(item, items=[]):   # BAD PRACTICE
    items.append(item)
    return items

print(add_item("a"))
print(add_item("b"))   # unexpectedly contains 'a' too!
```
**Output:**
```
['a']
['a', 'b']
```
**Fix:** use `None` as the default and create the list inside the function.
```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

## 28. *args

Collects any number of extra **positional** arguments into a tuple.

```python
def total(*args):
    return sum(args)

print(total(1, 2, 3))
print(total(10, 20, 30, 40))
```
**Output:**
```
6
100
```

## 29. **kwargs

Collects any number of extra **keyword** arguments into a dictionary.

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Asha", age=21, city="Pune")
```
**Output:**
```
name: Asha
age: 21
city: Pune
```

---

## 30. Return Values

```python
def add_and_multiply(a, b):
    return a + b, a * b   # returns a tuple

s, p = add_and_multiply(3, 4)
print(s, p)
```
**Output:**
```
7 12
```

---

## 31–33. Scope: Local and Global Variables

```python
x = 10   # global variable

def modify():
    x = 20   # local variable — different from global x
    print("Inside function:", x)

modify()
print("Outside function:", x)
```
**Output:**
```
Inside function: 20
Outside function: 10
```

To modify a global variable inside a function, use the `global` keyword:
```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)
```
**Output:**
```
2
```

---

## 34. Lambda Functions

Anonymous, single-expression functions defined with the `lambda` keyword.

```python
square = lambda x: x ** 2
add = lambda a, b: a + b

print(square(5))
print(add(3, 4))
```
**Output:**
```
25
7
```

**Best practice:** Use lambdas for short, throwaway functions (e.g., as a `key` for sorting), not for complex logic — use a regular `def` function instead for readability.

```python
students = [("Asha", 85), ("Ravi", 72), ("Meera", 90)]
students.sort(key=lambda s: s[1], reverse=True)
print(students)
```
**Output:**
```
[('Meera', 90), ('Asha', 85), ('Ravi', 72)]
```

---

## 35. map()

Applies a function to every item of an iterable.

```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)
```
**Output:**
```
[1, 4, 9, 16]
```

## 36. filter()

Keeps items where the function returns `True`.

```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
```
**Output:**
```
[2, 4, 6]
```

## 37. reduce()

Combines all items into a single value. Must be imported from `functools`.

```python
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda a, b: a * b, nums)
print(product)
```
**Output:**
```
24
```

---

## 38. Recursion

A function that calls itself, with a **base case** to stop the recursion.

```python
def factorial(n):
    if n == 0 or n == 1:    # base case
        return 1
    return n * factorial(n - 1)   # recursive case

print(factorial(5))
```
**Output:**
```
120
```

**Trace for `factorial(5)`:** `5 * factorial(4)` → `5 * 4 * factorial(3)` → ... → `5*4*3*2*1 = 120`.

**Common mistake:** Forgetting the base case causes infinite recursion and `RecursionError: maximum recursion depth exceeded`.

Another example — Fibonacci using recursion:
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(8)])
```
**Output:**
```
[0, 1, 1, 2, 3, 5, 8, 13]
```

---

## 39–44. Modules and Packages

### 40. import

A module is simply a `.py` file containing reusable code.

```python
import math
print(math.sqrt(16))
print(math.pi)

from math import sqrt, pi
print(sqrt(25))

import math as m
print(m.factorial(5))
```
**Output:**
```
4.0
3.141592653589793
5.0
120
```

### 41. Creating Custom Modules

**File: `calculator.py`**
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

**File: `main.py`** (in the same folder)
```python
import calculator

print(calculator.add(5, 3))
print(calculator.subtract(5, 3))
```
**Output:**
```
8
2
```

### 42. Packages

A **package** is a folder containing multiple modules plus an `__init__.py` file (which can be empty), allowing the folder to be imported as a single unit.

```
mypackage/
    __init__.py
    math_ops.py
    string_ops.py
```
```python
from mypackage import math_ops
```

### 43–44. `__name__` and `__main__`

Every Python file has a built-in variable `__name__`. When a file is run directly, `__name__` equals `"__main__"`. When imported, it equals the module's name.

```python
# calculator.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Running directly:", add(2, 3))
```
Running `python calculator.py` directly prints `Running directly: 5`. Importing it elsewhere with `import calculator` does **not** run that print statement.

**Best practice:** This pattern lets a file work both as a standalone script and as an importable module.

### 45. Standard Library Introduction

Python ships with many built-in modules — no installation needed:

| Module | Purpose |
|---|---|
| `math` | Mathematical functions |
| `random` | Random number generation |
| `datetime` | Date and time handling |
| `os` | Operating system interaction |
| `sys` | System-specific parameters |
| `json` | JSON encode/decode |
| `re` | Regular expressions |
| `collections` | Specialized container types |
| `itertools` | Efficient looping tools |

```python
import random
print(random.randint(1, 10))
print(random.choice(["red", "green", "blue"]))
```
**Sample Output:**
```
7
green
```

---

## Common Mistakes in Unit 2

1. Assuming `list.copy()` performs a deep copy — it's a **shallow copy** (nested objects are still shared).
2. Using a mutable default argument (`def f(x=[])`).
3. Forgetting `dict.get()` returns `None` (not an error) for missing keys unless you provide a default.
4. Confusing `map`/`filter` objects (lazy iterators) with lists — wrap with `list()` to see all values.
5. Writing recursive functions without a proper base case.
6. Modifying a list while iterating over it (causes skipped elements or bugs).

## Best Practices

1. Use list comprehensions for simple transformations; use regular loops for complex logic.
2. Prefer f-strings for formatting.
3. Use tuples for fixed, unchangeable data; lists for collections that change.
4. Use `*args`/`**kwargs` to make functions flexible, but document expected usage clearly.
5. Keep functions small and focused on a single task (Single Responsibility Principle).
6. Use `if __name__ == "__main__":` in every script meant to be both run and imported.

---

## Practice Questions (Unit 2)

1. Write a function that takes a list of numbers and returns a new list with only the even numbers, using list comprehension.
2. Write a program that counts the frequency of each word in a sentence using a dictionary.
3. Write a recursive function to compute the sum of digits of a number.
4. Write a function using `*args` that returns the maximum of any number of arguments.
5. Write a program to merge two dictionaries.
6. Write a function that removes duplicates from a list while preserving order.

## Interview Questions (Unit 2)

**Q1: What is the difference between a list and a tuple?**
A: Lists are mutable (can be changed after creation) and typically used for homogeneous collections that may grow or shrink. Tuples are immutable, generally faster, and often used for fixed collections of related values.

**Q2: What is the difference between `*args` and `**kwargs`?**
A: `*args` collects extra positional arguments into a tuple. `**kwargs` collects extra keyword arguments into a dictionary. Both let a function accept a variable number of arguments.

**Q3: What is the difference between shallow copy and deep copy?**
A: A shallow copy creates a new outer object but still shares references to nested (inner) objects. A deep copy (via `copy.deepcopy()`) recursively copies all nested objects too, so no memory is shared.

**Q4: Why are dictionary keys required to be immutable?**
A: Dictionaries use the key's hash value internally to organize and quickly locate values. Mutable objects (like lists) can change, which would change their hash and break the internal lookup — so Python disallows them as keys.

**Q5: What is the difference between `map()`/`filter()` and list comprehensions?**
A: Both can transform/filter iterables. `map()`/`filter()` take a function and an iterable and return a lazy iterator. List comprehensions are generally considered more Pythonic and readable for simple cases, while `map`/`filter` can be useful with existing named functions.

**Q6: Explain recursion and its base case.**
A: Recursion is when a function calls itself to solve smaller instances of a problem. The **base case** is the condition that stops the recursion — without it, the function calls itself indefinitely and raises `RecursionError`.

**Q7: What does `__name__ == "__main__"` mean?**
A: It checks whether the current file is being run directly (in which case `__name__` is `"__main__"`) versus being imported as a module into another file (in which case `__name__` is the module's own name).

---

*End of Unit 2. Continue to Unit 3 — Object-Oriented Programming and Error Handling.*
