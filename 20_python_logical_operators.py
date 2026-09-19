# Day 20: Python Logical Operators (and, or, not)
# Watch Video Tutorial: [https://www.instagram.com/reel/DddSaBTN9ou/?stkn=ZmY0dDlrNzJ5NTB6]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Conditional Logic - Logical Operators (and, or, not)
=====================================================
"""

# ---------------------------------------------------
# 1. 'and' Operator (Both conditions MUST be True)
# ---------------------------------------------------
weather_good = True
friends_free = True

print("--- 1. Testing 'and' Operator ---")
if weather_good and friends_free:
    print("Let's go!")
else:
    print("Plan cancelled.")


# ---------------------------------------------------
# 2. 'or' Operator (At least ONE condition MUST be True)
# ---------------------------------------------------
weather_good = False
friends_free = True

print("\n--- 2. Testing 'or' Operator ---")
if weather_good or friends_free:
    print("Let's go!")
else:
    print("Plan cancelled.")


# ---------------------------------------------------
# 3. 'not' Operator (Reverses the Boolean result)
# ---------------------------------------------------
weather_good = False

print("\n--- 3. Testing 'not' Operator ---")
if not weather_good:
    print("Stay home")


# ==========================================
# Key Takeaways:
# - and: Evaluates to True only if ALL expressions are True.
# - or : Evaluates to True if AT LEAST ONE expression is True.
# - not: Inverts the Boolean truth value (True -> False, False -> True).
# ==========================================
