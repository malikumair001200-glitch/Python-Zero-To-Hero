# Day 06: Introduction to Python Sets & Duplicate Handling
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Python Sets (Duplicates, Unordered Nature & Syntax)
=====================================================
"""

# 1. Creating a Set with Curly Brackets {}
# Sets do not allow duplicate values — duplicates are automatically ignored
myset = {"apple", "banana", "cherry", "apple"}

print("--- Print Set (Notice duplicate 'apple' is removed) ---")
print(myset)

# Output (Order may vary since Sets are unordered):
# {'banana', 'cherry', 'apple'}


# ==========================================
# Key Characteristics of Sets:
# - Unordered: Items do not have a defined order and cannot be accessed by index.
# - Unchangeable: Items cannot be changed, but new items can be added/removed.
# - No Duplicates: Duplicate values are automatically filtered out.
# ==========================================
