# UNIT 1 — C++ FUNDAMENTALS

This unit is a self-contained knowledge base chapter on C++ fundamentals, structured for retrieval-augmented generation. Each section is independently understandable.

---

# Introduction to C++

## Definition
C++ is a general-purpose, compiled, statically-typed programming language that supports procedural, object-oriented, and generic programming. It was created as an extension of the C language, adding features like classes and objects.

## Why It Is Used
C++ gives programmers fine-grained control over memory and hardware while also supporting high-level abstractions like classes. This combination makes it suitable for performance-critical software — operating systems, game engines, browsers, embedded systems, and high-frequency trading systems.

## Example
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, C++!" << endl;
    return 0;
}
```
## Output
```
Hello, C++!
```

## Real-World Application
C++ powers Windows and Linux kernel components, Chrome/Firefox browser engines, Adobe software, most AAA video game engines (Unreal Engine), and financial trading systems where speed is critical.

---

# History of C++

## Definition
C++ was created by **Bjarne Stroustrup** at Bell Labs, starting in **1979** as "C with Classes," and was renamed C++ in 1983. The `++` reflects the increment operator, symbolizing C++ as an "incremented" version of C.

## Key Milestones
| Year | Standard | Notable Additions |
|---|---|---|
| 1998 | C++98 | First ISO standard |
| 2011 | C++11 | auto, lambda, smart pointers, range-based for |
| 2014 | C++14 | Minor improvements to C++11 |
| 2017 | C++17 | structured bindings, std::optional, if-init statements |
| 2020 | C++20 | concepts, ranges, coroutines, modules |

This knowledge base primarily uses **C++17**, and clearly marks any **C++11** or **C++20**-specific features.

---

# C vs C++

## Definition
C is a procedural programming language. C++ is a superset of C that adds object-oriented programming, templates, exception handling, and a rich standard library.

## Comparison Table

| Feature | C | C++ |
|---|---|---|
| Paradigm | Procedural | Procedural + Object-Oriented + Generic |
| Classes/Objects | Not supported | Supported |
| Function overloading | Not supported | Supported |
| Reference variables | Not supported | Supported |
| Standard I/O | `printf`/`scanf` | `cout`/`cin` (also supports printf/scanf) |
| Memory management | `malloc`/`free` | `new`/`delete` (also supports malloc/free) |
| Exception handling | Not supported | Supported (`try`/`catch`) |
| Standard Template Library | Not available | Available (vector, map, etc.) |

## Example
```cpp
// C style
#include <stdio.h>
int main() {
    printf("Hello from C style\n");
    return 0;
}
```
```cpp
// C++ style
#include <iostream>
using namespace std;
int main() {
    cout << "Hello from C++ style" << endl;
    return 0;
}
```
Both compile fine as C++ (C++ is largely backward-compatible with C), but idiomatic C++ prefers `cout`/`cin`, classes, and the STL.

---

# Features of C++

## Definition and Explanation
1. **Object-Oriented** — supports classes, inheritance, polymorphism, encapsulation, abstraction.
2. **Compiled language** — source code is translated directly to machine code by a compiler, producing fast executables.
3. **Statically typed** — variable types are checked at compile time, catching many errors before the program runs.
4. **Rich Standard Library** — the STL provides ready-made containers (vector, map) and algorithms (sort, find).
5. **Low-level memory control** — supports pointers and manual memory management (`new`/`delete`).
6. **Platform-independent (source code level)** — C++ code can be compiled on different operating systems, though the compiled binary is platform-specific.
7. **Multi-paradigm** — supports procedural, object-oriented, and generic (template-based) programming.

---

# Applications of C++

- **Operating systems and system software** — parts of Windows, Linux, macOS
- **Game development** — Unreal Engine, most AAA game engines
- **Browsers** — Chrome (V8's C++ core), Firefox
- **Embedded systems** — firmware for microcontrollers, IoT devices
- **Financial systems** — high-frequency trading platforms (speed-critical)
- **Databases** — MySQL, MongoDB core components
- **Compilers and interpreters** — many language toolchains are written in C++

---

# Installing a C++ Compiler

## Explanation
A compiler translates C++ source code (`.cpp` files) into machine code the computer's processor can execute. Common compilers:

- **GCC/G++** (GNU Compiler Collection) — free, cross-platform, most widely used for learning.
- **Clang** — used on macOS by default (via Xcode Command Line Tools).
- **MSVC** — Microsoft's compiler bundled with Visual Studio on Windows.

## Steps (General)
1. On Windows: install **MinGW-w64** (provides `g++`) or Visual Studio.
2. On macOS: install Xcode Command Line Tools (`xcode-select --install`), which includes Clang.
3. On Linux: install via package manager, e.g., `sudo apt install g++`.
4. Verify installation:
```bash
g++ --version
```
**Sample Output:**
```
g++ (Ubuntu 13.2.0) 13.2.0
```

---

# GCC/G++

## Definition
`g++` is the GNU C++ compiler front end. It compiles `.cpp` files into an executable.

## Syntax
```bash
g++ filename.cpp -o output_name
./output_name        # run the program (Linux/macOS)
output_name.exe       # run the program (Windows)
```

## Example
```bash
g++ hello.cpp -o hello -std=c++17
./hello
```
The `-std=c++17` flag tells the compiler which C++ standard to use — important since some features (like `std::optional`) require a specific standard version or newer.

## Common Mistakes
- Forgetting `-o output_name` — the compiler then defaults to `a.out` (Linux/macOS) or `a.exe` (Windows), which can be confusing.
- Compiling without specifying `-std=c++17` (or newer) when using modern C++ features, causing a compile error.

---

# VS Code Setup

## Steps
1. Install **Visual Studio Code**.
2. Install the **C/C++ extension** (by Microsoft) from the Extensions Marketplace.
3. Ensure `g++` (or another compiler) is installed and available on the system PATH.
4. Create a `.cpp` file, write code, then either:
   - Use the integrated terminal to compile/run with `g++`, or
   - Use the "Run" button (requires a configured `tasks.json`/`launch.json`).
5. VS Code offers IntelliSense (autocomplete), debugging, and Git integration for C++ projects.

---

# First C++ Program

```cpp
#include <iostream>     // header for input/output stream objects
using namespace std;    // avoids having to write std:: before cout, endl, etc.

