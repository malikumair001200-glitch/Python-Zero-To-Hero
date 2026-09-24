# Day 26: Python Flexible Arguments (*args & **kwargs)
# Watch Video Tutorial: [https://www.instagram.com/reel/DdoSxHzJvKs/?stkn=MTl1c3pma3ZsbnBrag==]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Flexible Functions - Arbitrary Arguments (*args) & Keyword Arguments (**kwargs)
=====================================================
"""

# ---------------------------------------------------
# 1. Arbitrary Positional Arguments (*args)
# ---------------------------------------------------
# *args allows a function to accept any number of positional arguments.
# Python packs all incoming arguments into a Tuple.
def greet(*names):
    print("--- Greetings (*args) ---")
    for name in names:
        print("Hello", name)

# Calling the function with 3 dynamic arguments
greet("Ali", "Ahmed", "Sara")


# ---------------------------------------------------
# 2. Arbitrary Keyword Arguments (**kwargs)
# ---------------------------------------------------
# **kwargs allows a function to accept any number of key-value arguments.
# Python packs all incoming keyword arguments into a Dictionary.
def student(**details):
    print("\n--- Student Details (**kwargs) ---")
    print(details)

# Calling the function with multiple key-value pairs
student(name="Ali", age=20, city="Lahore")


# ==========================================
# Key Differences Summary:
# - *args   : Collects variable positional arguments into a Tuple.
# - **kwargs: Collects variable keyword arguments into a Dictionary.
# - Both make functions highly dynamic and flexible when input count isn't fixed.
# ==========================================
