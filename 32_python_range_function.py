# Day 32: Python range() Function (Start, Stop, and Step Parameters)
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Control Flow - Python range() Sequence Generator
=====================================================
"""

# ---------------------------------------------------
# 1. Full Syntax: range(start, stop, step)
# ---------------------------------------------------
# Generates a sequence from start (inclusive) to stop (exclusive) with a specified step increment.
numbers = range(1, 10, 2)

print("--- Custom Step Sequence (1, 10, 2) ---")
print(list(numbers))  # Output: [1, 3, 5, 7, 9]


# ---------------------------------------------------
# 2. Single Parameter Syntax: range(stop)
# ---------------------------------------------------
# Default start is 0, default step is 1. Stops right before the specified number.
default_sequence = range(5)

print("\n--- Default Sequence range(5) ---")
print(list(default_sequence))  # Output: [0, 1, 2, 3, 4]


# ==========================================
# Key Takeaways:
# - start: The beginning index of the sequence (inclusive, default: 0).
# - stop : The end index of the sequence (exclusive - stops at stop-1).
# - step : The increment value between each number (default: 1).
# - Immutable & Memory Efficient: range() creates an iterable object without storing all numbers in memory at once.
# ==========================================
