# UNIT 3 — OBJECT ORIENTED PROGRAMMING AND ERROR HANDLING

This unit is a self-contained knowledge base chapter covering classes, objects, inheritance, polymorphism, abstraction, dunder methods, iterators/generators, and exception handling.

---

## 1. Object-Oriented Programming (OOP)

OOP is a programming paradigm that organizes code around **objects** — bundles of data (attributes) and behavior (methods) — instead of just functions and logic.

**Four pillars of OOP:**
1. **Encapsulation** — bundling data and methods together, restricting direct access to some details.
2. **Inheritance** — a class can reuse and extend another class.
3. **Polymorphism** — the same interface/method name can behave differently for different classes.
4. **Abstraction** — hiding complex implementation details, exposing only what's necessary.

---

## 2–3. Classes and Objects

A **class** is a blueprint. An **object** (instance) is a concrete thing built from that blueprint.

```python
class Dog:
    pass

d1 = Dog()
d2 = Dog()
print(type(d1))
print(d1 is d2)
```
**Output:**
```
<class '__main__.Dog'>
False
```
`d1` and `d2` are two separate objects created from the same class.

---

## 4–5. Attributes and Methods

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name      # instance attribute
        self.breed = breed

    def bark(self):           # instance method
        return f"{self.name} says Woof!"

d1 = Dog("Rex", "Labrador")
print(d1.name, d1.breed)
print(d1.bark())
```
**Output:**
```
Rex Labrador
Rex says Woof!
```

---

## 6–7. Constructors and `__init__()`

`__init__()` is a special method automatically called when an object is created. It initializes the object's attributes.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print(f"Student object created for {self.name}")

s1 = Student("Priya", 88)
```
**Output:**
```
Student object created for Priya
```

---

## 8. `self`

`self` refers to the **current instance** of the class. It must be the first parameter of every instance method (Python passes it automatically).

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1     # self refers to THIS object's count

c1 = Counter()
c2 = Counter()
c1.increment()
c1.increment()
c2.increment()
print(c1.count, c2.count)   # each object keeps its own state
```
**Output:**
```
2 1
```

---

## 9–10. Instance Variables vs Class Variables

- **Instance variables**: unique to each object, defined with `self.`
- **Class variables**: shared across all objects of the class, defined directly inside the class body.

```python
class Student:
    school_name = "Green Valley High"   # class variable, shared

    def __init__(self, name):
        self.name = name                # instance variable, unique

s1 = Student("Asha")
s2 = Student("Ravi")
print(s1.school_name, s2.school_name)
Student.school_name = "Blue Ridge High"   # changes for ALL instances
print(s1.school_name, s2.school_name)

s1.name = "Ashwini"   # only changes s1's own instance variable
print(s1.name, s2.name)
```
**Output:**
```
Green Valley High Green Valley High
Blue Ridge High Blue Ridge High
Ashwini Ravi
```

---

## 11–13. Instance Methods, Class Methods, Static Methods

```python
class Employee:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):                       # instance method — needs an object
        print(f"{self.name} earns {self.salary}")

    @classmethod
    def change_company(cls, new_name):    # class method — works on the class itself
        cls.company = new_name

    @staticmethod
    def is_valid_salary(amount):          # static method — no access to self/cls
        return amount > 0

e1 = Employee("Kiran", 50000)
e1.show()
Employee.change_company("InnovateX")
print(Employee.company)
print(Employee.is_valid_salary(-100))
```
**Output:**
```
Kiran earns 50000
InnovateX
False
```

| Type | First parameter | Access | Called via |
|---|---|---|---|
| Instance method | `self` | Instance + class data | Object |
| Class method | `cls` | Class data only | Class or object |
| Static method | none required | Neither (utility function) | Class or object |

---

## 14. Encapsulation

Encapsulation restricts direct access to some attributes, exposing controlled access through methods. Python uses **naming conventions** rather than strict access modifiers:

- `public_var` — accessible from anywhere
- `_protected_var` — convention: "internal use", still accessible
- `__private_var` — name-mangled, harder to access from outside

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance     # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())
# print(acc.__balance)   # AttributeError: no attribute '__balance'
print(acc._BankAccount__balance)   # name mangling — still technically accessible
```
**Output:**
```
1500
1500
```

