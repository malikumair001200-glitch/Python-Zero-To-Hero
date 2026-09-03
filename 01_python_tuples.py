# ==========================================
# Day X: Python Tuples Explained Simply
# Watch Video Tutorial: [Link Video Publish Hone Ke Baad Yahan Lagana]
# Author: Waqas Manzoor Tech
# ==========================================

# 1. Defining a Tuple
# Tuples are used to store multiple items in a single variable.
# They are written with round brackets ().
my_tuple = ("apple", "banana", "cherry")
print("Original Tuple:", my_tuple)


# 2. Accessing Items (Indexing)
# Tuple items are ordered and zero-indexed, just like Lists.
print("Item at index 1:", my_tuple[1])  # Output: banana


# 3. Allow Duplicates
# Tuples can store duplicate values without any error.
duplicate_tuple = ("apple", "banana", "cherry", "apple")
print("Tuple with duplicates:", duplicate_tuple)


# 4. Immutability (Unchangeable)
# Once created, you CANNOT change, add, or remove items.
# Un-commenting the line below will throw a TypeError:
# my_tuple[1] = "mango"  # TypeError: 'tuple' object does not support item assignment


# 5. One-item Tuple Rule
# To create a tuple with only one item, you MUST add a trailing comma.
single_item_tuple = ("apple",)  # This is a Tuple
not_a_tuple = "apple"  # This is a String

print("Type with comma:", type(single_item_tuple))  # <class 'tuple'>
print("Type without comma:", type(not_a_tuple))  # <class 'str'>


# ==========================================
# Key Takeaway:
# Use Tuples when you have data that should remain constant and safe 
# from accidental modifications throughout your program!
# ==========================================
