# Real-Life Collaborative Git Workflow Example with Python Basics and GitHub Pull Request

This document simulates a realistic collaborative Git workflow where two developers (Person1 and Person2) work on the same repository. A key part of this workflow is using GitHub website actions to create pull requests. **After Person1 pushes its work, a pull request (PR) is created on GitHub to merge the changes into the `main` branch.** This PR must be merged so that Person2 can pull the updated and correct version of the file before starting their work.

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

Follow the steps below to simulate collaborative development with pull requests:

---

## Initial Setup

Assume the repository already exists and has a basic `main.py` file in the `main` branch. Start by cloning the repository:

```bash
git clone https://github.com/furkancybercore/python-collab-demo.git  # Clones the remote repo locally.
cd python-collab-demo                                            # Change directory to the project folder.
```

---

## Simulation Steps

### Step 1: Person1 - Initial Commit on Branch `person1`
Person1 starts work by creating a dedicated branch and adding initial Python basics.

```bash
git checkout -b person1  # Creates and switches to branch 'person1'
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
git commit -m "Person1: Add initial Python basics (variables, function, loop)"  # Commit message (-m for message)
git push -u origin person1                   # Push branch 'person1' to remote and set upstream
```

> **Note (GitHub Website Action):**
> After Person1 pushes its work, log in to GitHub and create a **Pull Request (PR)** from branch `person1` into `main`. Wait until this PR is reviewed, approved, and merged on the GitHub website. This ensures Person2 pulls the latest correct version of the code.

---

### Step 2: Person2 - Initial Commit on Branch `person2`
Before starting work, Person2 ensures they have the latest code following the PR merge.

```bash
git checkout main  # Switch to the main branch
git pull           # Update local main with the latest merged changes from GitHub
git branch person2  # Creates to branch 'person2'
git checkout person2  # Switches to branch 'person2'

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

> **Note (GitHub Website Action):**
> After Person2 pushes, a pull request should be created on GitHub from `person2` into `main`. Merge the PR to integrate Person2's changes before further work.

---

### Step 3: Person1 - First Update After Pulling
Before Person1 continues work, they pull changes from `main` (which now includes Person2's merged changes) to have the updated code.

```bash
git checkout person1    # Switch back to Person1 branch
git pull origin main    # Pull latest changes from main
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

> **Note:** After pushing, create a pull request on GitHub and merge it before any further changes from Person2.

---

### Step 4: Person1 - Second Update
Person1 continues by adding another Python concept (e.g., while loop).

```python
# main.py (Person1 adds additional code)

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

> **Note:** Again, after pushing, merge these changes via a GitHub PR so that the `main` branch stays updated.

---

### Step 5: Person2 - Second Update After Pulling
Before adding further changes, Person2 pulls the latest merged code from `main`.

```bash
git checkout person2
git pull origin main    # Update local branch with changes from main via the merged PRs
```

Person2 appends error handling to their code:
```python
# main.py (Person2 adds error handling)

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

> **Note (GitHub Website Action):**
> After pushing, create and merge a PR on GitHub to ensure `main` is updated before any further collaboration.

---

### Step 6: Person1 - Third Update After Pulling
Person1 pulls the latest changes from `main` and then refines an existing function.

```bash
git checkout person1
git pull origin main
```

Update the greeting function:
```python
# main.py (Person1 updates the greeting function)

def greet(user):
    # Updated greeting function with a personalized message
    return f"Welcome, {user}! We are glad to see you."

print(greet(name))
```

Stage, commit, and push:
```bash
git add main.py
git commit -m "Person1: Update greeting function for better user experience"
git push
```

> **Note:** As before, a pull request should be created and merged on GitHub after this push.

---

### Step 7: Person2 - Third Update After Pulling
Person2 switches back to their branch, pulls the latest merged `main` changes, then adds file operations code.

```bash
git checkout person2
git pull origin main
```

Append file operations code:
```python
# main.py (Person2 adds file operations)

# Write and Read File Example
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

> **Note:** Create a GitHub PR from `person2` and merge it after this push.

---

### Step 8: Person2 - Fourth Update
Before final integration, Person2 pulls the latest merged changes and adds another Python concept: string slicing and methods.

```bash
git pull origin main  # Ensure your branch is up to date
```

Append new code:
```python
# main.py (Person2 adds string slicing examples)

sample_text = "Git Collaboration Example"
print(sample_text[0:3])         # String slicing: prints first three characters
print(sample_text.lower().strip())  # Converts to lower case and trims whitespace
```

Stage, commit, and push:
```bash
git add main.py
git commit -m "Person2: Add string slicing and methods example"
git push
```

> **Note:** Again, create a pull request on GitHub and merge it once reviewed.

---

### Step 9: Person1 - Final Integration and Merge into `main`
Finally, Person1 ensures that the `main` branch is fully up-to-date with all the merged changes from both contributors, then performs the final merge.

```bash
git checkout main      # Switch to the main branch
git pull               # Make sure main is up to date with the latest merged PRs
git merge person1      # Merge Person1's branch into main (if any pending local changes)
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
    return f"Welcome, {user}! We are glad to see you."

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

## Summary of Collaborative Workflow Commands with GitHub Actions

| **Command**                              | **Explanation**                                                                     |
| ---------------------------------------- | ----------------------------------------------------------------------------------- |
| `git clone <url>`                      | Clones the remote repository locally.                                               |
| `git checkout -b <branch>`             | Creates and switches to a new branch.                                                |
| `git pull`                             | Fetches and merges remote changes into the current branch.                           |
| `git add <file>` or `git add .`        | Stages file changes for the next commit.                                             |
| `git commit -m "message"`               | Commits the staged changes with a descriptive message (-m means "message").           |
| `git push -u origin <branch>`          | Pushes the branch to the remote repository and sets up upstream tracking.             |
| `git merge <branch>`                   | Merges two branches (typically, a feature branch into main).                          |

**GitHub Website Actions:**
- **Pull Requests (PR):** After a push, go to the GitHub website, create a PR for the branch (e.g., Person1’s or Person2’s branch) to merge into `main`.
- **Code Review & Merge:** Get the code reviewed, then merge the PR into `main` on GitHub.
- **Sync Work:** Other developers should pull the latest merged changes from `main` to ensure they are working on the most updated code.

Happy Coding and Collaborating!