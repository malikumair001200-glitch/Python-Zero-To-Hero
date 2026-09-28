# Day 30: Python Recursion (Self-Calling Functions & Base Case)
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Advanced Control Flow - Recursion
=====================================================
"""

# ---------------------------------------------------
# 1. Recursive Function Definition
# ---------------------------------------------------
# A recursive function calls itself to break down a problem into smaller steps.
def countdown(n):
    # Base Case (Stop Condition): Prevents infinite function execution stack
    if n <= 0:
        print("Done!")
    else:
        print(n)
        # Recursive Step: Function calling itself with a modified argument (n - 1)
        countdown(n - 1)

# ---------------------------------------------------
# 2. Executing the Recursive Function
# ---------------------------------------------------
print("--- Recursive Countdown Execution ---")
countdown(5)


# ==========================================
# Key Takeaways:
# - Recursion is a programming pattern where a function calls itself.
# - Base Case: Mandatory condition that stops the recursive calls (prevents RecursionError).
# - Recursive Step: Reduces the problem space closer to the Base Case with each iteration.
# ==========================================
