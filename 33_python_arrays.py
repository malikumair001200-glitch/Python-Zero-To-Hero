# Day 33: Python Arrays (Using Lists to Store Multiple Values)
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Data Structures - Working with Arrays (Lists)
=====================================================
"""

# ---------------------------------------------------
# 1. Defining an Array (List in Python)
# ---------------------------------------------------
# Storing multiple values in a single variable
cars = ["Ford", "Volvo", "BMW"]

print("--- Initial Array ---")
print(cars)


# ---------------------------------------------------
# 2. Accessing Items by Index
# ---------------------------------------------------
# Python uses zero-based indexing (0 is the first item)
first_car = cars[0]

print("\n--- Access Item ---")
print("First Car (Index 0):", first_car)  # Output: Ford


# ---------------------------------------------------
# 3. Modifying an Existing Value
# ---------------------------------------------------
# Reassigning a new value using the specific index
cars[0] = "Toyota"

print("\n--- After Modifying Index 0 ---")
print(cars)  # Output: ['Toyota', 'Volvo', 'BMW']


# ---------------------------------------------------
# 4. Adding New Elements
# ---------------------------------------------------
# Using append() method to add an item to the end of the array
cars.append("Honda")

print("\n--- After Appending New Element ---")
print(cars)  # Output: ['Toyota', 'Volvo', 'BMW', 'Honda']


# ==========================================
# Key Takeaways:
# - Python does not have built-in support for native Arrays; Lists are commonly used as Arrays.
# - Zero-based Indexing: Access elements instantly using their positions (e.g., list[0]).
# - Mutability: Modify existing values directly or append new ones dynamically using .append().
# ==========================================
