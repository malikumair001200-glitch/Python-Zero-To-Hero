# Day 19: Python Else Statement (Default Fallback Condition)
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Conditional Logic - Else Statement (Fallback Option)
=====================================================
"""

# Define the variable
food = "pizza"

print("--- Checking Food Selection ---")

# 1. If statement checks first condition
if food == "chicken":
    print("Chicken order")

# 2. Elif statement checks second condition
elif food == "beef":
    print("Beef order")

# 3. Else statement executes when all preceding conditions are False
else:
    print("Other food")


# ==========================================
# Key Takeaway:
# - The 'else' block does not evaluate any condition.
# - It acts as a default fallback when all 'if' and 'elif' conditions evaluate to False.
# ==========================================
