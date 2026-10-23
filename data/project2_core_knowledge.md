# Machine Learning

## What is Machine Learning?
Machine Learning (ML) is a branch of artificial intelligence in which
computer systems learn patterns from data and use those patterns to make
predictions or decisions. A model is trained using examples rather than
being programmed with a separate rule for every possible input.

## Supervised Learning
Supervised learning uses labelled training data. Each training example
contains input features X and a known target y. The model learns a mapping
from X to y.

Example: predict student marks from hours studied.
Feature X: hours studied.
Target y: marks obtained.
A regression model predicts numerical values. A classification model
predicts categories, such as spam or not spam.

## Unsupervised Learning
Unsupervised learning works with data that has no supplied target labels.
Clustering groups similar observations. For example, a shop might group
customers by purchasing behaviour.

## Training, Validation and Testing
Training data is used to fit the model. Validation data can help select
model settings. Test data estimates performance on previously unseen
examples. Test data should not be used repeatedly to tune the model.

## Overfitting and Underfitting
Overfitting occurs when a model fits training examples too closely and
performs poorly on new data. Underfitting occurs when a model is too
simple to capture important patterns. More representative data,
regularisation, and appropriate model complexity can help.

## Common ML Metrics
For regression, mean absolute error and mean squared error measure
prediction error. For classification, accuracy, precision, recall and
F1 score are common metrics. Accuracy alone can be misleading when
classes are highly imbalanced.

## Python ML Example
from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [35, 45, 55, 65, 75]

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[6]])
print(prediction)

Here, X contains hours studied and y contains marks. The model predicts
marks for a student who studied six hours. This small artificial example
is for demonstration, not a reliable real-world prediction.

# SQL and Databases

## What is SQL?
SQL stands for Structured Query Language. It is used to create, read,
update and delete data in relational databases. A relational database
organises information into tables containing rows and columns.

## Primary Key and Foreign Key
A primary key uniquely identifies each row in a table. A foreign key
references a key in another table and can represent a relationship
between records.

## What is an SQL JOIN?
A JOIN combines related rows from two or more tables using a join
condition. For example, an Employees table may contain department_id,
while a Departments table maps department_id to department_name.

Example:
SELECT Employees.name, Departments.department_name
FROM Employees
INNER JOIN Departments
ON Employees.department_id = Departments.department_id;

INNER JOIN returns rows with matching values in both tables.
LEFT JOIN returns every row from the left table and matching rows from
the right table. When no right-side match exists, right-side columns
typically contain NULL.

## SQL Filtering and Grouping
WHERE filters rows before grouping. GROUP BY groups rows for aggregate
calculations. HAVING filters groups after aggregation. COUNT counts
rows or non-NULL values depending on the expression; SUM totals values.

Example:
SELECT department_id, COUNT(*) AS employee_count
FROM Employees
GROUP BY department_id;

## SQL Injection
SQL injection occurs when untrusted input is interpreted as part of an
SQL command. Use parameterized queries instead of concatenating user
input into SQL strings. Apply least-privilege database permissions.

# Operating Systems

## What is an Operating System?
An operating system manages computer hardware and software resources.
Its responsibilities include process management, memory management,
file management, device management and security.

## Process and Thread
A process is a running program with its own process resources and
address space. Threads are execution paths within a process and may
share that process's memory. Concurrency can introduce race conditions
when shared data is accessed without appropriate synchronisation.

## Virtual Memory and Paging
Virtual memory gives processes a virtual address space. In paging,
virtual memory is divided into fixed-size pages and physical memory
is divided into frames. A page table maps virtual pages to physical
frames, subject to the operating system's memory-management rules.

## What is a Page Fault?
A page fault occurs when a process accesses a virtual-memory page that
cannot currently be accessed through the expected valid mapping.
The operating system handles the fault. If the access is valid but the
page is not in RAM, the OS may load it from storage and update mappings.
Invalid accesses may instead result in an error or process termination.
A page fault does not always mean a program has crashed.

## Page Replacement
When physical memory has no suitable free frame, the operating system
may need to evict a page. FIFO replaces the page that has been in memory
the longest. LRU approximates replacing the page that has not been used
for the longest time. Replacement behaviour depends on the reference
string and the number of available frames.

## CPU Scheduling
FCFS runs processes in arrival order. SJF chooses a process with the
shortest expected CPU burst. Priority scheduling selects according to
priority. Round Robin gives each ready process a time quantum in turn.
Waiting time is time spent waiting in the ready queue. Turnaround time
is completion time minus arrival time.

