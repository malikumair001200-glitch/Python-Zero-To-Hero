# Day 37: Python Math (Built-in Functions and math Module)
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Built-in Functions & Standard Library - Python Math
=====================================================
"""

import math

# ---------------------------------------------------
# 1. Built-in Math Functions
# ---------------------------------------------------
# Finding minimum and maximum values in a sequence or set of numbers
x = min(5, 10, 25)
y = max(5, 10, 25)

print("--- Built-in Min & Max ---")
print("Min Value:", x)  # Output: 5
print("Max Value:", y)  # Output: 25

# Absolute value abs() and Power function pow()
abs_val = abs(-7.25)
power_val = pow(4, 3)

print("\n--- Absolute & Power Functions ---")
print("Absolute Value of -7.25:", abs_val)  # Output: 7.25
print("4 raised to power 3:", power_val)    # Output: 64


# ---------------------------------------------------
# 2. Advanced Mathematical Operations (math Module)
# ---------------------------------------------------
# Using math.sqrt() for square root calculation
sqrt_val = math.sqrt(64)

print("\n--- math Module Square Root ---")
print("Square root of 64:", sqrt_val)  # Output: 8.0


# ==========================================
# Key Takeaways:
# - min() & max(): Find extreme numeric boundaries instantly.
# - abs(): Returns positive distance from zero.
# - pow(x, y): Calculates power x^y (equivalent to x ** y).
# - math module: Provides advanced mathematical constants & methods like sqrt(), ceil(), floor(), sin(), etc.
# ==========================================
