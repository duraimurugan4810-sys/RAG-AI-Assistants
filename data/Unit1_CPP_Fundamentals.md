UNIT 1 — C++ FUNDAMENTALS

This unit covers: References, Memory Management, and Constructors/Destructors.

====================================================================
# TOPIC 1: REFERENCES
====================================================================

## Definition
A reference in C++ is an alias — an alternative name — for an already-existing variable. Once a reference is bound to a variable, any operation performed on the reference is actually performed on the original variable. Unlike a pointer, a reference is not a separate object that stores an address; it is a name bound directly to another object's storage.

## Why It Is Used
- To avoid copying large objects when passing them to functions (pass-by-reference instead of pass-by-value).
- To allow a function to modify the caller's variable directly (output parameters).
- To create cleaner, safer syntax than pointers (no need for dereferencing operators, no risk of a null reference in well-formed code).
- To implement operator overloading efficiently (e.g., `operator<<`, `operator=`).
- To enable range-based for loops to modify elements of a container in place.

## Syntax
```cpp
// Declaring a reference
int a = 10;
int& ref = a;   // ref is now another name for a

// Reference as a function parameter
void increment(int& x) {
    x++;
}

// Reference as a function return type
int& getElement(std::vector<int>& v, int index) {
    return v[index];
}

// Const reference (read-only alias, avoids copying)
void printValue(const std::string& s) {
    std::cout << s << std::endl;
}
```

## Example

### Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

// Function that modifies the caller's variable using a reference
void doubleValue(int& num) {
    num = num * 2;
}

// Function that returns a reference to a vector element
int& getElement(vector<int>& v, int index) {
    return v[index];
}

int main() {
    int x = 5;
    cout << "Before: x = " << x << endl;

    doubleValue(x);   // x is passed by reference
    cout << "After: x = " << x << endl;

    vector<int> numbers = {1, 2, 3, 4, 5};
    getElement(numbers, 2) = 100;  // modifies numbers[2] directly

    cout << "Vector after modification: ";
    for (int n : numbers) {
        cout << n << " ";
    }
    cout << endl;

    // Reference alias demonstration
    int a = 10;
    int& refA = a;
    refA = 20;   // changes a as well
    cout << "a = " << a << ", refA = " << refA << endl;

    return 0;
}
```

### Output
```
Before: x = 5
After: x = 10
Vector after modification: 1 2 100 4 5
a = 20, refA = 20
```

## Line-by-Line Explanation
- `void doubleValue(int& num)` — The parameter `num` is a reference to whatever `int` is passed in. No copy is made; `num` literally refers to the caller's variable.
- `num = num * 2;` — Because `num` is an alias for `x`, this line changes `x` itself.
- `doubleValue(x);` — Calling the function with `x` binds `num` to `x` for the duration of the call.
- `int& getElement(vector<int>& v, int index) { return v[index]; }` — Returns a reference to the actual element inside the vector, not a copy. This allows the caller to modify the vector element directly through the returned reference.
- `getElement(numbers, 2) = 100;` — Because the function returns a reference, this line assigns 100 directly into `numbers[2]`.
- `int& refA = a;` — `refA` becomes another name for `a`. There is no separate memory location for `refA`; it shares `a`'s memory.
- `refA = 20;` — Since `refA` and `a` are the same variable under two names, `a` becomes 20 too.

## Real-World Application
- **Function parameter passing in large systems**: Passing large objects (strings, vectors, custom classes) by `const&` avoids expensive copies in performance-critical code such as game engines and financial trading systems.
- **Operator overloading**: The `operator<<` for `std::ostream` takes and returns references so that chained calls like `cout << a << b;` work efficiently.
- **Range-based for loops**: `for (auto& item : container)` uses references to modify elements in place, common in data processing pipelines.
- **Swap functions and algorithms**: `std::swap(a, b)` uses references internally to exchange values without copying.

## Common Mistakes
1. **Trying to reseat a reference**: Once bound, a reference cannot be changed to refer to a different variable. Assigning to a reference assigns to the referred object, not the reference itself.
2. **Returning a reference to a local variable**: This creates a dangling reference because the local variable is destroyed when the function returns.
   ```cpp
   int& badFunction() {
       int local = 5;
       return local; // ERROR: dangling reference
   }
   ```
3. **Forgetting `const` when a reference should be read-only**: This can lead to accidental modification of the caller's data.
4. **Confusing references with pointers**: A reference must be initialized when declared and cannot be null; a pointer can be reassigned and can be null.
5. **Creating a reference to a temporary and expecting it to persist beyond its lifetime rules**: Only `const` references (or rvalue references) can bind to temporaries, and the lifetime extension rules must be understood carefully.

## Best Practices
- Prefer `const&` for function parameters when the object is large and should not be modified.
- Use non-`const` references only when the function is genuinely intended to modify the caller's variable.
- Never return a reference to a local (stack) variable.
- Use references over pointers whenever null-ability and reseating are not required — references communicate intent more clearly.
- Document clearly when a function takes a reference parameter to signal that the caller's data may be modified.

## Interview Questions
1. What is the difference between a reference and a pointer in C++?
2. Can a reference be null? Why or why not?
3. Why must a reference be initialized at the time of declaration?
4. What happens if you return a reference to a local variable from a function?
5. What is the difference between passing by value, passing by pointer, and passing by reference?
6. Explain reference collapsing rules in the context of templates (advanced).
7. What is an rvalue reference, and how does it differ from an lvalue reference?
8. Why do STL algorithms often take references or const references as parameters?

## Practice Problems
1. Write a function `swapValues(int& a, int& b)` that swaps two integers without using a temporary return value.
2. Write a function that takes a `const string&` and returns the number of vowels in it.
3. Given a `vector<int>`, write a function using references that doubles every element in place.
4. Explain (in comments) why the following code fails to compile, then fix it:
   ```cpp
   int& getRef() {
       int x = 42;
       return x;
   }
   ```
5. Write a class `Counter` with a method `int& value()` that returns a reference to its internal counter so external code can modify it directly.

====================================================================
# TOPIC 2: MEMORY MANAGEMENT
====================================================================

## Definition
Memory management in C++ refers to the process of allocating, using, and releasing memory during program execution. C++ provides two primary categories of memory: **stack memory** (automatically managed, fast, limited size) and **heap memory** (dynamically managed by the programmer using `new`/`delete` or by smart pointers, larger, slower to allocate).

## Why It Is Used
- To create objects whose size or lifetime is not known at compile time.
- To build dynamic data structures (linked lists, trees, graphs) that grow and shrink at runtime.
- To control object lifetime explicitly, independent of scope.
- To optimize performance by choosing appropriate memory strategies for different situations (stack for small short-lived data, heap for large or long-lived data).

## Syntax
```cpp
// Stack allocation (automatic)
int x = 10;

