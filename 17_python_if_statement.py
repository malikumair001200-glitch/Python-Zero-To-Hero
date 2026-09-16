# Day 17: Python If Statements & Conditional Logic
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Python If Statements & Indentation
Note: An 'if statement' executes a block of code ONLY 
      if the specified condition evaluates to True.
=====================================================
"""

# 1. Basic If Statement (Condition True)
age = 20

print("--- 1. Condition Evaluates to True ---")
if age >= 18:
    # Indented block runs because (20 >= 18) is True
    print("You are an adult")
# Output: You are an adult


# 2. Basic If Statement (Condition False)
age = 16

print("\n--- 2. Condition Evaluates to False ---")
if age >= 18:
    # This block is skipped because (16 >= 18) is False
    print("You are an adult")

print("Program execution continues outside the if block.")


# 3. Indentation Importance
# Python relies on whitespace (indentation) to define scope.
# Omitting indentation causes an IndentationError.
"""
Example of Syntax Error:
if age >= 18:
print("This will raise IndentationError!")
"""


# ==========================================
# Key Takeaways:
# - Python uses standard comparison operators (>=, <=, ==, !=, >, <) to evaluate conditions.
# - If the condition is True, the indented code block executes; if False, it is skipped.
# - Proper indentation (typically 4 spaces) is required to define the scope of the if block.
# ==========================================
