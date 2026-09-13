# Day 12: Adding Items to Python Dictionaries
# Watch Video Tutorial: [https://www.instagram.com/reel/DdOZt_CtfTx/?stkn=aWhoMzhnbXBzOGFt]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Adding New Items to Python Dictionaries
Note: Adding a new item is done by assigning a value to a new key
      or using the .update() method with a new key-value pair.
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


# 2. Adding a New Key-Value Pair using Direct Assignment
# Assigning a value to a non-existing key automatically creates it
student["subject"] = "Python"

print("\n--- After Adding New Key ('subject') ---")
print(student)
# Output: {'name': 'Ali', 'age': 20, 'city': 'Lahore', 'subject': 'Python'}


# 3. Adding a New Key-Value Pair using the update() Method
# If the key inside update() does not exist, it appends the new pair
student.update({"grade": "A"})

print("\n--- After Adding New Key via update() ('grade') ---")
print(student)
# Output: {'name': 'Ali', 'age': 20, 'city': 'Lahore', 'subject': 'Python', 'grade': 'A'}


# ==========================================
# Key Takeaways:
# - To insert a new item, assign a value to a brand-new key name inside square brackets [].
# - Alternatively, pass a new key-value pair into the .update() method.
# - If the key is new, Python appends it. If the key already exists, Python overwrites its value.
# ==========================================
