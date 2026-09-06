# Day 4: Unpacking Tuples in Python (and Asterisk *)
# Watch Video Tutorial: [https://www.instagram.com/reel/Dc8UFrBNe_u/?stkn=MXgwaDlpN3Zvem45bw==]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Unpacking Tuples & Using Asterisk (*) for Extra Values
=====================================================
"""

# 1. Basic Unpacking
# Extracting values back into variables (number of variables = number of items)
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print("--- Basic Unpacking ---")
print("green :", green)   # Output: apple
print("yellow:", yellow)  # Output: banana
print("red   :", red)     # Output: cherry


# 2. Unpacking using Asterisk (*)
# If the number of values exceeds variables, use * to collect remaining values in a List
fruits_extended = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits_extended

print("\n--- Unpacking with Asterisk (*) ---")
print("green :", green)   # Output: apple
print("yellow:", yellow)  # Output: banana
print("red   :", red)     # Output: ['cherry', 'strawberry', 'raspberry']


# ==========================================
# Key Takeaway:
# - Unpacking allows assigning tuple elements to multiple variables directly.
# - Use * to capture leftover items into a list when variable counts don't match.
# ==========================================
