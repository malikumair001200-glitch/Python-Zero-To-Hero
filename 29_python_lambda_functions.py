# Day 29: Python Lambda Functions (Anonymous Functions)
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Compact Code - Lambda Functions
=====================================================
"""

# ---------------------------------------------------
# 1. Standard Function vs. Lambda Function
# ---------------------------------------------------
# Standard function definition using 'def'
def add_ten(a):
    return a + 10

# Equivalent compact Lambda function syntax
# Syntax: lambda arguments : expression
add_ten_lambda = lambda a: a + 10

print("--- Standard vs. Lambda Output ---")
print("Standard Function Result:", add_ten(5))         # Output: 15
print("Lambda Function Result  :", add_ten_lambda(5))  # Output: 15


# ---------------------------------------------------
# 2. Lambda Function with Multiple Arguments
# ---------------------------------------------------
# Lambda function accepting two parameters
multiply = lambda a, b: a * b

print("\n--- Lambda with Multiple Arguments ---")
print("Multiplication Result:", multiply(5, 6))  # Output: 30


# ==========================================
# Key Takeaways:
# - Lambda functions are small, anonymous functions defined without 'def'.
# - A lambda function can take any number of arguments, but can only have ONE expression.
# - Best used for short, single-line operations or inside higher-order functions (like map, filter, or sorted).
# ==========================================
