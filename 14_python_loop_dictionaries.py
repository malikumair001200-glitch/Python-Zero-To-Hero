# Day 14: Looping Through Dictionaries in Python
# Watch Video Tutorial: [https://www.instagram.com/reel/DdRAbnhN3he/?stkn=MXMybHNoNXVxYXdtZw==]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Iterating over Python Dictionaries using For Loops
Methods: Default (Keys), .keys(), .values(), and .items()
=====================================================
"""

# 1. Sample Dictionary
student = {
    "name": "Ali",
    "age": 20,
    "city": "Lahore"
}

# 2. Iterating through Keys (Default Behavior)
print("--- Loop through Keys (Default) ---")
for x in student:
    print(x)
# Output:
# name
# age
# city


# 3. Iterating through Values using .values()
print("\n--- Loop through Values (.values()) ---")
for x in student.values():
    print(x)
# Output:
# Ali
# 20
# Lahore


# 4. Iterating through Both Keys and Values using .items()
print("\n--- Loop through Key-Value Pairs (.items()) ---")
for key, value in student.items():
    print(key, ":", value)
# Output:
# name : Ali
# age : 20
# city : Lahore


# ==========================================
# Key Takeaways:
# - Looping over a dictionary directly yields its key names by default.
# - Use dict.values() to iterate strictly over values.
# - Use dict.items() to unpack both keys and values simultaneously in a single loop pass.
# ==========================================
