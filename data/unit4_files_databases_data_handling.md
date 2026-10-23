# UNIT 4 — FILES, DATABASES, LIBRARIES AND DATA HANDLING

This unit is a self-contained knowledge base chapter covering file handling, regular expressions, date/time, essential modules, NumPy, Pandas, Matplotlib, SQLite, and REST APIs.

---

## 1–6. File Handling Basics

Python interacts with files using the built-in `open()` function.

```python
f = open("notes.txt", "w")   # open in write mode
f.write("Hello, file!")
f.close()                     # always close to release the file
```

**File modes:**

| Mode | Meaning |
|---|---|
| `"r"` | Read (default). Error if file doesn't exist. |
| `"w"` | Write. Creates file if missing; **overwrites** existing content. |
| `"a"` | Append. Creates file if missing; adds to the end. |
| `"x"` | Create. Fails if file already exists. |
| `"r+"` | Read and write. |
| `"rb"` / `"wb"` | Binary mode (for images, PDFs, etc.) |

---

## 3. Reading Files

```python
f = open("notes.txt", "r")
content = f.read()
print(content)
f.close()
```
**Output:**
```
Hello, file!
```

Other reading methods:
```python
with open("notes.txt", "r") as f:
    print(f.readline())      # reads one line
    f.seek(0)                 # reset pointer to start
    print(f.readlines())      # reads all lines into a list
```

---

## 4. Writing Files

```python
with open("output.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
```
Running this creates `output.txt` with:
```
Line 1
Line 2
```
**Note:** `"w"` mode erases any existing content before writing.

---

## 5. Appending Files

```python
with open("output.txt", "a") as f:
    f.write("Line 3\n")
```
`output.txt` now contains:
```
Line 1
Line 2
Line 3
```

---

## 6. The `with` Statement

`with` automatically closes the file when the block ends, even if an error occurs — safer than manually calling `.close()`.

```python
with open("notes.txt", "r") as f:
    data = f.read()
print(data)
print(f.closed)   # True — file is automatically closed after the block
```
**Output:**
```
Hello, file!
True
```

**Common mistake:** Forgetting to close a file manually (without `with`) can lead to resource leaks or unsaved data if the program crashes before `.close()` runs. **Best practice: always use `with`.**

---

## 7. Text Files — Full Example

```python
students = ["Asha,85", "Ravi,72", "Meera,90"]

with open("students.txt", "w") as f:
    for line in students:
        f.write(line + "\n")

with open("students.txt", "r") as f:
    for line in f:
        name, marks = line.strip().split(",")
        print(f"{name} scored {marks}")
```
**Output:**
```
Asha scored 85
Ravi scored 72
Meera scored 90
```

---

## 8. CSV Files

```python
import csv

# Writing a CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Asha", 22, "Pune"])
    writer.writerow(["Ravi", 25, "Delhi"])

# Reading a CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```
**Output:**
```
['Name', 'Age', 'City']
['Asha', '22', 'Pune']
['Ravi', '25', 'Delhi']
```

Using `csv.DictReader` for dictionary-style rows:
```python
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["City"])
```
**Output:**
```
Asha Pune
Ravi Delhi
```

---

## 9–10. JSON Files and Serialization

**Serialization** = converting a Python object into a storable/transmittable format (like JSON text). **Deserialization** = converting it back.

```python
import json

data = {"name": "Asha", "age": 22, "skills": ["Python", "SQL"]}

# Serialize: Python dict -> JSON string
json_string = json.dumps(data, indent=4)
print(json_string)

# Write to a file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Read and deserialize: JSON file -> Python dict
with open("data.json", "r") as f:
    loaded = json.load(f)
print(loaded["skills"])
```
**Output:**
```
{
    "name": "Asha",
    "age": 22,
    "skills": [
        "Python",
        "SQL"
    ]
}
['Python', 'SQL']
```

---

## 11–12. Regular Expressions (`re` module)

Regular expressions (regex) are patterns used to search, match, and manipulate text.

```python
import re

text = "Contact us at support@example.com or sales@example.org"

# Find all email addresses
emails = re.findall(r"[\w.]+@[\w.]+", text)
print(emails)

# Check if a string matches a pattern
match = re.search(r"\d{3}-\d{3}-\d{4}", "Call 987-654-3210 now")
print(match.group() if match else "No match")

# Replace text
cleaned = re.sub(r"\s+", " ", "This   has    extra   spaces")
print(cleaned)

# Validate a pattern fully
is_valid = bool(re.fullmatch(r"[A-Za-z]+", "Python"))
print(is_valid)
```
**Output:**
```
['support@example.com', 'sales@example.org']
987-654-3210
This has extra spaces
True
```

