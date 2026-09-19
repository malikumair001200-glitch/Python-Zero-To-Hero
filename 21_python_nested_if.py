# Day 21: Python Nested If Statements
# Watch Video Tutorial: [https://www.instagram.com/reel/Ddd9UQBtsPb/?stkn=ZzU3ZW55anByYXRo]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Conditional Logic - Nested If Statements
=====================================================
"""

# ---------------------------------------------------
# 1. Basic Nested If Example (Eligibility Check)
# ---------------------------------------------------
age = 25
has_degree = True

print("--- Job Application Verification ---")

# Outer condition: Checks primary eligibility (Age)
if age >= 18:
    # Inner condition: Evaluates secondary requirement (Degree)
    if has_degree:
        print("You can apply")
    else:
        print("Application rejected: Degree required.")
else:
    print("Application rejected: Underage.")


# ---------------------------------------------------
# 2. Alternative Scenario (Condition Fails)
# ---------------------------------------------------
applicant_age = 16
applicant_degree = True

print("\n--- Secondary Test Case ---")
if applicant_age >= 18:
    if applicant_degree:
        print("You can apply")
    else:
        print("Application rejected: Degree required.")
else:
    print("Application rejected: Underage.")


# ==========================================
# Key Takeaways:
# - A nested if statement is an if block inside another if block.
# - The inner condition is executed ONLY IF the outer condition evaluates to True.
# ==========================================
