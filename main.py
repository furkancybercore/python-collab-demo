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