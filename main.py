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

# main.py (update by Person1)

# If-Else Example
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
print(f"Status: {status}")

# main.py (Person1 adds additional code)

counter = 0
while counter < 3:       # While loop to print counter
    print(f"Counter: {counter}")
    counter += 1

# main.py (Person2 adds error handling)

try:
    value = int(input("Enter a number: "))  # Convert input to integer
except ValueError:
    print("That's not a valid number!")

# main.py (Person1 updates the greeting function)

def greet(user):
    # Updated greeting function with a personalized message
    return f"Welcome, {user}! We are glad to see you."

print(greet(name))