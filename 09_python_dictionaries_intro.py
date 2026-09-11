# Day 09: Introduction to Python Dictionaries
# Watch Video Tutorial: [https://www.instagram.com/reel/DdJU_u_tfaQ/?stkn=MTJxeTFsc25kbXZlbQ==]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Python Dictionaries (Key:Value Pairs & Access)
=====================================================
"""

# 1. Creating a Dictionary
# Dictionaries store data in key:value pairs using curly braces {}
student = {
    "name": "Ali",
    "age": 20,
    "city": "Lahore"
}

print("--- Entire Dictionary ---")
print(student)
# Output: {'name': 'Ali', 'age': 20, 'city': 'Lahore'}


# 2. Accessing Items by Key
# Retrieve values directly using their corresponding keys inside square brackets []
print("\n--- Accessing Specific Value ---")
print("Student Name:", student["name"])
# Output: Ali


# ==========================================
# Key Characteristics of Dictionaries:
# - Ordered: As of Python 3.7+, dictionaries maintain insertion order.
# - Key:Value Pairs: Every item is associated with a unique key.
# - No Duplicate Keys: Dictionary keys must be unique.
# - Fast Access: Values can be accessed directly via keys instead of numeric indexes.
# ==========================================