## Deadlock
Deadlock occurs when processes wait indefinitely for resources held by
one another. The four classic necessary conditions are mutual exclusion,
hold and wait, no preemption and circular wait.

# Cybersecurity

## What is Cybersecurity?
Cybersecurity protects systems, networks, applications and data from
unauthorised access, damage and disruption. Common goals include
confidentiality, integrity and availability.

## What is Phishing?
Phishing is a social-engineering attack in which an attacker impersonates
a trusted person or organisation to trick a victim into revealing
information, opening a harmful attachment or visiting a malicious site.
Phishing can arrive by email, text message, phone call or messaging app.

## How to Reduce Phishing Risk
Check the complete sender address and destination URL. Be cautious about
unexpected urgency, threats, prizes and requests for passwords or
one-time codes. Do not open suspicious attachments or sign in through
unexpected links. Verify unusual requests using a trusted contact method.
Report suspicious messages through the appropriate organisational
process.

## Passwords and Multi-Factor Authentication
Use long, unique passwords and preferably a reputable password manager.
Multi-factor authentication adds another verification step. Never share
one-time codes with someone who contacts you unexpectedly.

## Malware and Updates
Malware includes malicious software such as ransomware, spyware and
trojans. Keep the operating system and applications updated, use
reputable security protection, maintain backups and avoid untrusted
downloads. No single control prevents every attack.

## Least Privilege and Data Protection
Give each account only the permissions it needs. Back up important data.
Encrypt sensitive data where appropriate and protect recovery credentials.
Do not place passwords, API keys or tokens directly in source code.

# Cloud Computing

## What is Cloud Computing?
Cloud computing provides computing resources such as servers, storage,
databases and software over a network, often on demand. Customers can
scale resources without owning every physical server themselves.

## Cloud Service Models
IaaS (Infrastructure as a Service) provides resources such as virtual
machines, networks and storage. The customer manages much of the
operating system and applications.

PaaS (Platform as a Service) provides a managed platform for building
and deploying applications. The provider manages more of the underlying
infrastructure.

SaaS (Software as a Service) provides ready-to-use applications through
a browser or client. The provider manages most of the application
infrastructure.

## Deployment Models
A public cloud offers services over a provider's shared infrastructure.
A private cloud is dedicated to one organisation. A hybrid cloud combines
private infrastructure with public-cloud services.

## Benefits and Risks
Cloud services can provide elasticity, rapid provisioning, managed
services and usage-based pricing. Risks include misconfiguration,
unexpected cost, service outages, vendor dependency and data exposure.
Users must still manage their own identities, permissions and data
according to the service's shared-responsibility model.

# Transformers and Large Language Models

## What is a Large Language Model?
A large language model (LLM) is a neural network trained on text or other
sequences to learn statistical patterns and predict tokens. A tokenizer
converts text into token IDs. The model processes token representations
and generates a probability distribution over possible next tokens.

## What is a Transformer?
A Transformer is a neural-network architecture that uses attention
mechanisms and feed-forward layers to process sequences. Common components
include token embeddings, positional information, attention, residual
connections, layer normalisation and feed-forward networks.

## What is Self-Attention?
Self-attention lets each token use information from other permitted tokens
in the sequence. Queries, keys and values are computed from token
representations. Query-key similarity determines attention weights, which
are used to combine value vectors.

In a decoder-only language model, causal masking prevents a position from
attending to future tokens. This supports next-token prediction.

## Training and Generation
During training, a language model learns from sequences, commonly by
predicting the next token. The training loss measures the difference
between predicted token probabilities and the correct next tokens.
During generation, the model predicts a token, appends it to the sequence,
and repeats until a stopping condition is reached.

Greedy decoding selects the highest-probability token each step.
Sampling selects from a probability distribution. Temperature changes the
sharpness of the distribution before sampling; it does not add knowledge
to the model.

## What is RAG?
Retrieval-Augmented Generation (RAG) retrieves relevant passages from an
external knowledge collection and supplies them as context to a language
model. A typical pipeline embeds documents, stores vectors, embeds a
question, retrieves relevant chunks and generates an answer grounded in
those chunks.

RAG does not automatically guarantee correctness. Poor source documents,
weak retrieval, irrelevant chunks and unsupported model claims can still
cause errors. Sources should be checked and retrieved context should
actually support the answer.

## What are Embeddings?
An embedding maps an item such as text into a numerical vector. An
embedding model is trained to place useful semantic relationships in
vector space. Similarity search compares a query vector with stored
vectors. The distance scale depends on the embedding and distance metric;
a distance value is not automatically a percentage or probability.