int main() {             // program execution starts here
    cout << "Welcome to C++ Programming" << endl;
    return 0;             // 0 signals successful execution to the OS
}
```
## Line-by-Line Explanation
1. `#include <iostream>` — includes the input/output stream library, which provides `cin` and `cout`.
2. `using namespace std;` — lets us write `cout` instead of `std::cout`.
3. `int main() {` — the `main` function is the entry point; execution always starts here.
4. `cout << "Welcome to C++ Programming" << endl;` — prints text to the console; `endl` inserts a newline and flushes the output buffer.
5. `return 0;` — tells the operating system the program finished successfully (non-zero usually indicates an error).

## Output
```
Welcome to C++ Programming
```

---

# Structure of a C++ Program

## Explanation
A typical C++ program has these parts:
1. **Preprocessor directives** — `#include` statements that bring in libraries.
2. **Namespace declaration** — e.g., `using namespace std;` (optional but common for beginners).
3. **Global declarations** (optional) — constants, function prototypes, global variables.
4. **`main()` function** — where execution begins.
5. **Statements and expressions** — the actual logic.
6. **Return statement** — signals the exit status.

```cpp
#include <iostream>          // 1. Preprocessor directive
using namespace std;          // 2. Namespace declaration

const double PI = 3.14159;    // 3. Global constant

int main() {                   // 4. Entry point
    double radius = 5.0;
    double area = PI * radius * radius;   // 5. Statement
    cout << "Area: " << area << endl;
    return 0;                              // 6. Return statement
}
```
## Output
```
Area: 78.5397
```

---

# main()

## Definition
`main()` is the special function where every C++ program begins execution. Every valid, runnable C++ program must have exactly one `main()` function.

## Syntax
```cpp
int main() {
    // code
    return 0;
}
```
`main()` can also accept command-line arguments:
```cpp
int main(int argc, char* argv[]) {
    cout << "Number of arguments: " << argc << endl;
    return 0;
}
```
- `argc` — argument count (number of command-line arguments, including the program name itself).
- `argv` — argument vector (array of C-style strings holding the actual arguments).

## Common Mistakes
- Forgetting `return 0;` — technically allowed in C++ (the compiler implicitly returns 0 for `main` specifically), but it's best practice to include it explicitly.
- Declaring `main()` with the wrong return type — it must return `int`, not `void`, per the C++ standard.

---

# Comments

## Definition
Comments are notes in code ignored by the compiler, used to explain logic to human readers.

## Syntax
```cpp
// This is a single-line comment

/*
   This is a
   multi-line comment
*/
```

## Example
```cpp
#include <iostream>
using namespace std;

int main() {
    // Declare and initialize a variable
    int age = 20;  // age of the student

    /* Print the age
       to the console */
    cout << "Age: " << age << endl;
    return 0;
}
```
## Output
```
Age: 20
```

