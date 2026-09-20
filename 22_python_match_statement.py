# Day 22: Python Match Statement (Pattern Matching)
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Conditional Control Flow - Match-Case Statement
=====================================================
"""

# ---------------------------------------------------
# 1. Basic Match Statement Example
# ---------------------------------------------------
option = 2

print("--- User Menu Selection ---")

# Evaluates the expression against multiple case values
match option:
    case 1:
        print("Profile")
    case 2:
        print("Settings")
    case 3:
        print("Logout")


# ---------------------------------------------------
# 2. Match Statement with Default Case (_)
# ---------------------------------------------------
invalid_option = 99

print("\n--- Fallback / Invalid Option Test ---")

# The wild-card (_) pattern handles any unmatched inputs
match invalid_option:
    case 1:
        print("Profile")
    case 2:
        print("Settings")
    case 3:
        print("Logout")
    case _:
        print("Invalid option")


# ==========================================
# Key Takeaways:
# - The match statement compares a value against multiple defined case patterns.
# - The wildcard underscore (_) acts as a default fallback when no match is found.
# - Cleaner and more readable alternative to multi-branch if-elif-else chains.
# ==========================================
