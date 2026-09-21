# Day 24: Python Functions (Def, Calling, and Return Values)
# Watch Video Tutorial: [https://www.instagram.com/reel/Ddi1AmqtX8s/?stkn=OXlsenl0b3pta3Br]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Reusable Code - Functions & Return Statements
=====================================================
"""

# ---------------------------------------------------
# 1. Defining and Calling a Function
# ---------------------------------------------------
# 'def' keyword is used to define a function named 'greet'
def greet():
    print("Hello!")

print("--- Function Execution ---")
# The code inside the function runs only when called
greet()
greet()
greet()


# ---------------------------------------------------
# 2. Function with Return Value
# ---------------------------------------------------
# Functions can process data and send results back using 'return'
def add():
    return 10 + 20

# Capturing the returned value into a variable
result = add()

print("\n--- Return Value Check ---")
print("Result of add function:", result)


# ==========================================
# Key Takeaways:
# - Functions allow write-once, run-many code reusability.
# - Defining a function ('def') does not execute it until called.
# - The 'return' keyword sends data back to the caller.
# ==========================================
