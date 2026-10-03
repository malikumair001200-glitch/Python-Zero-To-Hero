# Day 36: Python Datetime Module & Date Formatting
# Watch Video Tutorial: [Video Publish Hone Ke Baad Yahan Link Paste Karein]
# Author: Waqas Manzoor

"""
=====================================================
Topic: Built-in Modules - Working with Dates and Times
=====================================================
"""

import datetime

# ---------------------------------------------------
# 1. Fetching Current Date and Time
# ---------------------------------------------------
# datetime.datetime.now() retrieves system timestamp
now = datetime.datetime.now()

print("--- Current Date & Time ---")
print(now)  # Output format: YYYY-MM-DD HH:MM:SS.microsecond


# ---------------------------------------------------
# 2. Creating Specific Date Objects
# ---------------------------------------------------
# Manually constructing a date (Year, Month, Day)
specific_date = datetime.datetime(2020, 5, 17)

print("\n--- Specific Created Date ---")
print(specific_date)  # Output: 2020-05-17 00:00:00


# ---------------------------------------------------
# 3. Date Formatting using strftime()
# ---------------------------------------------------
# strftime() formats date objects into readable string formats (%B gives full month name)
formatted_date = datetime.datetime(2018, 6, 1)

print("\n--- Formatted Date (Full Month Name) ---")
print(formatted_date.strftime("%B"))  # Output: June


# ==========================================
# Key Takeaways:
# - datetime module is built-in (no pip installation required).
# - datetime.now(): Gets current system timestamp.
# - datetime(year, month, day): Constructs custom date instances.
# - strftime(format_specifier): Converts date objects into custom string formats (%B = Month name, %Y = Year, %d = Day).
# ==========================================
