# Day 15: Copying Dictionaries in Python
# Watch Video Tutorial: [https://www.instagram.com/reel/DdS3SkUti7X/?stkn=MXgzcDFvZmNqczdkbA==]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Copying Dictionaries (copy() Method vs Direct Reference)
Note: Assigning dict2 = dict1 does NOT make a copy. It only creates 
      a reference to the same memory location!
=====================================================
"""

# 1. Incorrect Copying: Direct Reference Assignment (=)
print("--- 1. Direct Assignment (=) Issue ---")
original_dict = {
    "name": "Ali",
    "age": 20
}

# Modifying dict2 will also modify original_dict because they point to the same object
ref_dict = original_dict
original_dict["age"] = 21

print("Original Dict:", original_dict)
print("Referenced Dict:", ref_dict)
# Output: Both show age as 21!


# 2. Correct Way: Using the copy() Method
print("\n--- 2. Independent Copy using copy() ---")
dict1 = {
    "name": "Ali",
    "age": 20
}

# Creating an independent shallow copy
dict2 = dict1.copy()

# Updating dict1 will NOT affect dict2
dict1["age"] = 21

print("dict1 (Updated):", dict1)  # Output: {'name': 'Ali', 'age': 21}
print("dict2 (Copied) :", dict2)  # Output: {'name': 'Ali', 'age': 20}


# 3. Alternative Way: Using the dict() Built-in Function
print("\n--- 3. Independent Copy using dict() ---")
dict3 = dict(dict1)
print("dict3 (Constructor Copy):", dict3)


# ==========================================
# Key Takeaways:
# - Writing dict2 = dict1 only creates a new pointer/reference to the original dictionary.
# - Modifying a referenced dictionary alters the original data object simultaneously.
# - Use dict.copy() or dict(original_dict) to create a true independent copy.
# ==========================================