---

## 15–19. Inheritance

Inheritance allows a class (**child/subclass**) to reuse attributes and methods of another class (**parent/superclass**).

### 16. Single Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):        # Dog inherits from Animal
    def bark(self):
        print(f"{self.name} is barking")

d = Dog("Rex")
d.eat()     # inherited method
d.bark()    # own method
```
**Output:**
```
Rex is eating
Rex is barking
```

### 17. Multiple Inheritance

A class inherits from more than one parent class.

```python
class Flyable:
    def fly(self):
        print("I can fly")

class Swimmable:
    def swim(self):
        print("I can swim")

class Duck(Flyable, Swimmable):
    pass

d = Duck()
d.fly()
d.swim()
```
**Output:**
```
I can fly
I can swim
```

### 18. Multilevel Inheritance

A chain: Grandparent → Parent → Child.

```python
class Animal:
    def eat(self):
        print("Eating")

class Mammal(Animal):
    def walk(self):
        print("Walking")

class Dog(Mammal):
    def bark(self):
        print("Barking")

d = Dog()
d.eat()
d.walk()
d.bark()
```
**Output:**
```
Eating
Walking
Barking
```

### 19. Hierarchical Inheritance

One parent, multiple children.

```python
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

Car().start()
Bike().start()
```
**Output:**
```
Vehicle started
Vehicle started
```

### 20. Method Overriding

A child class provides its own implementation of a method already defined in the parent.

```python
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Cat(Animal):
    def sound(self):              # overrides parent's method
        print("Meow")

Animal().sound()
Cat().sound()
```
**Output:**
```
Some generic animal sound
Meow
```

---

## 21–22. Polymorphism and Duck Typing

**Polymorphism** means "many forms" — the same method name behaves differently depending on the object.

```python
class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Woof"

for animal in [Cat(), Dog()]:
    print(animal.sound())
```
**Output:**
```
Meow
Woof
```

**Duck typing**: "If it walks like a duck and quacks like a duck, it's a duck." Python doesn't check an object's type before calling a method — it just checks whether the method exists.

```python
class Duck:
    def sound(self):
        return "Quack"

class Robot:
    def sound(self):     # no inheritance relationship at all, but has same method name
        return "Beep"

def make_it_talk(thing):
    print(thing.sound())

make_it_talk(Duck())
make_it_talk(Robot())
```
**Output:**
```
Quack
Beep
```

---

## 23–25. Abstraction and Abstract Classes

Abstraction hides implementation details and exposes only essential features. In Python, abstract classes are created using the `abc` module.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass    # no implementation — subclasses MUST override this

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# shape = Shape()   # TypeError: Can't instantiate abstract class Shape
r = Rectangle(5, 3)
print(r.area())
```
**Output:**
```
15
```

If `Rectangle` did NOT implement `area()`, instantiating it would raise `TypeError: Can't instantiate abstract class Rectangle with abstract method area`.

**Interfaces in Python:** Python doesn't have a dedicated `interface` keyword like Java. Abstract classes with only abstract methods serve the same purpose — defining a contract that subclasses must follow.

---

## 26. `super()`

`super()` gives access to methods of the parent class, commonly used inside `__init__` to call the parent's constructor.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # call parent's __init__
        self.breed = breed

    def describe(self):
        print(f"{self.name} is a {self.breed}")

d = Dog("Rex", "Labrador")
d.describe()
```
**Output:**
```
Rex is a Labrador
```

---

## 27–31. Special (Dunder) Methods

"Dunder" = double underscore. These let custom classes work with Python's built-in syntax (`print()`, `len()`, `==`, etc.).

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        """User-friendly string, used by print() and str()."""
        return f"Book: {self.title}"

    def __repr__(self):
        """Developer-friendly string, used in the REPL/debugger."""
        return f"Book(title={self.title!r}, pages={self.pages})"

    def __len__(self):
        """Called by len()."""
        return self.pages

    def __eq__(self, other):
        """Called by ==."""
        return self.title == other.title and self.pages == other.pages

b1 = Book("Python 101", 250)
b2 = Book("Python 101", 250)

print(b1)             # uses __str__
print(repr(b1))        # uses __repr__
print(len(b1))          # uses __len__
print(b1 == b2)          # uses __eq__
```
**Output:**
```
Book: Python 101
Book(title='Python 101', pages=250)
250
True
```

