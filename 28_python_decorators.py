# Day 28: Python Decorators (Modifying Function Behavior)
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Advanced Python - Decorators (@decorator_name)
=====================================================
"""

# ---------------------------------------------------
# 1. Defining the Decorator Function
# ---------------------------------------------------
# A decorator takes another function as an argument,
# wraps its execution, and extends its behavior without altering original code.
def changecase(func):
    def myinner():
        # Execute the original function and modify its return value
        return func().upper()
    return myinner


# ---------------------------------------------------
# 2. Applying the Decorator
# ---------------------------------------------------
# Using the @ symbol to decorate 'myfunction'
@changecase
def myfunction():
    return "Hello Sally"


# ---------------------------------------------------
# 3. Executing the Decorated Function
# ---------------------------------------------------
print("--- Decorated Function Output ---")
print(myfunction())  # Output: HELLO SALLY


# ==========================================
# Key Takeaways:
# - Decorators allow adding extra functionality to functions dynamically.
# - The original function's source code remains untouched (Clean Code).
# - Syntax: Use '@decorator_name' directly above the function declaration.
# ==========================================