// Heap allocation using new/delete
int* p = new int(5);
delete p;

// Dynamic array allocation
int* arr = new int[10];
delete[] arr;

// Heap allocation of an object
class MyClass {};
MyClass* obj = new MyClass();
delete obj;

// Modern approach: smart pointers (see Topic on Smart Pointers in Unit 4)
#include <memory>
std::unique_ptr<int> smartPtr = std::make_unique<int>(5);
```

## Example

### Code
```cpp
#include <iostream>
using namespace std;

class Resource {
public:
    Resource(int id) : id(id) {
        cout << "Resource " << id << " acquired." << endl;
    }
    ~Resource() {
        cout << "Resource " << id << " released." << endl;
    }
    int getId() const { return id; }
private:
    int id;
};

int main() {
    // Stack allocation: automatically destroyed at end of scope
    {
        Resource stackResource(1);
        cout << "Using stack resource with id: " << stackResource.getId() << endl;
    } // stackResource destructor called here automatically

    // Heap allocation: must be manually released
    Resource* heapResource = new Resource(2);
    cout << "Using heap resource with id: " << heapResource->getId() << endl;
    delete heapResource;   // must explicitly delete to avoid memory leak

    // Dynamic array on the heap
    int* dynamicArray = new int[5];
    for (int i = 0; i < 5; i++) {
        dynamicArray[i] = i * i;
    }
    cout << "Dynamic array contents: ";
    for (int i = 0; i < 5; i++) {
        cout << dynamicArray[i] << " ";
    }
    cout << endl;
    delete[] dynamicArray;  // must use delete[] for arrays

    return 0;
}
```

### Output
```
Resource 1 acquired.
Using stack resource with id: 1
Resource 1 released.
Resource 2 acquired.
Using heap resource with id: 2
Resource 2 released.
Dynamic array contents: 0 1 4 9 16
```

## Line-by-Line Explanation
- `Resource stackResource(1);` — Creates an object on the stack. Its constructor runs immediately.
- The closing `}` of the inner block — Triggers the destructor automatically because `stackResource` goes out of scope. This is the basis of RAII (Resource Acquisition Is Initialization).
- `Resource* heapResource = new Resource(2);` — Allocates memory on the heap and calls the constructor. The pointer `heapResource` stores the address of this memory.
- `delete heapResource;` — Calls the destructor and frees the heap memory. Forgetting this line causes a memory leak.
- `int* dynamicArray = new int[5];` — Allocates an array of 5 integers on the heap.
- `delete[] dynamicArray;` — Frees the array memory. Using `delete` (without brackets) on an array allocated with `new[]` is undefined behavior.

## Real-World Application
- **Game engines**: Objects like enemies, projectiles, and particles are often allocated dynamically and released when destroyed, requiring careful memory management to avoid leaks and stutter from excessive allocation.
- **Embedded systems**: Memory is limited, so understanding stack vs. heap trade-offs is critical for real-time performance.
- **Server applications**: Long-running processes must avoid leaks; tools like Valgrind or AddressSanitizer are used to detect memory issues.
- **Custom data structures**: Implementing a linked list, tree, or hash map from scratch requires manual (or smart-pointer-based) heap management.

## Common Mistakes
1. **Memory leaks**: Forgetting to call `delete` or `delete[]` after `new`/`new[]`.
2. **Double deletion**: Calling `delete` twice on the same pointer, which causes undefined behavior.
3. **Dangling pointers**: Using a pointer after the memory it points to has been deleted.
4. **Mismatched new/delete**: Using `delete` on memory allocated with `new[]`, or vice versa.
5. **Not setting pointers to `nullptr` after deletion**, which can make dangling pointer bugs harder to detect.
6. **Stack overflow from deep recursion or huge local arrays**, since stack memory is much more limited than heap memory.

## Best Practices
- Prefer smart pointers (`unique_ptr`, `shared_ptr`) over raw `new`/`delete` in modern C++ (see Unit 4).
- Follow RAII: tie resource lifetime to object lifetime so cleanup happens automatically via destructors.
- Always match `new` with `delete` and `new[]` with `delete[]`.
- Set raw pointers to `nullptr` after deleting them if they might be checked or reused later.
- Use tools like Valgrind, AddressSanitizer, or Visual Studio's memory diagnostics to catch leaks during development.
- Minimize manual memory management in application-level code; reserve raw `new`/`delete` for low-level library or systems code.

## Interview Questions
1. What is the difference between stack and heap memory in C++?
2. What causes a memory leak, and how can it be prevented?
3. What is the difference between `delete` and `delete[]`?
4. What is a dangling pointer, and how can it be avoided?
5. Explain RAII and how it relates to memory management.
6. What happens if you call `delete` on a pointer twice?
7. What are the trade-offs between stack and heap allocation in terms of speed and lifetime?
8. How do smart pointers help prevent memory leaks compared to raw pointers?

## Practice Problems
1. Write a program that allocates an array of 10 doubles on the heap, fills it with squares of indices, prints it, and properly frees the memory.
2. Write a class `Buffer` that allocates a dynamic array in its constructor and frees it in its destructor, demonstrating RAII.
3. Identify and fix the bug in the following code:
   ```cpp
   int* ptr = new int(5);
   delete ptr;
   delete ptr;
   ```
4. Write a program that intentionally leaks memory, then describe (in comments) how you would detect the leak using a tool.
5. Compare the performance implications of allocating 1000 small objects on the stack vs. the heap; write a short explanation.

====================================================================
# TOPIC 3: CONSTRUCTORS AND DESTRUCTORS
====================================================================

## Definition
A **constructor** is a special member function of a class that is automatically invoked when an object of that class is created; it is used to initialize the object's data members. A **destructor** is a special member function that is automatically invoked when an object is destroyed (goes out of scope or is deleted); it is used to release resources the object may hold.

## Why It Is Used
- To guarantee that an object starts its life in a valid, well-defined state (constructor).
- To guarantee that resources (memory, file handles, network connections, locks) are properly released when an object's lifetime ends (destructor).
- To implement the RAII (Resource Acquisition Is Initialization) idiom, which ties resource management to object lifetime.
- To support different ways of creating objects via constructor overloading (default, parameterized, copy, move).

## Syntax
```cpp
class MyClass {
public:
    // Default constructor
    MyClass() {
        // initialization code
    }

