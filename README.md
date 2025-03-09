# Real-Life Collaborative Git Workflow Example with Python Basics

This document simulates a realistic collaborative Git workflow where two developers (Person1 and Person2) are working on the same repository. One key aspect is that **each person pulls the updated code (from `main`) before starting new work**. This ensures that each contributor works on the latest version of the project and minimizes merge conflicts.

There are **nine steps** in our simulation with the following order of operations:
1. Person1
2. Person2
3. Person1
4. Person1
5. Person2
6. Person1
7. Person2
8. Person2
9. Person1

The repository details are:
- **Project Name**: `python-collab-demo`
- **Repository URL**: [https://github.com/furkancybercore/python-collab-demo.git](https://github.com/furkancybercore/python-collab-demo.git)
- **Branches**: `main`, `person1`, `person2`

Follow the steps below to simulate collaborative development:

---

## Initial Setup

Assume the repository already exists and has a basic `main.py` file in the `main` branch. Begin by cloning the repository:

```bash
git clone https://github.com/furkancybercore/python-collab-demo.git  # Clone the remote repo locally.
git cd python-collab-demo                                      # Navigate into the project folder.
```

---

## Simulation Steps

### Step 1: Person1 - Initial Commit on Branch `person1`
Person1 starts work by creating a dedicated branch and adding initial Python basics.

```bash
git checkout -b person1  # Create and switch to branch 'person1'
```

Update `main.py` with initial Python code:
```python
# main.py (Person1's initial code)

# Basic Variables and Function
name = "Alice"              # String variable
age = 30                    # Integer variable

def greet(user):          # Function to greet a user
    return f"Hello, {user}!"

print(greet(name))

# Basic Loop Example
for i in range(3):        # Loop to print numbers 0 to 2
    print(f"Count: {i}")
```

Stage, commit, and push:
```bash
git add main.py                              # Stage changes in main.py
git commit -m "Person1: Add initial Python basics (variables, function, loop)"  # Commit with a message (-m for message)
git push -u origin person1                   # Push branch 'person1' to remote and set upstream
```

---

### Step 2: Person2 - Initial Commit on Branch `person2`
Before starting work, Person2 ensures they have the latest code from `main`.

```bash
git checkout main  # Switch to the main branch
git pull           # Update local main with the latest remote changes
git checkout -b person2  # Create and switch to branch 'person2'
```

Person2 adds new Python content (e.g., dictionaries and sets):
```python
# main.py (Person2's addition)

# Dictionaries and Set Operations
person_info = {
    "name": "Bob",
    "country": "Turkey"
}

unique_numbers = {1, 2, 3, 2, 1}  # Sets automatically remove duplicates
unique_numbers.add(4)
print(f"Person Info: {person_info}")
print(f"Unique Numbers: {unique_numbers}")
```

Stage, commit, and push:
```bash
git add main.py
git commit -m "Person2: Add dictionary and set examples"  # Commit message explaining the change
git push -u origin person2
```

---

### Step 3: Person1 - First Update After Pulling
Before Person1 continues work, they pull changes from `main` to include Person2's updates.

```bash
git checkout person1    # Switch back to Person1 branch
git pull origin main    # Pull latest changes from main (simulate integration)
```

Append new code (e.g., if-else logic):
```python
# main.py (update by Person1)

# If-Else Example
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
print(f"Status: {status}")
```

Stage, commit, and push:
```bash
git add main.py
git commit -m "Person1: Add if-else example for age verification"
git push
```

---

### Step 4: Person1 - Second Update
Person1 adds another Python concept (e.g., while loop).

```python
# main.py (Person1 adds additional logic)

counter = 0
while counter < 3:       # While loop to print counter
    print(f"Counter: {counter}")
    counter += 1
```

Stage, commit, and push:
```bash
git add main.py
git commit -m "Person1: Add while loop to print counter values"
git push
```

---

### Step 5: Person2 - Second Update After Pulling
Person2 pulls the latest main to incorporate Person1's updates before adding new content.

```bash
git checkout person2
git pull origin main    # Update local branch with changes from main
```

Person2 appends error handling to their code:
```python
# main.py (Person2 appends error handling)

try:
    value = int(input("Enter a number: "))  # Convert input to integer
except ValueError:
    print("That's not a valid number!")
```

Stage, commit, and push:
```bash
git add main.py
git commit -m "Person2: Add error handling for user input"
git push
```

---

### Step 6: Person1 - Third Update After Pulling
Person1 pulls updated changes and continues by refining an existing function.

```bash
git checkout person1
git pull origin main
```

Person1 updates the greeting function for improved clarity:
```python
# main.py (Person1 updates the greeting function)

def greet(user):
    # Updated greeting function with a personalized message
    return f"Welcome, {user}! Glad to have you here."

print(greet(name))
```

Stage, commit, and push:
```bash
git add main.py
git commit -m "Person1: Update greeting function for better UX"
git push
```

---

### Step 7: Person2 - Third Update After Pulling
Person2 pulls the latest changes to avoid conflicts, then adds a file operations example.

```bash
git checkout person2
git pull origin main
```

Append new file operations code:
```python
# main.py (Person2 adds file operations)

# Simple File Write and Read Example
with open("sample.txt", "w") as f:
    f.write("Hello from Person2!")

try:
    with open("sample.txt", "r") as f:
        content = f.read()
    print(f"File Content: {content}")
except FileNotFoundError:
    print("File not found!")
```

Stage, commit, and push:
```bash
git add main.py
git commit -m "Person2: Add file operations example (write & read)"
git push
```

---

### Step 8: Person2 - Fourth Update
Before final integration, Person2 adds another Python concept: string slicing and methods.

```python
# main.py (Person2 adds string slicing examples)

sample_text = "Git Collaboration Example"
print(sample_text[0:3])         # String slicing: prints first three characters
print(sample_text.lower().strip())  # Convert to lower case and remove whitespace
```

Stage, commit, and push:
```bash
git add main.py
git commit -m "Person2: Add string slicing and methods example"
git push
```

---

### Step 9: Person1 - Final Integration and Merge into `main`
Person1 now pulls the latest changes, merges both branches back to `main`, and pushes the integrated code.

```bash
git checkout main      # Switch to the main branch
git pull               # Ensure main is up to date with remote changes
git merge person1      # Merge Person1's branch into main
git merge person2      # Merge Person2's branch into main
git push origin main   # Push the updated main branch to remote
```

---

## Final `main.py` Content After Merging

Below is a sample of what the integrated `main.py` file might look like after all merges:

```python
# main.py - Final Integrated Version

# -------------------------------
# Person1's Contributions
# -------------------------------
name = "Alice"
age = 30

def greet(user):
    # Updated greeting function with a personalized message
    return f"Welcome, {user}! Glad to have you here."

print(greet(name))

# Basic Loop Example
for i in range(3):
    print(f"Count: {i}")

# If-Else Example
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
print(f"Status: {status}")

counter = 0
while counter < 3:
    print(f"Counter: {counter}")
    counter += 1

# -------------------------------
# Person2's Contributions
# -------------------------------
person_info = {
    "name": "Bob",
    "country": "Turkey"
}

unique_numbers = {1, 2, 3, 2, 1}
unique_numbers.add(4)
print(f"Person Info: {person_info}")
print(f"Unique Numbers: {unique_numbers}")

try:
    value = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")

# File Operations Example
with open("sample.txt", "w") as f:
    f.write("Hello from Person2!")

try:
    with open("sample.txt", "r") as f:
        content = f.read()
    print(f"File Content: {content}")
except FileNotFoundError:
    print("File not found!")

# String Slicing and Methods
sample_text = "Git Collaboration Example"
print(sample_text[0:3])  # Prints 'Git'
print(sample_text.lower().strip())
```

---

## Summary of Collaborative Workflow Commands

| **Command**                              | **Explanation**                                                                     |
| ---------------------------------------- | ----------------------------------------------------------------------------------- |
| `git clone <url>`                      | Clones the remote repository locally.                                               |
| `git checkout -b <branch>`             | Creates and switches to a new branch.                                                |
| `git pull`                             | Fetches and merges remote changes into the current branch.                           |
| `git add <file>` or `git add .`       | Stages file changes for the next commit.                                             |
| `git commit -m "message"`               | Commits the staged changes with a descriptive message (`-m` for message).            |
| `git push -u origin <branch>`          | Pushes the branch to the remote repository and sets the upstream tracking branch.     |
| `git merge <branch>`                   | Merges specified branch changes into the current branch.                              |

**Note:** This simulation represents a real-life scenario where developers always pull changes from the main branch before starting new work, commit their changes, and then merge all contributions into the main branch.

Happy Coding!
