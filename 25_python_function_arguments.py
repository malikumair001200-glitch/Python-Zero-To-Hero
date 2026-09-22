# Day 25: Python Function Arguments and Parameters
# Watch Video Tutorial: [https://www.instagram.com/reel/DdlHw8vNuuN/?stkn=MWZrNmVxdmVjZm40dQ==]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Reusable Code - Parameters vs. Arguments
=====================================================
"""

# ---------------------------------------------------
# 1. Single Parameter & Argument Example
# ---------------------------------------------------
# 'name' is the parameter (placeholder for dynamic input)
def greet(name):
    print("Hello", name)

print("--- Dynamic Greeting Execution ---")
# Passing "Ali" and "Ahmed" as arguments to the same function
greet("Ali")
greet("Ahmed")


# ---------------------------------------------------
# 2. Multiple Parameters & Positional Arguments
# ---------------------------------------------------
# Function expecting two parameters: 'name' and 'age'
def student(name, age):
    print(f"Student Name: {name}, Age: {age}")

print("\n--- Multiple Arguments Execution ---")
student("Ali", 20)


# ---------------------------------------------------
# 3. Parameter Mismatch Error Handling (Note)
# ---------------------------------------------------
# Executing student("Ali") without passing the second required argument ('age')
# will raise a TypeError: student() missing 1 required positional argument: 'age'


# ==========================================
# Key Takeaways:
# - Parameters are variables listed in the function definition.
# - Arguments are the real values passed to the function during execution.
# - The number of arguments passed must match the number of expected parameters.
# ==========================================
