# UNIT 5 — ADVANCED PYTHON, AUTOMATION, AI AND PROJECTS

This unit is a self-contained knowledge base chapter covering closures, decorators, context managers, type hints, dataclasses, logging, testing, concurrency, web basics, machine learning, and RAG concepts.

---

## 1–3. Advanced Functions, Closures, Decorators

### 2. Closures

A closure is a function that "remembers" variables from its enclosing scope even after that outer function has finished running.

```python
def make_multiplier(factor):
    def multiply(number):
        return number * factor    # 'factor' is remembered from the outer scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))
```
**Output:**
```
10
15
```
Here, `multiply` is a closure — it "closes over" the variable `factor` from `make_multiplier`'s scope.

### 3. Decorators

A decorator is a function that wraps another function to add extra behavior without modifying its original code.

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

print(slow_function())
```
**Output (approximate):**
```
slow_function took 1.0002 seconds
Done
```

`@timer` above `def slow_function():` is equivalent to writing `slow_function = timer(slow_function)`.

**Decorator with arguments passed through:**
```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def add(a, b):
    return a + b

print(add(3, 4))
```
**Output:**
```
Calling add with args=(3, 4), kwargs={}
7
```

**Real-world uses of decorators:** logging, timing, authentication checks, caching (`functools.lru_cache`), input validation.

---

## 4–5. Context Managers

A context manager handles setup and cleanup automatically using the `with` statement (like automatically closing files, covered in Unit 4).

### 5. Custom Context Managers

**Method 1: Using a class**
```python
class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print("File closed automatically")

with FileOpener("test.txt", "w") as f:
    f.write("Hello from custom context manager")
```
**Output:**
```
File closed automatically
```

**Method 2: Using `contextlib`**
```python
from contextlib import contextmanager

@contextmanager
def timer_context():
    import time
    start = time.time()
    yield                      # code inside the 'with' block runs here
    print(f"Elapsed: {time.time() - start:.4f}s")

with timer_context():
    total = sum(range(1000000))
```
**Sample Output:**
```
Elapsed: 0.0234s
```

---

## 6. Advanced Generators

Generators can also receive values, delegate to other generators (`yield from`), and be combined in pipelines.

```python
def read_large_data():
    for i in range(5):
        yield f"record_{i}"

def process(records):
    for record in records:
        yield record.upper()

for item in process(read_large_data()):
    print(item)
```
**Output:**
```
RECORD_0
RECORD_1
RECORD_2
RECORD_3
RECORD_4
```

`yield from` delegates to a sub-generator:
```python
def inner():
    yield 1
    yield 2

def outer():
    yield from inner()
    yield 3

print(list(outer()))
```
**Output:**
```
[1, 2, 3]
```

---

## 7. Type Hints

Type hints document expected argument/return types. Python does **not** enforce them at runtime (they're for readability and tools like `mypy`).

```python
def greet(name: str, age: int) -> str:
    return f"{name} is {age} years old"

print(greet("Asha", 22))

from typing import List, Dict, Optional

def average(nums: List[float]) -> float:
    return sum(nums) / len(nums)

def get_user(user_id: int) -> Optional[Dict[str, str]]:
    users = {1: {"name": "Asha"}}
    return users.get(user_id)   # returns None if not found

print(average([1.0, 2.0, 3.0]))
print(get_user(1))
print(get_user(99))
```
**Output:**
```
Asha is 22 years old
2.0
{'name': 'Asha'}
None
```

---

## 8. dataclasses

`@dataclass` automatically generates `__init__`, `__repr__`, and `__eq__` for classes that mainly hold data.

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    marks: float = 0.0    # default value

s1 = Student("Asha", 22, 88.5)
s2 = Student("Asha", 22, 88.5)

print(s1)             # auto-generated __repr__
print(s1 == s2)        # auto-generated __eq__
```
**Output:**
```
Student(name='Asha', age=22, marks=88.5)
True
```
Without `@dataclass`, you'd have to write `__init__`, `__repr__`, and `__eq__` by hand.

---

## 9. Enums

`Enum` creates a set of named constants, improving readability over "magic" strings/numbers.