## Best Practices
- Write comments explaining **why**, not just what the code does.
- Avoid excessive/redundant comments that just restate obvious code.

---

# Variables

## Definition
A variable is a named memory location that stores a value of a specific type, which can change during program execution.

## Syntax
```cpp
type variable_name = value;
```

## Example
```cpp
#include <iostream>
using namespace std;

int main() {
    int age = 21;
    double price = 99.99;
    char grade = 'A';

    cout << age << " " << price << " " << grade << endl;
    return 0;
}
```
## Output
```
21 99.99 A
```

## Common Mistakes
- Using a variable before initializing it (its value is **undefined/garbage** in C++, unlike some languages that auto-initialize).
- Declaring the same variable name twice in the same scope, causing a compile error.

---

# Constants

## Definition
A constant is a value that cannot be changed after it is initialized. C++ provides `const` and `#define` for constants.

## Syntax
```cpp
const type name = value;      // preferred, type-safe
#define NAME value              // preprocessor macro, no type checking
```

## Example
```cpp
#include <iostream>
using namespace std;

const double PI = 3.14159;
#define MAX_USERS 100

int main() {
    cout << "PI: " << PI << endl;
    cout << "MAX_USERS: " << MAX_USERS << endl;
    // PI = 3.14;   // Compile error: assignment of read-only variable
    return 0;
}
```
## Output
```
PI: 3.14159
MAX_USERS: 100
```

## Best Practices
Prefer `const` (or `constexpr`, covered in Unit 5) over `#define` — `const` respects scoping rules and type checking, while `#define` performs plain text substitution and can cause subtle bugs.

---

# Identifiers

## Definition
Identifiers are names given to variables, functions, classes, and other user-defined items.

## Rules
- Can contain letters, digits, and underscores.
- Cannot start with a digit.
- Cannot be a C++ keyword.
- Case-sensitive (`age` and `Age` are different identifiers).

**Valid:** `total_marks`, `_count`, `student1`
**Invalid:** `1student` (starts with digit), `float` (keyword), `total-marks` (hyphen not allowed)

---

# Keywords

## Definition
Keywords are reserved words with predefined meaning in C++ and cannot be used as identifiers.

## Common C++ Keywords
```
int, float, double, char, bool, void, if, else, switch, case, for, while,
do, break, continue, return, class, struct, public, private, protected,
new, delete, this, virtual, static, const, namespace, using, template,
try, catch, throw, true, false, nullptr, auto
```

`auto`, `nullptr`, and `constexpr` are C++11 keywords added to the original C++ keyword set.

---

# Data Types

## Definition
A data type specifies what kind of value a variable can hold and how much memory it occupies.

## Overview Table

| Type | Description | Typical Size |
|---|---|---|
| `int` | Whole numbers | 4 bytes |
| `float` | Single-precision decimal | 4 bytes |
| `double` | Double-precision decimal | 8 bytes |
| `char` | Single character | 1 byte |
| `bool` | true/false | 1 byte |
| `void` | No value/type | — |

(Exact sizes are compiler/platform-dependent; use `sizeof()` to check on a given system.)

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "int: " << sizeof(int) << " bytes" << endl;
    cout << "float: " << sizeof(float) << " bytes" << endl;
    cout << "double: " << sizeof(double) << " bytes" << endl;
    cout << "char: " << sizeof(char) << " bytes" << endl;
    cout << "bool: " << sizeof(bool) << " bytes" << endl;
    return 0;
}
```
## Output (typical on most modern systems)
```
int: 4 bytes
float: 4 bytes
double: 8 bytes
char: 1 byte
bool: 1 byte
```

---

# int

## Definition
`int` stores whole numbers (positive, negative, or zero), typically 4 bytes, ranging roughly from -2,147,483,648 to 2,147,483,647.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 42;
    int b = -17;
    cout << a << " " << b << endl;
    return 0;
}
```
## Output
```
42 -17
```

## Common Mistakes
Integer overflow — assigning a value outside `int`'s range wraps around unpredictably rather than raising an error:
```cpp
int maxVal = 2147483647;
maxVal = maxVal + 1;    // overflow — undefined behavior, typically wraps to a large negative number
cout << maxVal << endl;
```
**Typical Output:**
```
-2147483648
```

---

# float

## Definition
`float` stores single-precision floating-point (decimal) numbers, typically 4 bytes, with about 6-7 significant decimal digits of precision.

```cpp
#include <iostream>
using namespace std;

int main() {
    float price = 99.99f;   // 'f' suffix marks this literal as a float, not double
    cout << price << endl;
    return 0;
}
```
## Output
```
99.99
```

