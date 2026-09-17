# Day 18: Python Elif Statements & Multi-Condition Logic
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Python Elif Statements
Note: The 'elif' keyword is Python's way of saying:
      "If the previous conditions were not true, then try this condition."
=====================================================
"""

# 1. Evaluating Multiple Conditions using if-elif
score = 75

print("--- Evaluating Grade for Score:", score, "---")

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    # 75 >= 70 evaluates to True, so this block executes
    print("Grade: C")
elif score >= 60:
    print("Grade: D")

# Output: Grade: C


# 2. Short-Circuit Execution Behavior
# Once Python finds a condition that evaluates to True, 
# it executes that block and skips ALL remaining elif/else checks.


# ==========================================
# Key Takeaways:
# - Use 'elif' to chain multiple conditional evaluations sequentially.
# - Conditions are evaluated top-to-bottom.
# - As soon as a condition resolves to True, Python executes its block and bypasses subsequent conditions.
# ==========================================
