# Day 07: Accessing Items in Python Sets
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Accessing Set Items (Membership Testing & Iteration)
Note: Sets are unordered, so items cannot be accessed via index.
=====================================================
"""

# Defining a sample set
thisset = {"apple", "banana", "cherry"}

# 1. Checking if an item exists using the 'in' keyword (Membership Testing)
# Returns True if present, False if not
print("--- Checking Item Existence ('in' keyword) ---")
print("Is 'banana' in set?", "banana" in thisset)  # Output: True
print("Is 'orange' in set?", "orange" in thisset)  # Output: False


# 2. Iterating through Set items using a 'for' loop
# Since Sets have no indexes, we loop through items directly
print("\n--- Looping Through Set Items ---")
for x in thisset:
    print(x)

# Output (Order may vary due to unordered nature):
# apple
# banana
# cherry

# ==========================================
# Key Takeaways:
# - You CANNOT access items in a set by referring to an index or key (e.g., thisset[0] will raise an error).
# - Use the 'in' keyword to check if a specific item exists.
# - Use a 'for' loop to iterate through every item one by one.
# ==========================================