```python
from enum import Enum

class Status(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3

order_status = Status.APPROVED
print(order_status)
print(order_status.name, order_status.value)

if order_status == Status.APPROVED:
    print("Order has been approved")
```
**Output:**
```
Status.APPROVED
APPROVED 2
Order has been approved
```

---

## 10. Logging

`logging` is preferred over `print()` for production code — it supports severity levels, timestamps, and output to files.

```python
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("Debug message (won't show, below INFO level)")
logging.info("Application started")
logging.warning("Low disk space")
logging.error("Failed to connect to database")
```
**Sample Output:**
```
2026-08-08 10:20:15,123 - INFO - Application started
2026-08-08 10:20:15,124 - WARNING - Low disk space
2026-08-08 10:20:15,125 - ERROR - Failed to connect to database
```

**Logging levels (low to high severity):** `DEBUG` < `INFO` < `WARNING` < `ERROR` < `CRITICAL`.

---

## 11–12. Unit Testing and pytest

Automated tests verify code correctness and catch regressions.

**Using built-in `unittest`:**
```python
import unittest

def add(a, b):
    return a + b

class TestMathFunctions(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

if __name__ == "__main__":
    unittest.main()
```

**Using `pytest` (simpler syntax, widely used in industry):**
```python
# test_calculator.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```
Run with: `pytest test_calculator.py`
**Sample Output:**
```
============= test session starts =============
test_calculator.py .                      [100%]
============== 1 passed in 0.01s ==============
```

**Best practice:** Name test files `test_*.py` and test functions `test_*` so pytest auto-discovers them.

---

## 13–17. Concurrency: Multithreading, Multiprocessing, asyncio

### 13. Multithreading

Useful for **I/O-bound** tasks (waiting on network/disk), since Python's Global Interpreter Lock (GIL) limits true parallel CPU execution across threads.

```python
import threading
import time

def download(name):
    print(f"Starting {name}")
    time.sleep(1)
    print(f"Finished {name}")

threads = [threading.Thread(target=download, args=(f"file{i}",)) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("All downloads complete")
```
**Sample Output:**
```
Starting file0
Starting file1
Starting file2
Finished file0
Finished file1
Finished file2
All downloads complete
```
All three "downloads" run concurrently (roughly 1 second total, not 3), because they overlap while waiting.

### 14. multiprocessing

Useful for **CPU-bound** tasks (heavy computation), since it uses separate processes (each with its own Python interpreter and memory), bypassing the GIL.

```python
from multiprocessing import Process

def square_numbers():
    result = [i * i for i in range(1000000)]

if __name__ == "__main__":
    processes = [Process(target=square_numbers) for _ in range(4)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print("All processes complete")
```
**Output:**
```
All processes complete
```

### 15–16. asyncio / Asynchronous Programming

`asyncio` allows a single thread to handle many I/O-bound tasks concurrently using `async`/`await`, without the overhead of threads.

```python
import asyncio

async def fetch_data(name, delay):
    print(f"Start fetching {name}")
    await asyncio.sleep(delay)     # simulates a non-blocking I/O wait
    print(f"Finished fetching {name}")
    return f"{name} data"

async def main():
    results = await asyncio.gather(
        fetch_data("A", 2),
        fetch_data("B", 1),
        fetch_data("C", 3)
    )
    print(results)

asyncio.run(main())
```
**Output:**
```
Start fetching A
Start fetching B
Start fetching C
Finished fetching B
Finished fetching A
Finished fetching C
['A data', 'B data', 'C data']
```
All three tasks run concurrently; total time is about 3 seconds (the longest task), not 6 (the sum).

### 17. Choosing a Concurrency Model

| Task type | Best approach |
|---|---|
| I/O-bound (network, file, API calls) | `asyncio` or threading |
| CPU-bound (heavy computation) | `multiprocessing` |
| Simple I/O parallelism, easier to reason about | threading |

---

## 18. Web Scraping Concepts

Web scraping extracts data from websites automatically. Common tools: `requests` (fetch HTML) + `BeautifulSoup` (parse HTML).

```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com")
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("h1").text
links = [a["href"] for a in soup.find_all("a")]
print(title)
print(links)
```

