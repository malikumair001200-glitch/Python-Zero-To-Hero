# Day 27: Python Variable Scope (Local vs Global Scope)
# Watch Video Tutorial: [https://www.instagram.com/reel/DdqUsLFtYam/?stkn=Nzhkank4MGNwbTA3]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Variable Scope - Local Scope vs. Global Scope
=====================================================
"""

# ---------------------------------------------------
# 1. Local Scope
# ---------------------------------------------------
# A variable created inside a function belongs to the local scope of that function,
# and can only be used inside that function.
def myfunc_local():
    x = 300
    print("Inside Local Scope Function:", x)

myfunc_local()

# Accessing 'x' outside the function will throw a NameError:
# print(x)  # NameError: name 'x' is not defined


# ---------------------------------------------------
# 2. Global Scope
# ---------------------------------------------------
# A variable created in the main body of the Python code is a global variable
# and belongs to the global scope. It is accessible from any scope (inside and outside functions).
y = 300

def myfunc_global():
    print("Accessing Global Variable Inside Function:", y)

myfunc_global()
print("Accessing Global Variable Outside Function:", y)


# ==========================================
# Key Differences Summary:
# - Local Scope : Variable is created INSIDE a function and accessible ONLY within it.
# - Global Scope: Variable is created OUTSIDE functions and accessible ANYWHERE in the file.
# - Scope rules prevent unexpected variable overwrites across different modules.
# ==========================================
