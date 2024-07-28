"""
    OrderedDict is a dictionary subclass in Python's collections module that maintains the order of items
    based on the order in which they were inserted. While regular dictionaries in Python (from Python 3.7) also
    maintain insertion order, 'OrderedDict' provides additional methods that can be useful in certain scenarios.

    When to use 'OrderedDict'
        1. Maintaining Insertion Order: When you need to maintain the order of items as they were added.
        2. Reordering items: When you need to manipulate the order of items (e.g, moving items to the end or
            beginning.
        3. Implementing LRU cache: When you need to implement a Least Recently Used (LRU) cache.
        4. Dictionary Subclass with Extra Features: When you want a dictionary with additional methods like
            'move_to_end'.
"""

# ------------------------------------------------------------------------------------------------------------

# Basic Example
from collections import OrderedDict

# Create an Ordered Dict
ordered_dict = OrderedDict()
ordered_dict['apple'] = 1
ordered_dict['banana'] = 2
ordered_dict['orange'] = 3

# print(ordered_dict)  # Output: OrderedDict([('apple', 1), ('banana', 2), ('orange', 3)])

# ------------------------------------------------------------------------------------------------------------

# Example 1: Maintaining Insertion Order

ordered_dict1 = OrderedDict()
ordered_dict1['first'] = 1
ordered_dict1['second'] = 2
ordered_dict1['third'] = 3

for key, value in ordered_dict1.items():
    pass
    # print(f"{key}: {value}")

# ------------------------------------------------------------------------------------------------------------

# Example 2: Reordering items

ordered_dict2 = OrderedDict()
ordered_dict2['first'] = 1
ordered_dict2['second'] = 2
ordered_dict2['third'] = 3

# Move 'second' to the end
ordered_dict2.move_to_end('second')
for key, value in ordered_dict2.items():
    pass
    # print(f"{key}: {value}")

# ------------------------------------------------------------------------------------------------------------

# Example 3: Sorting 'OrderedDict' by Value
ordered_dict3 = OrderedDict()
ordered_dict3['apple'] = 3
ordered_dict3['banana'] = 1
ordered_dict3['orange'] = 2

# Sort OrderedDict by values
sorted_ordered_dict = OrderedDict(sorted(ordered_dict3.items(), key=lambda item: item[1]))
for key, value in ordered_dict3.items():
    print(f"{key}: {value}")

