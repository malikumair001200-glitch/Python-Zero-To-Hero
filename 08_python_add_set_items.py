# Day 08: Adding Items to Python Sets (add() vs update())
# Watch Video Tutorial: [https://www.instagram.com/reel/DdGyRhFtFFp/?stkn=MWZ3aDF6Zm8yYW5obw==]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Adding Elements to Python Sets
Note: Sets are mutable, meaning we can add new items to existing sets.
=====================================================
"""

# 1. Adding a Single Item using add()
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")

print("--- After add('orange') ---")
print(thisset)
# Output: {'banana', 'cherry', 'apple', 'orange'}


# 2. Adding Multiple Set Items using update()
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)

print("\n--- After update(tropical) ---")
print(thisset)
# Output: {'banana', 'mango', 'papaya', 'cherry', 'pineapple', 'apple', 'orange'}


# 3. Adding Items from Any Iterable (List/Tuple) using update()
mylist = ["kiwi", "grapes"]
thisset.update(mylist)

print("\n--- After update(mylist) ---")
print(thisset)
# Output includes all elements from list added to set without duplicates


# ==========================================
# Key Takeaways:
# - Use add() to insert a single element into a Set.
# - Use update() to insert multiple elements from another Set or any iterable (List, Tuple, etc.).
# - Duplicates will still be automatically ignored during addition.
# ==========================================
