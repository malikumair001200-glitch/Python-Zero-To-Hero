# Day 31: Python Generators and Memory Efficiency (yield Keyword)
# Watch Video Tutorial: [https://www.instagram.com/reel/Dd3j1wWNhlm/?stkn=ZTkybjY3d2tlbHox]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Advanced Python - Generators & Memory Optimization
=====================================================
"""

# ---------------------------------------------------
# 1. Defining a Generator Function
# ---------------------------------------------------
# Instead of 'return', generators use 'yield' to produce values one at a time.
# Execution pauses at 'yield' and resumes on the next iteration.
def my_generator():
    yield 1
    yield 2
    yield 3


# ---------------------------------------------------
# 2. Iterating Over Generator Values
# ---------------------------------------------------
print("--- Generator Iteration Output ---")

# Python requests values sequentially without loading all elements into RAM at once
for value in my_generator():
    print(value)


# ==========================================
# Key Takeaways:
# - Generators yield items one at a time, providing lazy evaluation.
# - 'yield' pauses function state and retains local scope variables for subsequent calls.
# - Ideal for processing massive datasets, log files, or streaming data with minimal memory (RAM) usage.
# ==========================================
