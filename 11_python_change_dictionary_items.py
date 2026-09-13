# Day 11: Changing Dictionary Items in Python
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Modifying/Updating Dictionary Values
Note: Dictionaries are mutable, meaning values can be updated directly.
=====================================================
"""

# 1. Defining Sample Dictionary
student = {
    "name": "Ali",
    "age": 20,
    "city": "Lahore"
}

print("--- Original Dictionary ---")
print(student)
# Output: {'name': 'Ali', 'age': 20, 'city': 'Lahore'}


# 2. Updating Value by Referencing Key Name directly
student["age"] = 21

print("\n--- After Direct Assignment (student['age'] = 21) ---")
print(student)
# Output: {'name': 'Ali', 'age': 21, 'city': 'Lahore'}


# 3. Updating Value using the update() Method
# Expects a dictionary or iterable with key-value pairs
student.update({"age": 22})

print("\n--- After update() Method (student.update({'age': 22})) ---")
print(student)
# Output: {'name': 'Ali', 'age': 22, 'city': 'Lahore'}


# ==========================================
# Key Takeaways:
# - Refer to the specific key inside square brackets [] to assign a new value.
# - Use the .update() method passing a dictionary object to change existing values.
# - If the key exists, its value is overwritten. If it doesn't exist, a new key-value pair is created.
# ==========================================