**Common regex symbols:**

| Symbol | Meaning |
|---|---|
| `\d` | digit |
| `\w` | word character (letters, digits, underscore) |
| `\s` | whitespace |
| `+` | one or more |
| `*` | zero or more |
| `?` | zero or one |
| `^` | start of string |
| `$` | end of string |
| `[]` | character set |

---

## 13–14. Date and Time (`datetime` module)

```python
from datetime import datetime, timedelta

now = datetime.now()
print(now)
print(now.year, now.month, now.day)
print(now.strftime("%Y-%m-%d %H:%M:%S"))   # formatted string

# Parsing a string into a datetime object
dt = datetime.strptime("2025-01-15", "%Y-%m-%d")
print(dt)

# Date arithmetic
future = now + timedelta(days=10)
print(future.strftime("%Y-%m-%d"))
```
**Sample Output:**
```
2026-08-08 10:15:32.123456
2026 8 8
2026-08-08 10:15:32
2025-01-15 00:00:00
2026-08-18
```

---

## 15. Random Module

```python
import random

print(random.random())            # random float between 0 and 1
print(random.randint(1, 100))     # random integer in range
print(random.choice(["A", "B", "C"]))
print(random.sample(range(1, 50), 6))   # 6 unique random numbers (like a lottery draw)

items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)
```
**Sample Output:**
```
0.7623094
42
B
[3, 17, 29, 8, 41, 12]
[4, 1, 5, 2, 3]
```

---

## 16. Math Module

```python
import math

print(math.sqrt(16))
print(math.pow(2, 5))
print(math.factorial(5))
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.log(100, 10))
print(math.pi)
```
**Output:**
```
4.0
32.0
120
5
4
2.0
3.141592653589793
```

---

## 17. OS Module

```python
import os

print(os.getcwd())              # current working directory
os.makedirs("new_folder", exist_ok=True)
print(os.listdir("."))           # list files/folders in current directory
print(os.path.exists("data.csv"))
print(os.path.join("folder", "file.txt"))
```
**Sample Output:**
```
/home/user/project
['new_folder', 'data.csv', 'students.txt']
True
folder/file.txt
```

---

## 18. pathlib

A modern, object-oriented way to work with file paths (alternative to `os.path`).

```python
from pathlib import Path

p = Path("data") / "students.csv"
print(p)
print(p.name)
print(p.suffix)
print(p.parent)
print(p.exists())
```
**Output:**
```
data/students.csv
students.csv
.csv
data
False
```

---

## 19–21. Virtual Environments and pip

A **virtual environment** is an isolated Python environment so project dependencies don't conflict across projects.

```bash
python -m venv myenv          # create virtual environment
myenv\Scripts\activate         # activate (Windows)
source myenv/bin/activate      # activate (macOS/Linux)
pip install numpy pandas       # install packages inside the venv
pip freeze > requirements.txt  # save installed packages list
pip install -r requirements.txt   # install from that list (e.g. on another machine)
deactivate                     # exit the virtual environment
```

**Best practice:** Always use a virtual environment per project to avoid version conflicts between packages used by different projects.

---

## 22–24. NumPy

NumPy is the core library for numerical computing in Python, built around the fast, multi-dimensional **array** (`ndarray`).

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.shape)
print(arr.dtype)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
print(matrix.shape)

# Vectorized operations (fast, no explicit loop needed)
print(arr * 2)
print(arr + 10)
print(arr.sum())
print(arr.mean())
print(arr.max())

zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
identity = np.eye(3)
print(zeros)
print(identity)

# Slicing
print(arr[1:4])
print(matrix[:, 1])   # all rows, column index 1
```
**Output:**
```
[1 2 3 4 5]
(5,)
int64
[[1 2 3]
 [4 5 6]]
(2, 3)
[ 2  4  6  8 10]
[11 12 13 14 15]
15
3.0
5
[[0. 0. 0.]
 [0. 0. 0.]]
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
[2 3 4]
[2 5]
```

**Why NumPy over regular Python lists?** NumPy arrays are stored in contiguous memory and operations are vectorized (implemented in C), making them dramatically faster for numerical work than looping over Python lists.

---

## 25–34. Pandas

Pandas is built on top of NumPy and provides powerful, easy-to-use data structures for working with tabular ("spreadsheet-like") data.

### 26. Series

A `Series` is a one-dimensional labeled array.

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print(s)
print(s["b"])
```
**Output:**
```
a    10
b    20
c    30
d    40
dtype: int64
20
```

### 27. DataFrame