---

# double

## Definition
`double` stores double-precision floating-point numbers, typically 8 bytes, offering about 15-16 significant decimal digits — more precise than `float`. This is the default floating-point type in C++ for literals like `3.14`.

```cpp
#include <iostream>
using namespace std;

int main() {
    double pi = 3.14159265358979;
    cout << pi << endl;
    return 0;
}
```
## Output
```
3.14159
```
(`cout` shows fewer digits by default; use `<iomanip>`'s `setprecision()` for full precision — see the operators/formatting section in later units.)

## Best Practices
Prefer `double` over `float` unless memory is tightly constrained (e.g., embedded systems) — `double` provides more precision and is the default for floating-point literals.

---

# char

## Definition
`char` stores a single character, 1 byte, internally represented as an integer (its ASCII/character code).

```cpp
#include <iostream>
using namespace std;

int main() {
    char grade = 'A';
    cout << grade << endl;
    cout << (int)grade << endl;   // shows the underlying ASCII value
    return 0;
}
```
## Output
```
A
65
```

---

# bool

## Definition
`bool` stores a truth value: `true` or `false`, internally represented as `1` and `0`.

```cpp
#include <iostream>
using namespace std;

int main() {
    bool isPassed = true;
    bool isFailed = false;
    cout << isPassed << " " << isFailed << endl;   // prints 1 and 0 by default
    cout << boolalpha << isPassed << " " << isFailed << endl;   // prints true/false
    return 0;
}
```
## Output
```
1 0
true false
```

---

# void

## Definition
`void` represents "no type" or "no value." It is used for functions that don't return a value, and for generic pointers (`void*`).

```cpp
#include <iostream>
using namespace std;

void greet() {          // no return value
    cout << "Hello!" << endl;
}

int main() {
    greet();
    return 0;
}
```
## Output
```
Hello!
```

---

# Type Modifiers

## Definition
Type modifiers alter the size or range/sign of a base data type.

| Modifier | Meaning |
|---|---|
| `signed` | can hold negative and positive values (default for int) |
| `unsigned` | can hold only non-negative values (doubles the positive range) |
| `short` | reduced size integer |
| `long` | extended size integer |

```cpp
#include <iostream>
using namespace std;

int main() {
    short s = 100;
    long l = 1000000L;
    unsigned int u = 4000000000u;
    long long ll = 9223372036854775807LL;

    cout << s << " " << l << " " << u << " " << ll << endl;
    return 0;
}
```
## Output
```
100 1000000 4000000000 9223372036854775807
```

## Common Mistakes
Assigning a negative value to an `unsigned` type doesn't raise an error — it wraps around to a very large positive number:
```cpp
unsigned int x = -1;
cout << x << endl;
```
**Typical Output:**
```
4294967295
```

---

# Type Conversion

## Definition
Type conversion is changing a value from one data type to another. **Implicit conversion** happens automatically; **explicit conversion (type casting)** is done manually by the programmer.

## Example — Implicit Conversion
```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 5;
    double b = a;    // int implicitly converted to double
    cout << b << endl;

    double x = 9.7;
    int y = x;         // double implicitly converted (truncated) to int
    cout << y << endl;
    return 0;
}
```
## Output
```
5
9
```
Note: converting `double` to `int` truncates the decimal part (doesn't round).

---

# Type Casting

## Definition
Type casting is explicit, programmer-directed type conversion.

## Syntax (C-style and C++ style)
```cpp
(type) expression;              // C-style cast
static_cast<type>(expression);  // C++ style cast (preferred)
```

## Example
```cpp
#include <iostream>
using namespace std;

int main() {
    double price = 49.95;
    int rounded = static_cast<int>(price);   // preferred modern C++ style
    int oldStyle = (int)price;                // C-style, still works but less safe

    cout << rounded << " " << oldStyle << endl;
    return 0;
}
```
## Output
```
49 49
```

## Best Practices
Prefer `static_cast<>` over C-style casts — it is more explicit about intent and is checked more strictly by the compiler, reducing the chance of unsafe/unintended conversions.

---

# Input using cin

## Definition
`cin` (character input) reads data from the standard input (usually the keyboard) into variables.

```cpp
#include <iostream>
using namespace std;

int main() {
    string name;
    int age;

    cout << "Enter your name: ";
    cin >> name;
    cout << "Enter your age: ";
    cin >> age;

    cout << name << " is " << age << " years old" << endl;
    return 0;
}
```
## Sample Run
```
Enter your name: Ravi
Enter your age: 22
Ravi is 22 years old
```

## Common Mistakes
`cin >> name` with `string name;` reads only **one word** (stops at whitespace). To read a full line including spaces, use `getline(cin, name)` instead.

```cpp
#include <iostream>
using namespace std;

int main() {
    string fullName;
    cout << "Enter your full name: ";
    getline(cin, fullName);
    cout << "Hello, " << fullName << endl;
    return 0;
}
```
**Sample Run:**
```
Enter your full name: Ravi Kumar
Hello, Ravi Kumar
```

---

# Output using cout

## Definition
`cout` (character output) sends data to standard output (usually the console), using the insertion operator `<<`.

```cpp
#include <iostream>
using namespace std;

int main() {
    int marks = 95;
    cout << "Marks: " << marks << ", Grade: " << 'A' << endl;
    cout << "Line 1" << "\n" << "Line 2" << endl;
    return 0;
}
```
## Output
```
Marks: 95, Grade: A
Line 1
Line 2
```

`endl` inserts a newline and flushes the output buffer; `"\n"` inserts only a newline (slightly faster since it doesn't force a flush).

---

# Operators

## Overview
C++ provides several categories of operators used to perform operations on variables and values.

---

# Arithmetic Operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `7 + 2` | `9` |
| `-` | Subtraction | `7 - 2` | `5` |
| `*` | Multiplication | `7 * 2` | `14` |
| `/` | Division | `7 / 2` | `3` (integer division) |
| `%` | Modulus | `7 % 2` | `1` |

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 7, b = 2;
    cout << a + b << " " << a - b << " " << a * b << " " << a / b << " " << a % b << endl;

    double x = 7.0, y = 2.0;
    cout << x / y << endl;   // true decimal division
    return 0;
}
```
## Output
```
9 5 14 3 1
3.5
```

## Common Mistakes
`int / int` performs **integer division** (truncates the decimal part), which surprises many beginners. `7 / 2` gives `3`, not `3.5`. To get a decimal result, at least one operand must be a `float`/`double`.

---

# Relational Operators

| Operator | Meaning |
|---|---|
| `==` | equal to |
| `!=` | not equal to |
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal to |
| `<=` | less than or equal to |

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 5, b = 8;
    cout << (a == b) << " " << (a != b) << " " << (a < b) << " " << (a >= b) << endl;
    return 0;
}
```
## Output
```
0 1 1 0
```
(C++ prints `bool` results as `1`/`0` by default.)

---

# Logical Operators

| Operator | Meaning |
|---|---|
| `&&` | logical AND |
| `\|\|` | logical OR |
| `!` | logical NOT |

```cpp
#include <iostream>
using namespace std;

int main() {
    bool a = true, b = false;
    cout << (a && b) << " " << (a || b) << " " << (!a) << endl;
    return 0;
}
```
## Output
```
0 1 0
```

---

# Assignment Operators

| Operator | Equivalent |
|---|---|
| `=` | assign |
| `+=` | `x = x + y` |
| `-=` | `x = x - y` |
| `*=` | `x = x * y` |
| `/=` | `x = x / y` |
| `%=` | `x = x % y` |

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 10;
    x += 5;
    cout << x << endl;
    x *= 2;
    cout << x << endl;
    return 0;
}
```
## Output
```
15
30
```

---

# Increment and Decrement

## Definition
`++` increases a value by 1; `--` decreases it by 1. Both have **prefix** (`++x`) and **postfix** (`x++`) forms, which behave differently when used in an expression.

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 5;
    cout << x++ << endl;    // prints 5, THEN increments x to 6 (postfix)
    cout << x << endl;       // now shows 6

    int y = 5;
    cout << ++y << endl;      // increments y to 6 FIRST, then prints 6 (prefix)
    return 0;
}
```
## Output
```
5
6
6
```

## Common Mistakes
Confusing prefix and postfix behavior inside complex expressions (e.g., `arr[i++]` vs `arr[++i]`) is a classic source of bugs — always trace through carefully or split into separate statements for clarity.

---

# Bitwise Operators

| Operator | Meaning |
|---|---|
| `&` | AND |
| `\|` | OR |
| `^` | XOR |
| `~` | NOT (complement) |
| `<<` | left shift |
| `>>` | right shift |

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 6, b = 3;   // 110, 011 in binary
    cout << (a & b) << " " << (a | b) << " " << (a ^ b) << " " << (~a) << " " << (a << 1) << " " << (a >> 1) << endl;
    return 0;
}
```
## Output
```
2 7 5 -7 12 3
```

## Real-World Application
Bitwise operators are heavily used in low-level programming — setting/clearing flags, working with hardware registers, compact data encoding, and performance-critical algorithms (e.g., checking if a number is a power of two).

---

# Conditional Operator

## Definition
The ternary operator `?:` is a shorthand for a simple if-else expression.

## Syntax
```cpp
condition ? value_if_true : value_if_false;
```

```cpp
#include <iostream>
using namespace std;

