"""
    defaultdict is a subclass of Python's built-in 'dict' class. It overrides one method and adds one
    writeable instance variable. The 'defaultdict' class is part of the 'collections' module. The primary
    pupose of 'defaultdict' is to provide a default value for the dictionary keys that have not been set yet.

    When to Use defaultdict:
        1. Handling Missing Keys: When you need to handle missing keys without having to explicitly check for their
           existence.
        2. Grouping Items: When you need to group items together (e.g., grouping words by their first letter).
        3. Counting Items: When you need to count occurrences of items (e.g., counting word frequencies).
        4. Building Complex Data Structures: When building nested dictionaries or lists as values without needing to
           initialize them.
"""

# ------------------------------------------------------------------------------------------------------------

# Basic Example
from collections import defaultdict

# Create a defaultdict with int as default factory
dd = defaultdict(int)
# print(dd['missing_key'])  # Output: 0

# ------------------------------------------------------------------------------------------------------------

# Example 1: Counting Word Frequencies
sentence = "the quick brown fox jumps over the lazy dog the quick brown fox"

word_count = defaultdict(int)

for word in sentence.split():
    word_count[word] += 1

# Print word frequencies
# print(dict(word_count))  # Output: {'the': 3, 'quick': 2, 'brown': 2, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

# ------------------------------------------------------------------------------------------------------------

# Example 2: Grouping Words by Their First Letter
words = ["apple", "banana", "apricot", "blueberry", "avocado"]

# Create a defaultdict with list as the default factory
grouped_words = defaultdict(list)
for word in words:
    first_letter = word[0]
    grouped_words[first_letter].append(word)

# print(dict(grouped_words))  # Output: {'a': ['apple', 'apricot', 'avocado'], 'b': ['banana', 'blueberry']}

# ------------------------------------------------------------------------------------------------------------

# Example 3: Creating a Nested Dictionary
# Create a defaultdict with another defaultdict as the default factory
student_scores = defaultdict(lambda: defaultdict(int))

student_scores['Alice']['Math'] = 95
student_scores['Alice']['Science'] = 90
student_scores['Bob']['Math'] = 85
student_scores['Bob']['History'] = 88

# print(dict(student_scores))  # Output: {'Alice': {'Math': 95, 'Science': 90}, 'Bob': {'Math': 85, 'History': 88}}

# ------------------------------------------------------------------------------------------------------------

# List of edges in the graph
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]

# Create a defaultdict with list as the default factory
adjacency_list = defaultdict(list)

# Build the adjacency list
for start, end in edges:
    adjacency_list[start].append(end)
    adjacency_list[end].append(start)  # For undirected graph

# Print adjacency list
print(dict(adjacency_list))  # Output: {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C', 'E'], 'E': ['D']}