**Best practice:** Always define `__repr__` for debugging; define `__str__` when you want a nicer display for end users.

---

## 32–33. Iterators and Iterables

- **Iterable**: an object you can loop over (has `__iter__`), e.g., list, string, dict.
- **Iterator**: an object that produces the next value one at a time (has `__next__`), created from an iterable.

```python
nums = [1, 2, 3]
it = iter(nums)          # get an iterator from the iterable
print(next(it))
print(next(it))
print(next(it))
# print(next(it))        # raises StopIteration — no more items
```
**Output:**
```
1
2
3
```

Custom iterator class:
```python
class CountUp:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current

for num in CountUp(5):
    print(num, end=" ")
```
**Output:**
```
1 2 3 4 5
```

---

## 34–35. Generators and `yield`

A generator is a simpler way to create an iterator using a function with `yield` instead of `return`. It produces values **lazily** (one at a time), saving memory.

```python
def count_up(limit):
    current = 1
    while current <= limit:
        yield current
        current += 1

for num in count_up(5):
    print(num, end=" ")
```
**Output:**
```
1 2 3 4 5
```

**Why use generators?** They don't store the entire sequence in memory — useful for very large or infinite sequences.

```python
def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci_gen()
first_10 = [next(gen) for _ in range(10)]
print(first_10)
```
**Output:**
```
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

## 36–41. Exception Handling

Errors that occur during execution (not caught at parse time) are called **exceptions**. Unhandled exceptions crash the program.

```python
print(10 / 0)
```
**Output:**
```
ZeroDivisionError: division by zero
```

### 37–40. try, except, else, finally

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That's not a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result: {result}")     # runs only if no exception occurred
finally:
    print("Execution finished")    # always runs, error or not
```
**Sample run (input = 0):**
```
Enter a number: 0
Cannot divide by zero
Execution finished
```
**Sample run (input = 5):**
```
Enter a number: 5
Result: 2.0
Execution finished
```

**Catching multiple exception types together:**
```python
try:
    x = int("abc")
except (ValueError, TypeError) as e:
    print(f"Error occurred: {e}")
```
**Output:**
```
Error occurred: invalid literal for int() with base 10: 'abc'
```

**Catching any exception (use sparingly):**
```python
try:
    risky_code = 1 / 0
except Exception as e:
    print(f"Something went wrong: {e}")
```
**Output:**
```
Something went wrong: division by zero
```

### 41. raise

Manually trigger an exception.

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount

try:
    withdraw(100, 500)
except ValueError as e:
    print(f"Transaction failed: {e}")
```
**Output:**
```
Transaction failed: Insufficient balance
```

### 42. Custom Exceptions

Create your own exception classes by inheriting from `Exception`.

```python
class InsufficientBalanceError(Exception):
    """Raised when a withdrawal exceeds available balance."""
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(f"Cannot withdraw {amount}, balance is only {balance}")
    return balance - amount

try:
    withdraw(200, 300)
except InsufficientBalanceError as e:
    print(f"Error: {e}")
```
**Output:**
```
Error: Cannot withdraw 300, balance is only 200
```

### 43. Assertions

`assert` checks that a condition is `True`; if not, it raises `AssertionError`. Used mainly for debugging and internal checks (not for validating user input in production).

```python
def calculate_average(numbers):
    assert len(numbers) > 0, "List must not be empty"
    return sum(numbers) / len(numbers)

