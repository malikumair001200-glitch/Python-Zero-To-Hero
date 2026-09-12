# Day 10: Accessing Python Dictionary Items
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Accessing Dictionary Items (Square Brackets & get() Method)
=====================================================
"""

# 1. Sample Dictionary
student = {
    "name": "Ali",
    "age": 20,
    "city": "Lahore"
}

# 2. Accessing Values using Square Brackets []
print("--- Accessing Value via Key Name ---")
print("Student Name:", student["name"])
# Output: Ali


# 3. Alternative Method: Using get()
# Safe retrieval using the .get() method
print("\n--- Accessing Value via get() Method ---")
print("Student City:", student.get("city"))
# Output: Lahore


# ==========================================
# Key Takeaways:
# - Refer to key names inside square brackets (e.g., student["name"]) to retrieve values directly.
# - Alternatively, use student.get("name") for a safer access pattern.
# - Accessing a non-existent key with [] raises a KeyError, while .get() safely returns None.
# ==========================================
