"""
This module demonstrates set operations by checking if two sets are disjoint.

A disjoint set contains no common elements with another set.
"""

# Define two sample sets with no common elements
set1 = {1, 2, 3}
set2 = {4, 5, 6}

# Check if the sets are disjoint using the isdisjoint() method
if set1.isdisjoint(set2):
    print("The sets are disjoint.")  # Sets have no common elements
else:
    print("The sets are not disjoint.")  # Sets share at least one element 