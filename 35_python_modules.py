# Day 35: Python Modules (Code Organization & Reusability)
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Modular Programming - Python Modules
=====================================================
"""

# ---------------------------------------------------
# 1. Module Definition Concept
# ---------------------------------------------------
# A module is a file containing Python definitions, functions, and statements.
# Example: Assume a separate file named 'mymodule.py' containing:
#
# def greeting(name):
#     print("Hello, " + name)


# ---------------------------------------------------
# 2. Importing and Executing Module Functions
# ---------------------------------------------------
# You can import custom modules or built-in modules using the 'import' keyword.
# Importing standard math module as a demonstration of built-in module usage:
import math

print("--- Module Usage Example ---")
# Accessing function inside module using dot notation (module_name.function_name)
print("Square Root using math module:", math.sqrt(16))  # Output: 4.0


# ---------------------------------------------------
# 3. Custom Module Execution Simulation
# ---------------------------------------------------
# Simulating mymodule.greeting("Jonathan") call:
def greeting(name):
    print("Hello, " + name)

print("\n--- Custom Function Call ---")
greeting("Jonathan")  # Output: Hello, Jonathan


# ==========================================
# Key Takeaways:
# - A module is simply a Python file (.py) containing reusable code.
# - Use the 'import' keyword to bring code from one file into another.
# - Modular code improves maintainability, readability, and reusability.
# ==========================================