**Best practice / ethics:** Always check a website's `robots.txt` and terms of service before scraping, avoid overwhelming servers with requests, and prefer official APIs when available.

---

## 19–21. Automation, Environment Variables, Configuration

```python
import os

# Reading environment variables (never hardcode secrets in code)
api_key = os.environ.get("API_KEY", "default_value")
print(api_key)
```

Automation example — renaming all `.txt` files in a folder:
```python
import os

folder = "documents"
for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        new_name = filename.replace(" ", "_")
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
print("Renaming complete")
```

**Best practice:** Store secrets (API keys, passwords) in environment variables or a `.env` file (loaded via the `python-dotenv` package), never directly in source code.

---

## 22–25. REST APIs, Flask, FastAPI, Backend Concepts

### 23. Flask — Minimal Example

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the API"

@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.get_json()
    result = data["a"] + data["b"]
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
```
Running this starts a local web server; sending a POST request to `/add` with JSON `{"a": 2, "b": 3}` returns `{"result": 5}`.

### 24. FastAPI — Minimal Example

FastAPI is a modern framework known for speed and automatic interactive API documentation.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    a: int
    b: int

@app.get("/")
def home():
    return {"message": "Welcome to the API"}

@app.post("/add")
def add_numbers(numbers: Numbers):
    return {"result": numbers.a + numbers.b}
```
Run with: `uvicorn main:app --reload`. FastAPI automatically validates request data types (using the `Numbers` model) and generates interactive docs at `/docs`.

### 25. REST API Concepts

| HTTP Method | Purpose |
|---|---|
| `GET` | Retrieve data |
| `POST` | Create new data |
| `PUT` / `PATCH` | Update existing data |
| `DELETE` | Remove data |

REST APIs are **stateless** — each request contains all information needed; the server doesn't remember previous requests.

---

## 26–29. Machine Learning with Python (scikit-learn)

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample data: hours studied vs marks scored
X = [[1], [2], [3], [4], [5]]     # feature: hours studied
y = [35, 45, 55, 65, 75]           # target: marks scored

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)             # training the model

predictions = model.predict(X_test)
print("Predictions:", predictions)

mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

print("Predicted marks for 6 hours studied:", model.predict([[6]]))
```
**Sample Output:**
```
Predictions: [75.]
Mean Squared Error: 0.0
Predicted marks for 6 hours studied: [85.]
```

**Key ML terms:**
- **Feature (X):** input variable(s) used to make a prediction.
- **Target (y):** the value being predicted.
- **Training:** the model learns patterns from `X_train`/`y_train`.
- **Testing/evaluation:** checking performance on unseen data (`X_test`/`y_test`).
- **Overfitting:** model memorizes training data but performs poorly on new data.

---

## 30–33. Introduction to Deep Learning and PyTorch

Deep learning uses **neural networks** — layers of interconnected nodes that learn patterns from data, especially effective for images, text, and audio.

```python
import torch
import torch.nn as nn

# A tensor is PyTorch's core data structure (like a NumPy array, but supports GPU + autograd)
x = torch.tensor([1.0, 2.0, 3.0])
print(x)
print(x.shape)

# A minimal neural network with one linear layer
class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)   # 1 input feature -> 1 output

    def forward(self, x):
        return self.linear(x)

model = SimpleNet()
sample_input = torch.tensor([[2.0]])
output = model(sample_input)
print(output)
```
**Sample Output:**
```
tensor([1., 2., 3.])
torch.Size([3])
tensor([[0.8452]], grad_fn=<AddmmBackward0>)
```
(The exact output number varies because the network's weights are randomly initialized.)

**Key concepts:**
- **Tensor:** a multi-dimensional array, PyTorch's fundamental data structure.
- **Layer:** a transformation applied to data (e.g., `nn.Linear`).
- **Forward pass:** computing output from input through the network.
- **Backpropagation/autograd:** automatically computing gradients to update weights during training.

---

## 34–38. Python for AI, LLM Applications, Embeddings, and RAG

### 36. Embeddings

An **embedding** is a numeric vector representation of text (or other data) that captures semantic meaning — similar meanings produce vectors that are close together in vector space.

```python
# Conceptual example (actual embedding models require an API or local model)
# text -> embedding vector
"cat"  -> [0.12, -0.45, 0.98, ...]
"kitten" -> [0.14, -0.42, 0.95, ...]   # close to "cat" — similar meaning
"car"  -> [-0.80, 0.33, 0.02, ...]     # far from "cat" — different meaning
```

Cosine similarity is commonly used to measure how close two embeddings are:
```python
import numpy as np

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