    // Parameterized constructor
    MyClass(int value) : data(value) {
        // initialization code
    }

    // Copy constructor
    MyClass(const MyClass& other) : data(other.data) {
        // deep copy logic if needed
    }

    // Destructor
    ~MyClass() {
        // cleanup code
    }

private:
    int data;
};
```

## Example

### Code
```cpp
#include <iostream>
#include <string>
using namespace std;

class Employee {
public:
    // Default constructor
    Employee() : name("Unknown"), salary(0.0) {
        cout << "Default constructor called for " << name << endl;
    }

    // Parameterized constructor
    Employee(string empName, double empSalary) : name(empName), salary(empSalary) {
        cout << "Parameterized constructor called for " << name << endl;
    }

    // Copy constructor
    Employee(const Employee& other) : name(other.name), salary(other.salary) {
        cout << "Copy constructor called for " << name << endl;
    }

    // Destructor
    ~Employee() {
        cout << "Destructor called for " << name << endl;
    }

    void display() const {
        cout << name << " earns " << salary << endl;
    }

private:
    string name;
    double salary;
};

int main() {
    cout << "--- Creating emp1 with default constructor ---" << endl;
    Employee emp1;
    emp1.display();

    cout << "\n--- Creating emp2 with parameterized constructor ---" << endl;
    Employee emp2("Alice", 75000.0);
    emp2.display();

    cout << "\n--- Creating emp3 as a copy of emp2 ---" << endl;
    Employee emp3(emp2);
    emp3.display();

    cout << "\n--- End of main, destructors will now be called in reverse order ---" << endl;
    return 0;
}
```

### Output
```
--- Creating emp1 with default constructor ---
Default constructor called for Unknown
Unknown earns 0

