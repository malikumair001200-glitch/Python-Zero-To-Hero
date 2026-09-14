# Day 13: Removing Items from Python Dictionaries
# Watch Video Tutorial: [https://www.instagram.com/reel/DdQVe3StqW6/?stkn=dGRsazJwZHZ1d2Yw]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Removing Items from Python Dictionaries
Methods: pop(), popitem(), del keyword, and clear()
=====================================================
"""

# 1. Sample Dictionary
student = {
    "name": "Ali",
    "age": 20,
    "city": "Lahore"
}

print("--- Original Dictionary ---")
print(student)
# Output: {'name': 'Ali', 'age': 20, 'city': 'Lahore'}


# 2. Removing a Specific Item using pop()
# Removes the item with the specified key name and returns its value
student.pop("city")

print("\n--- After pop('city') ---")
print(student)
# Output: {'name': 'Ali', 'age': 20}


# 3. Removing the Last Inserted Item using popitem()
# In Python 3.7+, popitem() removes the last inserted key-value pair
student.popitem()

print("\n--- After popitem() ---")
print(student)
# Output: {'name': 'Ali'}


# 4. Removing a Specific Item or Dictionary using del
# Re-declaring key for demonstration
student["age"] = 20

print("\n--- Re-added 'age' for del demonstration ---")
print(student)

# Using del to remove a specific key
del student["age"]

print("\n--- After del student['age'] ---")
print(student)
# Output: {'name': 'Ali'}


# 5. Emptying the Dictionary using clear()
# Removes all elements, leaving an empty dictionary
student.clear()

print("\n--- After clear() ---")
print(student)
# Output: {}


# ==========================================
# Key Takeaways:
# - pop("key"): Removes a specific item by key.
# - popitem(): Removes the last inserted key-value pair.
# - del dict["key"]: Deletes a specific item (or the entire dictionary variable if key is omitted).
# - clear(): Empties the entire dictionary without deleting the object itself.
# ==========================================
