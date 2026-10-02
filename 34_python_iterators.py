# Day 34: Python Iterators (iter() and next() Functions)
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Control Flow - Python Iterators & Iterables
=====================================================
"""

# ---------------------------------------------------
# 1. Iterable vs Iterator
# ---------------------------------------------------
# A tuple is an iterable object, but not an iterator itself.
mytuple = ("apple", "banana", "cherry")

# Converting the iterable (tuple) into an iterator object using iter()
myit = iter(mytuple)


# ---------------------------------------------------
# 2. Traversing Values Using next()
# ---------------------------------------------------
print("--- Accessing Items Sequentially ---")

# Fetching elements one-by-one on-demand
print(next(myit))  # Output: apple
print(next(myit))  # Output: banana
print(next(myit))  # Output: cherry


# ==========================================
# Key Takeaways:
# - Iterable: An object that contains elements that can be iterated over (e.g., lists, tuples, strings).
# - Iterator: An object with a state that remembers where it is during iteration.
# - iter(): Initializes/returns an iterator object from an iterable.
# - next(): Fetches the next item from an iterator object until StopIteration is raised.
# ==========================================