vec1 = [1, 2, 3]
vec2 = [1, 2, 3.5]
print(cosine_similarity(vec1, vec2))
```
**Output:**
```
0.9987...
```

### 37–38. RAG Concepts and Building a Simple RAG Application

**RAG (Retrieval-Augmented Generation)** combines two steps:
1. **Retrieval** — search a knowledge base (like this document!) for the most relevant chunks of text given a user's question, typically using embedding similarity.
2. **Generation** — pass the retrieved chunks + the user's question to a language model, which generates an answer grounded in that retrieved content.

**Why RAG?** Language models have a fixed training cutoff and can "hallucinate" facts. RAG lets them answer accurately from up-to-date or domain-specific documents (like this Python knowledge base) without retraining the model.

**Simplified RAG pipeline (conceptual code):**
```python
# Step 1: Split documents into chunks
def chunk_text(text, chunk_size=200):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

# Step 2: Convert chunks into embeddings (using an embedding model/API)
# embeddings = [get_embedding(chunk) for chunk in chunks]

# Step 3: Given a user question, embed it and find the most similar chunk(s)
def find_best_chunk(question_embedding, chunk_embeddings, chunks):
    similarities = [cosine_similarity(question_embedding, emb) for emb in chunk_embeddings]
    best_index = similarities.index(max(similarities))
    return chunks[best_index]

# Step 4: Pass the best-matching chunk + question to a language model to generate the final answer
# answer = call_llm(prompt=f"Context: {best_chunk}\n\nQuestion: {question}")
```

**Core building blocks of a RAG system:**
- **Document loader** — reads source files (PDF, markdown, text).
- **Chunker** — splits documents into manageable pieces.
- **Embedding model** — converts text chunks into vectors.
- **Vector store** — a database optimized for similarity search (e.g., FAISS, Chroma, Pinecone).
- **Retriever** — finds the most relevant chunks for a given query.
- **LLM** — generates the final answer using retrieved context.

*(This knowledge base itself is structured with clear headings and self-contained sections specifically so it can serve as the document source for a RAG pipeline like this.)*

---

## 39–45. Project Architecture and Professional Practices

### 40. Professional Python Project Structure

```
my_project/
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── tests/
│   ├── test_main.py
├── data/
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

### 41. Git and Python Projects

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <repo_url>
git push -u origin main
```
**Best practice:** Add a `.gitignore` to exclude `__pycache__/`, `venv/`, `.env`, and other generated/sensitive files from version control.

### 42. requirements.txt

Lists all packages a project depends on, so others (or deployment systems) can recreate the same environment.

```
flask==3.0.0
pandas==2.2.0
requests==2.31.0
numpy==1.26.0
```
Install all at once with: `pip install -r requirements.txt`

### 44. Debugging and Optimization

- Profile code with `time` or the `cProfile` module to find slow sections before optimizing.
- Prefer built-in functions and vectorized operations (NumPy/Pandas) over manual Python loops for performance.
- Cache expensive repeated computations with `functools.lru_cache`.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def expensive_calculation(n):
    return sum(i*i for i in range(n))

print(expensive_calculation(1000000))   # slow the first time
print(expensive_calculation(1000000))   # instant — cached result
```

### 45. Security Best Practices

1. Never hardcode API keys, passwords, or secrets in source code — use environment variables.
2. Always use parameterized SQL queries to prevent injection.
3. Validate and sanitize all user input.
4. Keep dependencies up to date to avoid known vulnerabilities.
5. Use HTTPS for any network communication involving sensitive data.
6. Don't log sensitive information (passwords, tokens) in plain text.

---

## Common Mistakes in Unit 5

