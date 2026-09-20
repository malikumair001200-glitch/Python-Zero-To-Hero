# Day 23: Python While Loop (Conditional Iteration)
# Watch Video Tutorial: [https://www.instagram.com/reel/DdgqXC7tncF/?stkn=MWNzNms0dDI5Nmxteg==]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Control Flow - While Loop
=====================================================
"""

# ---------------------------------------------------
# 1. Basic While Loop Example
# ---------------------------------------------------
i = 1

print("--- While Loop Iteration ---")

# The loop continues to run as long as the condition evaluates to True
while i < 6:
    print(i)
    # Incrementing the iterator variable is critical to prevent infinite loops
    i += 1


# ---------------------------------------------------
# 2. Key Takeaway & Safeguard Example
# ---------------------------------------------------
# Always ensure the condition will eventually evaluate to False.
# Without 'i += 1', the condition (1 < 6) remains permanently True, 
# resulting in an Infinite Loop that crashes execution.


# ==========================================
# Key Takeaways:
# - A while loop repeatedly executes a block of code AS LONG AS a condition is True.
# - Always update/increment the loop control variable inside the loop body.
# - Useful when the exact number of iterations is unknown in advance.
# ==========================================