print(calculate_average([10, 20, 30]))
# calculate_average([])   # raises AssertionError: List must not be empty
```
**Output:**
```
20.0
```

### 44. Debugging Techniques

- Use `print()` statements to inspect variable values at key points.
- Use Python's built-in debugger: `import pdb; pdb.set_trace()` to pause execution and inspect state interactively.
- Use IDE breakpoints (VS Code, PyCharm) to step through code line by line.
- Read the **full traceback** — Python shows the exact line and call chain that caused an error.
- Use `try/except` temporarily around suspicious code to isolate where a failure occurs.
- Use `logging` (covered in Unit 5) instead of `print()` for production-quality debugging.

---

## Common Mistakes in Unit 3

1. Forgetting `self` as the first parameter of instance methods.
2. Confusing class variables with instance variables (modifying a class variable through one instance can unexpectedly affect all instances if done incorrectly).
3. Not calling `super().__init__()` in a child class, missing parent initialization.
4. Catching `Exception` too broadly, hiding real bugs.
5. Using `assert` for user-input validation in production code (asserts can be disabled with the `-O` flag).
6. Forgetting a `StopIteration`/termination condition in custom iterators, causing infinite loops.

## Best Practices

1. Use `__repr__` for debugging output, `__str__` for user-facing display.
2. Catch **specific** exceptions rather than bare `except:`.
3. Use custom exceptions for domain-specific errors (e.g., `InsufficientBalanceError`) — clearer than generic ones.
4. Favor composition or duck typing over deep inheritance chains when possible.
5. Use `finally` (or a `with` context manager, covered in Unit 5) to guarantee cleanup (closing files, releasing resources).
6. Keep exception messages clear and actionable.

---

## Practice Questions (Unit 3)

1. Create a `Vehicle` class with subclasses `Car` and `Bike` that override a `describe()` method.
2. Create a class `Circle` with a private radius attribute and methods to get/set it safely.
3. Write a custom generator that yields only even numbers up to a limit.
4. Create a custom exception `NegativeValueError` and raise it when a function receives a negative number.
5. Implement `__eq__` and `__lt__` for a `Point` class so two points can be compared.
6. Write a program that reads a list of numbers and safely handles `ValueError` for any non-numeric input.

## Interview Questions (Unit 3)

**Q1: What is the difference between a class method and a static method?**
A: A class method takes `cls` as its first parameter and can access/modify class-level state. A static method takes neither `self` nor `cls` — it's a regular function logically grouped inside the class, with no access to instance or class data unless passed explicitly.

**Q2: What is method overriding vs method overloading?**
A: Overriding is when a subclass provides a new implementation of a method already defined in its parent class. Python doesn't support traditional method overloading (same method name, different parameter lists) like Java/C++; similar behavior can be achieved using default arguments or `*args`/`**kwargs`.

**Q3: What is the difference between `__str__` and `__repr__`?**
A: `__str__` returns a readable string meant for end users (used by `print()`). `__repr__` returns an unambiguous string meant for developers/debugging (used in the REPL and by `repr()`). If `__str__` isn't defined, Python falls back to `__repr__`.

**Q4: What is the difference between an abstract class and a regular class?**
A: An abstract class (using `ABC` and `@abstractmethod`) cannot be instantiated directly and is meant to define a common interface that subclasses must implement. A regular class can be instantiated directly.

**Q5: What is the difference between `try-except-else` and `try-except-finally`?**
A: `else` runs only if no exception was raised in the `try` block. `finally` always runs, whether an exception occurred or not — typically used for cleanup code.

**Q6: What is duck typing?**
A: A style of dynamic typing where an object's suitability is determined by the presence of certain methods/behavior, not by its class or inheritance. "If it has a `.sound()` method, we can call `.sound()` on it," regardless of the object's actual type.

**Q7: What is the difference between an iterator and a generator?**
A: A generator is a specific, simpler way to create an iterator using a function with `yield`. Every generator is an iterator, but not every iterator is a generator (you can also build iterators manually with `__iter__`/`__next__` in a class).

**Q8: Why should you avoid catching bare `except:`?**
A: A bare `except:` catches *all* exceptions, including ones you didn't anticipate (like `KeyboardInterrupt` or `SystemExit`), which can hide real bugs and make debugging harder. It's better to catch specific exception types.

---

*End of Unit 3. Continue to Unit 4 — Files, Databases, Libraries and Data Handling.*