A `DataFrame` is a 2-dimensional labeled table (like a spreadsheet or SQL table) — the core Pandas structure.

```python
data = {
    "Name": ["Asha", "Ravi", "Meera"],
    "Age": [22, 25, 21],
    "City": ["Pune", "Delhi", "Mumbai"]
}
df = pd.DataFrame(data)
print(df)
print(df.head(2))
print(df["Name"])
print(df.loc[0])           # row by label/index
print(df.iloc[1])          # row by position
```
**Output:**
```
    Name  Age    City
0   Asha   22    Pune
1   Ravi   25   Delhi
2  Meera   21  Mumbai
   Name  Age   City
0  Asha   22   Pune
1  Ravi   25  Delhi
0     Asha
1     Ravi
2    Meera
Name: Name, dtype: object
Name     Asha
Age        22
City     Pune
Name: 0, dtype: object
Name      Ravi
Age         25
City     Delhi
Name: 1, dtype: object
```

### 28. Reading CSV with Pandas

```python
df = pd.read_csv("data.csv")
print(df)
print(df.shape)       # (rows, columns)
print(df.columns)
print(df.describe())  # statistical summary of numeric columns
```

### 29–30. Data Cleaning and Filtering

```python
data = {
    "Name": ["Asha", "Ravi", "Meera", "Kabir"],
    "Marks": [85, None, 90, 60]
}
df = pd.DataFrame(data)
print(df)

print(df.isnull())                       # detect missing values
df_clean = df.dropna()                    # drop rows with missing values
print(df_clean)

df_filled = df.fillna(df["Marks"].mean())  # fill missing values with the mean
print(df_filled)

# Filtering rows
high_scorers = df_filled[df_filled["Marks"] > 70]
print(high_scorers)
```
**Output (abbreviated):**
```
    Name  Marks
0   Asha   85.0
1   Ravi    NaN
2  Meera   90.0
3  Kabir   60.0

    Name  Marks
0  False  False
1  False   True
2  False  False
3  False  False

    Name  Marks
0   Asha   85.0
2  Meera   90.0
3  Kabir   60.0

    Name      Marks
0   Asha  85.000000
1   Ravi  78.333333
2  Meera  90.000000
3  Kabir  60.000000

    Name      Marks
0   Asha  85.000000
1   Ravi  78.333333
2  Meera  90.000000
```

### 31. Sorting

```python
df_sorted = df_filled.sort_values(by="Marks", ascending=False)
print(df_sorted)
```

### 32. Grouping

```python
sales = pd.DataFrame({
    "Region": ["East", "West", "East", "West"],
    "Sales": [100, 150, 200, 130]
})
grouped = sales.groupby("Region")["Sales"].sum()
print(grouped)
```
**Output:**
```
Region
East    300
West    280
Name: Sales, dtype: int64
```

### 33. Missing Values

(Covered above: `.isnull()`, `.dropna()`, `.fillna()`.)

### 34. Merging Datasets

```python
students = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Asha", "Ravi", "Meera"]})
marks = pd.DataFrame({"ID": [1, 2, 3], "Marks": [85, 72, 90]})

merged = pd.merge(students, marks, on="ID")
print(merged)
```
**Output:**
```
   ID   Name  Marks
0   1   Asha     85
1   2   Ravi     72
2   3  Meera     90
```

---

## 35–36. Matplotlib — Basic Visualization

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [200, 250, 180, 300]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("sales_chart.png")   # save instead of plt.show() in non-interactive scripts
plt.close()
```
This generates a line chart saved as `sales_chart.png`, plotting sales values against months, with axis labels and a title.

Other common chart types:
```python
plt.bar(months, sales)      # bar chart
plt.hist([1,2,2,3,3,3,4])   # histogram
plt.scatter(months, sales)  # scatter plot
plt.pie(sales, labels=months)  # pie chart
```

---

## 37–40. SQLite and Databases

SQLite is a lightweight, file-based relational database built into Python via the `sqlite3` module — no separate server needed.

```python
import sqlite3

# Connect (creates the file if it doesn't exist)
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

# Insert (CREATE)
cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Asha", 85))
cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Ravi", 72))
conn.commit()

# Read (READ)
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Update (UPDATE)
cursor.execute("UPDATE students SET marks = ? WHERE name = ?", (90, "Ravi"))
conn.commit()

# Delete (DELETE)
cursor.execute("DELETE FROM students WHERE name = ?", ("Asha",))
conn.commit()

cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

