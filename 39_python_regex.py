# Day 39: Python Regular Expressions (re Module & Key Functions)
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Text Processing - Python Regular Expressions (RegEx)
=====================================================
"""

import re

# Sample target text
txt = "The rain in Spain"

# ---------------------------------------------------
# 1. findall() Function
# ---------------------------------------------------
# Returns a list containing all matches of the pattern
matches = re.findall("ai", txt)

print("--- 1. findall() Output ---")
print("All matching patterns:", matches)  # Output: ['ai', 'ai']


# ---------------------------------------------------
# 2. search() Function
# ---------------------------------------------------
# Searches for a match and returns a Match Object if found
search_result = re.search("Spain", txt)

print("\n--- 2. search() Output ---")
print("Search Match Object:", search_result)
print("Start position:", search_result.start()) if search_result else None


# ---------------------------------------------------
# 3. split() Function
# ---------------------------------------------------
# Returns a list where the string has been split at each match (\s = whitespace)
split_result = re.split(r"\s", txt)

print("\n--- 3. split() Output ---")
print("Split Text List:", split_result)  # Output: ['The', 'rain', 'in', 'Spain']


# ---------------------------------------------------
# 4. sub() Function
# ---------------------------------------------------
# Replaces one or many matches with a specified string
sub_result = re.sub(r"\s", "-", txt)

print("\n--- 4. sub() Output ---")
print("Replaced String:", sub_result)  # Output: The-rain-in-Spain


# ==========================================
# Key Takeaways:
# - re module provides built-in support for Regular Expressions in Python.
# - findall(): Extracts all occurrences of a matching pattern into a list.
# - search(): Returns a Match object if a pattern is present anywhere in the string.
# - split(): Splits the string into substrings wherever the pattern matches.
# - sub(): Replaces matched patterns with replacement text.
# ==========================================