int main() {
    int age = 20;
    string result = (age >= 18) ? "Adult" : "Minor";
    cout << result << endl;
    return 0;
}
```
## Output
```
Adult
```

---

# Operator Precedence

## Definition
Operator precedence determines the order in which operators are evaluated in an expression without parentheses. Simplified order (highest to lowest): `()` > unary (`++`, `--`, `!`) > `*, /, %` > `+, -` > relational > logical AND/OR > assignment.

```cpp
#include <iostream>
using namespace std;

int main() {
    int result = 5 + 3 * 2;         // * evaluated first
    cout << result << endl;

    int result2 = (5 + 3) * 2;      // parentheses override default precedence
    cout << result2 << endl;
    return 0;
}
```
## Output
```
11
16
```

## Best Practices
Use parentheses liberally in complex expressions, even when not strictly necessary, to make the intended evaluation order clear to future readers.

---

# Conditional Statements

# if

```cpp
#include <iostream>
using namespace std;

int main() {
    int marks = 85;
    if (marks >= 40) {
        cout << "Passed" << endl;
    }
    return 0;
}
```
## Output
```
Passed
```

# if-else

```cpp
#include <iostream>
using namespace std;

int main() {
    int marks = 30;
    if (marks >= 40) {
        cout << "Passed" << endl;
    } else {
        cout << "Failed" << endl;
    }
    return 0;
}
```
## Output
```
Failed
```

# nested if

```cpp
#include <iostream>
using namespace std;

