# Day 16: Nested Dictionaries in Python
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Nested Dictionaries in Python
Note: A dictionary can contain dictionaries, this is called 
      nested dictionaries.
=====================================================
"""

# 1. Defining a Nested Dictionary
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

print("--- 1. Full Nested Dictionary Structure ---")
print(myfamily)


# 2. Accessing Items in Nested Dictionaries
# Access nested keys using multiple square brackets [][]
child2_name = myfamily["child2"]["name"]

print("\n--- 2. Accessing Nested Item (child2 -> name) ---")
print("Child 2 Name:", child2_name)
# Output: Tobias


# 3. Looping Through Nested Dictionaries
print("\n--- 3. Iterating Through Nested Dictionary ---")
# Outer loop unpacks outer keys (child1, child2...) and inner dictionaries
for child, info in myfamily.items():
    print(f"\n{child}:")
    # Inner loop iterates through key-value pairs of each nested dictionary
    for key, value in info.items():
        print(f"  {key}: {value}")


# ==========================================
# Key Takeaways:
# - Nested Dictionaries store dictionaries inside another dictionary.
# - Access nested values by chaining bracket keys: dict[outer_key][inner_key].
# - Use nested for loops (outer loop for parent keys, inner loop for child items) to unpack hierarchical data.
# ==========================================