--- Creating emp2 with parameterized constructor ---
Parameterized constructor called for Alice
Alice earns 75000

--- Creating emp3 as a copy of emp2 ---
Copy constructor called for Alice
Alice earns 75000

--- End of main, destructors will now be called in reverse order ---
Destructor called for Alice
Destructor called for Alice
Destructor called for Unknown
```

## Line-by-Line Explanation
- `Employee() : name("Unknown"), salary(0.0) { ... }` — The default constructor uses a member initializer list to set `name` and `salary` before the constructor body runs.
- `Employee(string empName, double empSalary) : name(empName), salary(empSalary) { ... }` — The parameterized constructor initializes members directly from the arguments passed.
- `Employee(const Employee& other) : name(other.name), salary(other.salary) { ... }` — The copy constructor creates a new object by copying the data members of an existing object (`other`). It takes a `const&` to avoid infinite recursion (a copy constructor taking by value would need to copy its argument, calling itself again).
- `~Employee() { ... }` — The destructor is called automatically. It has no return type and no parameters, and a class can only have one destructor.
- `Employee emp3(emp2);` — Invokes the copy constructor because `emp3` is being initialized directly from `emp2`.
- At the end of `main()`, the destructors run in **reverse order of construction**: `emp3`, then `emp2`, then `emp1` — this is why "Alice" appears destructed twice (once for `emp3`, once for `emp2`) before "Unknown" (`emp1`).

## Real-World Application
- **Database connection classes**: Constructor opens a connection; destructor closes it automatically, ensuring connections are never left open by accident.
- **File handling wrappers**: Constructor opens a file; destructor closes it, following RAII so files are never left unclosed even if an exception is thrown.
- **Smart pointer implementations**: `unique_ptr` and `shared_ptr` rely entirely on constructor/destructor pairs to manage heap memory automatically.
- **Logging systems**: A `ScopedTimer` class can log elapsed time by recording a start time in the constructor and printing the duration in the destructor, useful for profiling code blocks.

## Common Mistakes
1. **Forgetting to define a destructor when a class manages a raw resource** (like a `new`-allocated pointer), causing memory leaks.
2. **Defining a copy constructor incorrectly (shallow copy) for a class that owns dynamically allocated memory**, leading to double-free errors when both objects are destroyed.
3. **Not marking single-argument constructors `explicit`**, which can lead to unintended implicit conversions.
4. **Throwing exceptions from a destructor**, which is dangerous and can cause `std::terminate` to be called if another exception is already propagating.
5. **Relying on constructor/destructor call order across translation units for global/static objects**, which is not guaranteed by the standard (the "static initialization order fiasco").

## Best Practices
- Use member initializer lists rather than assignment inside the constructor body for efficiency and correctness (especially for `const` members and references).
- Follow the "Rule of Three/Five/Zero": if a class defines any of destructor, copy constructor, or copy assignment operator, it usually needs to define all three (Rule of Three); in modern C++, also consider move constructor and move assignment (Rule of Five), or design the class to need none of them (Rule of Zero) by using smart pointers/STL containers.
- Mark single-parameter constructors `explicit` unless implicit conversion is genuinely desired.
- Keep destructors simple and never let them throw exceptions.
- Prefer RAII wrappers (smart pointers, STL containers) over manual resource management to minimize the need for custom destructors.

## Interview Questions
1. What is the difference between a constructor and a destructor?
2. Can a class have multiple constructors? Can it have multiple destructors?
3. What is a copy constructor, and when is it invoked?
4. What is the Rule of Three (and Rule of Five) in C++?
5. Why should a destructor never throw an exception?
6. What is the purpose of a member initializer list, and why is it preferred over assignment in the constructor body?
7. What happens if you don't define a destructor for a class that allocates heap memory?
8. In what order are constructors and destructors called for objects with inheritance (base and derived classes)?
9. What is a virtual destructor, and why is it needed in polymorphic base classes? (see Unit 2 — Inheritance/Polymorphism)

## Practice Problems
1. Write a class `DynamicArray` that allocates an array in its constructor and frees it in its destructor. Implement a proper copy constructor to avoid double-free errors.
2. Demonstrate constructor and destructor call order by creating three objects of a class `Logger` in `main()` and observing the console output.
3. Write a class with a deliberately shallow copy constructor, show how it causes a bug, then fix it with a deep copy.
4. Implement a `ScopedTimer` class that prints the elapsed time between construction and destruction using `<chrono>`.
5. Explain why the following class is dangerous and fix it:
   ```cpp
   class Bad {
   public:
       Bad() { data = new int[100]; }
       // no destructor, no copy constructor defined
   private:
       int* data;
   };
   ```

====================================================================
UNIT 1 SUMMARY
====================================================================
This unit covered three foundational pillars of C++ programming:
- **References** provide safe, alias-based access to variables, enabling efficient parameter passing and cleaner syntax than pointers.
- **Memory Management** distinguishes between automatic stack memory and manually managed heap memory, and introduces the discipline needed to avoid leaks, dangling pointers, and double deletions.
- **Constructors and Destructors** define how objects are initialized and cleaned up, forming the basis of the RAII idiom that underlies safe resource management throughout modern C++.

Together, these topics form the base layer on which inheritance, polymorphism, STL usage, templates, exception handling, and smart pointers (covered in later units) are built.

## Important Concepts
- Reference vs. pointer semantics
- Pass-by-value vs. pass-by-reference vs. pass-by-pointer
- Stack allocation vs. heap allocation
- `new`/`delete` and `new[]`/`delete[]` pairing
- RAII (Resource Acquisition Is Initialization)
- Default, parameterized, and copy constructors
- Member initializer lists
- Rule of Three / Rule of Five / Rule of Zero
- Destructor call order and exception safety

## Frequently Asked Questions
**Q: Can references be reassigned to refer to a different variable?**
A: No. Once a reference is bound, it cannot be changed to alias a different object; assignment to a reference assigns to the underlying object.

**Q: Is heap memory automatically freed when a program ends?**
A: The operating system reclaims all process memory when a program terminates, but relying on this is bad practice; leaked memory during a long-running program's execution still causes real problems (growing memory usage, degraded performance).

**Q: Why use a member initializer list instead of assigning inside the constructor body?**
A: It initializes members directly (avoiding a default construction followed by an assignment), is required for `const` members and reference members, and is generally more efficient.

**Q: What happens if a class has a pointer member but no custom copy constructor?**
A: The compiler generates a default copy constructor that performs a shallow copy, copying the pointer value (address) rather than the pointed-to data. This can lead to double-free errors when both objects' destructors run.

## Interview Questions (Unit Recap)
1. Explain references vs pointers with examples.
2. What is a memory leak and how do you prevent it?
3. Explain the Rule of Three/Five/Zero.
4. Why must destructors avoid throwing exceptions?
5. Walk through constructor and destructor call order for stack vs heap objects.

## Practice Exercises
1. Write a `Point` class with x and y coordinates, a parameterized constructor, a copy constructor, and a destructor that prints a message when called.
2. Write a function that swaps two `Point` objects using references.
3. Allocate a `Point` object on the heap, use it, and properly delete it.
4. Create a class that violates the Rule of Three, demonstrate the resulting bug, then fix it.

## Coding Challenges
1. **Resource Manager**: Implement a class `FileHandle` that simulates opening a file in the constructor (print "File opened") and closing it in the destructor (print "File closed"). Ensure copies are handled safely (either deep-copy the resource or delete the copy constructor).
2. **Reference-Based Swap**: Implement a generic `template<typename T> void mySwap(T& a, T& b)` function without using `std::swap`.
3. **Leak Hunter**: Given a code snippet with multiple `new` calls and only some matching `delete` calls, identify every leak and rewrite the code so it is leak-free.
4. **Deep Copy Challenge**: Implement a `Matrix` class that dynamically allocates a 2D array in its constructor, and correctly implements a deep-copy copy constructor and a matching destructor.