int main() {
    int num = 15;
    if (num > 0) {
        if (num % 2 == 0) {
            cout << "Positive even" << endl;
        } else {
            cout << "Positive odd" << endl;
        }
    } else {
        cout << "Non-positive" << endl;
    }
    return 0;
}
```
## Output
```
Positive odd
```

# else-if

```cpp
#include <iostream>
using namespace std;

int main() {
    int marks = 72;
    char grade;

    if (marks >= 90) grade = 'A';
    else if (marks >= 75) grade = 'B';
    else if (marks >= 60) grade = 'C';
    else grade = 'D';

    cout << "Grade: " << grade << endl;
    return 0;
}
```
## Output
```
Grade: C
```

## Common Mistakes
Using `=` instead of `==` inside a condition is a classic C/C++ bug: `if (x = 5)` compiles (it assigns 5 to x and evaluates as true), but does NOT compare x to 5. Always double-check comparison operators.

# switch

## Definition
`switch` selects one of many code blocks to execute based on the value of a variable, often more readable than a long `if-else-if` chain for discrete values.

```cpp
#include <iostream>
using namespace std;

int main() {
    int day = 3;
    switch (day) {
        case 1:
            cout << "Monday" << endl;
            break;
        case 2:
            cout << "Tuesday" << endl;
            break;
        case 3:
            cout << "Wednesday" << endl;
            break;
        default:
            cout << "Invalid day" << endl;
    }
    return 0;
}
```
## Output
```
Wednesday
```

## Common Mistakes
Forgetting `break;` after a `case` causes **fall-through** — execution continues into the next case unintentionally:
```cpp
int day = 2;
switch (day) {
    case 1:
        cout << "Monday" << endl;
    case 2:
        cout << "Tuesday" << endl;   // executes
    case 3:
        cout << "Wednesday" << endl;  // ALSO executes (fall-through!)
        break;
}
```
**Output:**
```
Tuesday
Wednesday
```

---

# Loops

# for loop

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 0; i < 5; i++) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}
```
## Output
```
0 1 2 3 4
```
## Line-by-Line Explanation
- `int i = 0` — initialization, runs once at the start.
- `i < 5` — condition, checked before every iteration; loop continues while true.
- `i++` — update, runs after each iteration.

# while loop

```cpp
#include <iostream>
using namespace std;

int main() {
    int count = 0;
    while (count < 5) {
        cout << count << " ";
        count++;
    }
    cout << endl;
    return 0;
}
```
## Output
```
0 1 2 3 4
```

# do-while

## Definition
`do-while` checks the condition **after** executing the loop body, guaranteeing the body runs at least once.

```cpp
#include <iostream>
using namespace std;

int main() {
    int num;
    do {
        cout << "This runs at least once" << endl;
        num = 10;
    } while (num < 5);
    return 0;
}
```
## Output
```
This runs at least once
```

