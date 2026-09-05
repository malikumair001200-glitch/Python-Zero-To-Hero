# Day 3: Updating Python Tuples (Workarounds)
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Updating Tuples (Change, Add, Remove Items)
Note: Tuples are immutable, so we use List conversion or concatenation.
=====================================================
"""

# 1. Change Tuple Value
# Convert to List -> Change Item -> Convert back to Tuple
mytuple = ("apple", "banana", "cherry")
mylist = list(mytuple)
mylist[1] = "kiwi"
mytuple = tuple(mylist)

print("Updated Tuple (Change Item):", mytuple)
# Output: ('apple', 'kiwi', 'cherry')


# 2. Add Item to Tuple (using + operator)
# Combine two tuples (Note the trailing comma for single-item tuple)
mytuple = mytuple + ("orange",)

print("Updated Tuple (Add Item):", mytuple)
# Output: ('apple', 'kiwi', 'cherry', 'orange')


# 3. Remove Item from Tuple
# Convert to List -> Remove Item -> Convert back to Tuple
mylist = list(mytuple)
mylist.remove("apple")
mytuple = tuple(mylist)

print("Updated Tuple (Remove Item):", mytuple)
# Output: ('kiwi', 'cherry', 'orange')
