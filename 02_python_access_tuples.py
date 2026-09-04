# Day X: Accessing Python Tuple Items
# Watch Video Tutorial: [https://www.instagram.com/reel/Dc3WrQaoOwG/?igsi=MWE4OHEwNjR1MzNsZQ==]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Accessing Tuple Items (Indexing, Slicing, Check)
=====================================================
"""

# 1. Accessing Items by Indexing (Positive Indexing)
# Tuple items are indexed starting from 0
mytuple = ("apple", "banana", "cherry")
print("Accessing second item [1]:", mytuple[1])  # Output: banana

# 2. Negative Indexing (Accessing from the end)
# -1 refers to the last item, -2 to the second last, etc.
print("Accessing last item [-1]:", mytuple[-1])  # Output: cherry

# 3. Range of Indexes / Slicing
# Specifies where to start and where to end the range (end index is excluded)
mytuple_large = ("apple", "banana", "cherry", "orange", "kiwi")
print("Slicing [1:4]:", mytuple_large[1:4])  # Output: ('banana', 'cherry', 'orange')

# 4. Check if Item Exists ('in' keyword)
# Determines if a specified item is present in a tuple
if "apple" in mytuple_large:
    print("Yes, 'apple' is in the fruits tuple!")