## Common Mistakes
Forgetting the semicolon `;` after `while(condition)` in a `do-while` loop — this is required, unlike a regular `while` loop, and its absence causes a compile error.

# break

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 0; i < 10; i++) {
        if (i == 5) break;
        cout << i << " ";
    }
    cout << endl;
    return 0;
}
```
## Output
```
0 1 2 3 4
```

# continue

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 0; i < 5; i++) {
        if (i == 2) continue;
        cout << i << " ";
    }
    cout << endl;
    return 0;
}
```
## Output
```
0 1 3 4
```

# nested loops

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= 3; j++) {
            cout << "(" << i << "," << j << ") ";
        }
        cout << endl;
    }
    return 0;
}
```
## Output
```
(1,1) (1,2) (1,3) 
(2,1) (2,2) (2,3) 
(3,1) (3,2) (3,3) 
```

---

# Arrays

## Definition
An array is a fixed-size collection of elements of the same type, stored in contiguous memory.

# One-dimensional Arrays

## Syntax
```cpp
type arrayName[size] = {values};
```

```cpp
#include <iostream>
using namespace std;

int main() {
    int marks[5] = {85, 90, 78, 92, 60};

    for (int i = 0; i < 5; i++) {
        cout << marks[i] << " ";
    }
    cout << endl;

    cout << "First element: " << marks[0] << endl;
    cout << "Array size (bytes): " << sizeof(marks) << endl;
    cout << "Number of elements: " << sizeof(marks) / sizeof(marks[0]) << endl;
    return 0;
}
```
## Output
```
85 90 78 92 60 
First element: 85
Array size (bytes): 20
Number of elements: 5
```

## Common Mistakes
Accessing an index outside the array bounds (e.g., `marks[5]` for a 5-element array with valid indices 0-4) does **not** raise an error in C++ — it reads/writes into adjacent memory, causing **undefined behavior**. This is a common source of serious bugs and security vulnerabilities.

# Two-dimensional Arrays

## Syntax
```cpp
type arrayName[rows][cols] = {{...}, {...}};
```

```cpp
#include <iostream>
using namespace std;

