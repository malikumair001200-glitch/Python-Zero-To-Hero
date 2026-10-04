# Day 38: Python JSON Handling (json.loads() & json.dumps())
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Standard Library - Working with JSON Data
=====================================================
"""

import json

# ---------------------------------------------------
# 1. Parsing JSON String to Python Dictionary (json.loads)
# ---------------------------------------------------
# JSON string received from an API or web service
json_string = '{ "name":"John", "age":30, "city":"New York"}'

# Convert (parse) JSON string into a Python dictionary
python_dict = json.loads(json_string)

print("--- JSON to Python Dictionary ---")
print("Full Dictionary:", python_dict)
print("Accessing 'age':", python_dict["age"])  # Output: 30


# ---------------------------------------------------
# 2. Converting Python Dictionary to JSON String (json.dumps)
# ---------------------------------------------------
# Python dictionary object
python_data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert (serialize) Python dictionary into JSON formatted string
json_output = json.dumps(python_data)

print("\n--- Python Dictionary to JSON String ---")
print("JSON Output String:", json_output)
print("Type of Output:", type(json_output))  # Output: <class 'str'>


# ==========================================
# Key Takeaways:
# - JSON (JavaScript Object Notation) is a standard format for data exchange between web systems.
# - json.loads(): Parses/converts a valid JSON string into a Python Dictionary.
# - json.dumps(): Serializes/converts a Python Dictionary into a JSON-formatted string.
# ==========================================