1. Forgetting `functools.wraps` in decorators, which loses the original function's name/docstring (use `@functools.wraps(func)` on the wrapper).
2. Using threading for CPU-bound work — the GIL prevents true parallel speedup; use multiprocessing instead.
3. Forgetting `await` before an async call, which returns a coroutine object instead of the actual result.
4. Treating type hints as runtime type enforcement — Python does not check them by default.
5. Hardcoding secrets/API keys directly in code that gets pushed to version control.
6. Building a RAG system without properly chunking documents, causing poor retrieval accuracy.

## Best Practices

1. Use `async`/`multiprocessing`/`threading` appropriately based on whether the task is I/O-bound or CPU-bound.
2. Write unit tests for critical logic before deploying.
3. Use logging instead of `print()` for anything beyond quick debugging.
4. Structure projects consistently (`src/`, `tests/`, `requirements.txt`, `README.md`).
5. For RAG systems, keep document chunks focused and self-contained (as done throughout this knowledge base) to improve retrieval quality.
6. Version-control everything except secrets and generated files.

---

## Practice Questions (Unit 5)

1. Write a decorator that logs how many times a function has been called.
2. Write a custom context manager that measures and prints memory/time usage of a code block.
3. Write an async program that fetches data from three different (simulated) sources concurrently.
4. Use `@dataclass` to model a `Product` with `name`, `price`, and `in_stock` fields.
5. Build a minimal Flask API with one `GET` and one `POST` endpoint.
6. Train a simple linear regression model using scikit-learn on a small custom dataset.
7. Explain, in your own words, the steps you would take to build a RAG assistant over a folder of PDF files.

## Interview Questions (Unit 5)

**Q1: What is a closure, and why is it useful?**
A: A closure is a function that captures and remembers variables from its enclosing scope, even after that outer function has returned. It's useful for creating factory functions, maintaining state without classes, and implementing decorators.

**Q2: What is a decorator, and give a real-world use case.**
A: A decorator is a function that wraps another function to add behavior without modifying its source code. Common uses include logging, timing, authentication/permission checks, and caching (e.g., `functools.lru_cache`).

**Q3: What is the difference between multithreading and multiprocessing?**
A: Multithreading runs multiple threads within a single process, sharing memory — good for I/O-bound tasks, but limited for CPU-bound tasks by Python's GIL. Multiprocessing runs separate processes, each with its own memory and interpreter, enabling true parallelism for CPU-bound tasks.

**Q4: What problem does asyncio solve?**
A: It allows a program to handle many I/O-bound operations (like network requests) concurrently on a single thread, without the overhead of creating multiple threads or processes, by cooperatively pausing/resuming tasks with `await`.

**Q5: What are type hints, and does Python enforce them?**
A: Type hints are annotations that indicate expected variable/parameter/return types (e.g., `def f(x: int) -> str`). Python does not enforce them at runtime by default — they're primarily for documentation and static analysis tools like `mypy`.

**Q6: What is RAG (Retrieval-Augmented Generation) and why is it useful?**
A: RAG is an approach where a language model's answer is grounded by first retrieving relevant chunks of text from an external knowledge base (using embedding similarity search), then generating a response using both the retrieved context and the user's question. It reduces hallucination and allows the model to answer accurately about information outside its training data or specific to a domain (like this Python knowledge base).

**Q7: What is an embedding?**
A: A numeric vector representation of data (commonly text) that captures semantic meaning, such that similar items have vectors that are close together in vector space, typically measured with cosine similarity.

**Q8: What is the difference between Flask and FastAPI?**
A: Flask is a lightweight, flexible web framework with a simple, minimal core. FastAPI is a newer framework built for speed, with built-in data validation (via Pydantic), automatic interactive API documentation, and native support for asynchronous request handling.

**Q9: Why should secrets not be hardcoded in source code?**
A: Hardcoded secrets can be exposed if the code is shared, pushed to a public repository, or leaked, creating serious security risks. Storing them in environment variables or `.env` files (excluded from version control) keeps them separate from code and easier to rotate/manage securely.

---

*End of Unit 5. All 5 units are now complete. Continue to the Coding Problems Section, Project Section, and the 150+ Interview Questions Bank.*