int main() {
    int matrix[2][3] = {
        {1, 2, 3},
        {4, 5, 6}
    };

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
```
## Output
```
1 2 3 
4 5 6 
```

## Real-World Application
2D arrays represent grids, matrices, images (pixel data), game boards (like tic-tac-toe or chess), and tables of data.

---

# Strings Introduction

## Definition
C++ supports two kinds of strings:
1. **C-style strings** — arrays of `char` terminated by a null character `\0`.
2. **`std::string`** — a modern, safer, and easier-to-use class from the C++ Standard Library (covered fully in Unit 2).

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    char cstyle[] = "Hello";        // C-style string
    string modern = "Hello, C++";   // std::string

    cout << cstyle << endl;
    cout << modern << endl;
    cout << modern.length() << endl;
    cout << modern + "!" << endl;    // std::string supports concatenation with +
    return 0;
}
```
## Output
```
Hello
Hello, C++
10
Hello, C++!
```

## Best Practices
Prefer `std::string` over C-style character arrays in modern C++ — it manages memory automatically, supports easy concatenation/comparison, and avoids common buffer-overflow bugs. C-style strings and full `std::string` operations are covered in depth in Unit 2.

---

# Unit 1 Summary

- C++ is a compiled, statically-typed, multi-paradigm language extending C with object-oriented features.
- Every C++ program starts execution in `main()`, and typically includes `#include <iostream>` for I/O.
- Core built-in types: `int`, `float`, `double`, `char`, `bool`, `void`, with modifiers like `signed`/`unsigned`/`short`/`long`.
- Operators include arithmetic, relational, logical, assignment, bitwise, increment/decrement, and the ternary conditional operator.
- Conditional statements (`if`, `if-else`, `switch`) and loops (`for`, `while`, `do-while`) control program flow, supported by `break`, `continue`.
- Arrays store fixed-size collections of same-typed elements, in 1D or 2D forms.
- `std::string` is the modern, preferred way to work with text over raw C-style strings.

## Important Concepts to Remember
- Integer division truncates; use `double`/`float` for decimal results.
- `switch` requires `break` to prevent fall-through.
- Array bounds are not checked automatically in C++ — out-of-bounds access is undefined behavior.
- `static_cast<>` is the preferred, safer alternative to C-style casts.

---

# Frequently Asked Questions

**Q: Is C++ the same as C with just added features?**
A: C++ started as "C with Classes" and remains largely backward-compatible with C, but it has evolved into a distinct, much larger language with object-oriented programming, templates, exception handling, and a large standard library that C does not have.

**Q: Why does `7 / 2` give `3` instead of `3.5` in C++?**
A: Because both operands are `int`, C++ performs integer division, which truncates (discards) the decimal part. To get `3.5`, at least one operand must be a floating-point type, e.g., `7.0 / 2`.

**Q: What happens if I access an array index out of bounds?**
A: C++ does not perform automatic bounds checking on raw arrays. Accessing an out-of-bounds index results in **undefined behavior** — it might read garbage data, corrupt other memory, or crash, without a guaranteed error message.

**Q: Should I use `#define` or `const` for constants?**
A: Prefer `const` (or `constexpr` for compile-time constants, covered in Unit 5). `#define` performs raw text substitution via the preprocessor with no type checking, which can lead to subtle bugs; `const` is type-safe and scoped properly.

---

# Interview Questions (Unit 1)

**Q1: What is the difference between C and C++?**
A: C is purely procedural, while C++ is a multi-paradigm language supporting procedural, object-oriented, and generic programming. C++ adds classes, function overloading, references, exception handling, templates, and the STL, which C lacks.

**Q2: What is the difference between `float` and `double`?**
A: `float` is single-precision (typically 4 bytes, ~6-7 significant digits), while `double` is double-precision (typically 8 bytes, ~15-16 significant digits). `double` is more precise and is the default type for floating-point literals in C++.

**Q3: What is the difference between `=` and `==`?**
A: `=` is the assignment operator, used to assign a value to a variable. `==` is the equality comparison operator, used to check if two values are equal. Confusing them inside an `if` condition is a classic bug since `if (x = 5)` compiles but assigns rather than compares.

**Q4: What is the difference between prefix (`++x`) and postfix (`x++`) increment?**
A: Prefix increment increases the value first, then returns the updated value. Postfix increment returns the current value first, then increases it. This distinction matters when the increment is used within a larger expression.

**Q5: Why is `switch` sometimes preferred over multiple `if-else-if` statements?**
A: `switch` can be more readable when comparing a single variable against many discrete constant values, and some compilers can optimize it into a jump table for faster branching compared to sequential `if-else-if` checks.

**Q6: What does `sizeof()` do, and why is it useful?**
A: `sizeof()` returns the size, in bytes, of a data type or variable. It's useful for understanding memory layout, calculating the number of elements in a fixed-size array (`sizeof(arr) / sizeof(arr[0])`), and for portability across platforms where type sizes may vary.

**Q7: What is undefined behavior in C++, and why is it dangerous?**
A: Undefined behavior refers to code whose behavior the C++ standard does not define or guarantee — such as out-of-bounds array access or signed integer overflow. It's dangerous because the program might appear to "work" during testing but fail unpredictably (crash, produce wrong results, or even become a security vulnerability) under different compilers, optimization levels, or inputs.

**Q8: What is the difference between C-style strings and `std::string`?**
A: C-style strings are null-terminated `char` arrays requiring manual memory management and careful bounds handling. `std::string` is a C++ standard library class that manages memory automatically, supports operators like `+` for concatenation, and provides many built-in methods, making it safer and easier to use.

---

# Practice Problems (Unit 1)

1. Write a program to swap two numbers without using a third (temporary) variable.
2. Write a program to check whether a given year is a leap year.
3. Write a program to find the largest of three numbers using nested `if`.
4. Write a program that prints a multiplication table for a number entered by the user.
5. Write a program to reverse the digits of an integer.
6. Write a program using a `switch` statement to build a simple calculator (+, -, *, /).
7. Write a program to find the sum and average of elements in a 1D array.
8. Write a program to add two 2x2 matrices using 2D arrays.
9. Write a program to check if a number is prime using a `for` loop.
10. Write a program to print the Fibonacci series up to n terms using a `while` loop.

---

# Coding Challenges (Unit 1)

**Challenge 1:** Write a program that reads 10 integers into an array and prints them in reverse order without using a second array.

**Challenge 2:** Write a program to find the second largest element in an array without sorting it.

**Challenge 3:** Write a program that prints a right-angled triangle pattern of stars using nested loops, where the number of rows is provided by the user.

```cpp
// Sample solution for Challenge 3
#include <iostream>
using namespace std;

int main() {
    int rows;
    cout << "Enter number of rows: ";
    cin >> rows;

    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}
```
**Sample Run (rows = 4):**
```
Enter number of rows: 4
* 
* * 
* * * 
* * * * 
```

---

*End of Unit 1 — C++ Fundamentals. Say "Generate Unit 2" to continue with Functions, Strings, Pointers and References.*