conn.close()
```
**Output:**
```
(1, 'Asha', 85)
(2, 'Ravi', 72)
[(2, 'Ravi', 90)]
```

**Security note:** Always use parameterized queries (`?` placeholders) instead of string formatting to insert values — this prevents **SQL injection** attacks.

```python
# UNSAFE — never do this:
# cursor.execute(f"SELECT * FROM students WHERE name = '{user_input}'")

# SAFE:
cursor.execute("SELECT * FROM students WHERE name = ?", (user_input,))
```

---

## 41–43. APIs and the `requests` Library

An **API** (Application Programming Interface) lets programs communicate with each other, often over HTTP. The `requests` library makes calling web APIs easy.

```python
import requests

response = requests.get("https://api.github.com/users/octocat")
print(response.status_code)     # 200 means success

data = response.json()          # parse JSON response into a Python dict
print(data["login"])
print(data["public_repos"])
```
**Sample Output:**
```
200
octocat
8
```

**POST request example:**
```python
payload = {"title": "New Post", "body": "Content here", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
print(response.status_code)
print(response.json())
```
**Sample Output:**
```
201
{'title': 'New Post', 'body': 'Content here', 'userId': 1, 'id': 101}
```

**Handling errors:**
```python
try:
    response = requests.get("https://api.example.com/data", timeout=5)
    response.raise_for_status()   # raises an error for 4xx/5xx status codes
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")
```

---

## Common Mistakes in Unit 4

1. Forgetting to close files (always prefer `with open(...) as f:`).
2. Using `"w"` mode when you meant `"a"`, accidentally erasing existing data.
3. Building SQL queries with f-strings/string concatenation — this opens the door to SQL injection. Always use parameterized queries.
4. Assuming a CSV file has no missing values — always check with `.isnull()` before analysis.
5. Forgetting `newline=""` when writing CSV files on Windows (causes extra blank lines).
6. Not handling network/API failures (timeouts, bad status codes) — always wrap API calls in `try/except`.
7. Confusing `df.loc[]` (label-based) with `df.iloc[]` (position-based) in Pandas.

## Best Practices

1. Always use `with` statements for file and database resource management.
2. Validate and clean data before analysis (`dropna()`, `fillna()`, type checks).
3. Use `.env` files or environment variables for API keys — never hardcode secrets.
4. Use `requests.get(..., timeout=...)` to avoid hanging indefinitely on a slow server.
5. Prefer Pandas' vectorized operations over manual Python loops for large datasets — much faster.
6. Keep raw data files separate from cleaned/processed data files.

---

## Practice Questions (Unit 4)

1. Write a program that reads a text file and counts the number of words in it.
2. Write a program to store student records in a CSV file and then read and display them.
3. Write a program using regex to extract all phone numbers from a block of text.
4. Write a program that fetches JSON weather data from a public API and prints the temperature.
5. Create a SQLite database of books (title, author, year) and write functions to add, update, and delete records.
6. Using Pandas, read a CSV of sales data, remove missing rows, and print the total sales grouped by region.

## Interview Questions (Unit 4)

**Q1: Why is the `with` statement preferred over manually calling `open()`/`close()`?**
A: `with` guarantees the file is closed automatically, even if an exception occurs inside the block, preventing resource leaks and ensuring data is properly flushed to disk.

**Q2: What's the difference between `json.dumps()` and `json.dump()`?**
A: `json.dumps()` converts a Python object into a JSON-formatted **string** in memory. `json.dump()` writes the JSON-formatted data directly to a **file object**.

**Q3: What is the difference between a NumPy array and a Python list?**
A: NumPy arrays are homogeneous (all elements same type), stored in contiguous memory, and support fast vectorized operations. Python lists are heterogeneous and generally slower for numerical operations because each operation runs as a Python-level loop.

**Q4: What is the difference between `df.loc[]` and `df.iloc[]` in Pandas?**
A: `.loc[]` selects rows/columns by **label** (index name). `.iloc[]` selects rows/columns by **integer position**, regardless of the label.

**Q5: How do you prevent SQL injection in Python?**
A: By using parameterized queries (placeholders like `?` or `%s`) instead of directly formatting user input into the SQL string. The database driver safely escapes the values.

**Q6: What does `response.raise_for_status()` do in the `requests` library?**
A: It raises an `HTTPError` exception if the HTTP response status code indicates an error (4xx or 5xx), which is useful for catching failed API calls early instead of silently proceeding with bad data.

**Q7: What is the difference between `.dropna()` and `.fillna()` in Pandas?**
A: `.dropna()` removes rows (or columns) that contain missing (`NaN`) values. `.fillna()` replaces missing values with a specified value (like the column mean, zero, or a placeholder), preserving the row.

---

*End of Unit 4. Continue to Unit 5 — Advanced Python, Automation, AI and Projects.*
