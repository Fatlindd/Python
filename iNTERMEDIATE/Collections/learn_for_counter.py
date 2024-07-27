"""
    Counter is a subclass of the 'dict' class in Python, designed specifically to count objects.
    So it's part of the 'collections' module and is used to count the occurrences of elements in an
    iterable, such as list, string or any other container.

    Common Use Cases for 'Counter'
    1. Counting occurrences of elements in a list or string.
    2. Finding the most common elements.
    3. Creating histograms or frequency distributions.

    Summary:
    Counter is useful for counting occurrences and finding common elements in iterables.
    Exercise 1 demonstrated counting words in a text.
    Exercise 2 showed counting character frequency.
    Exercise 3 highlighted finding the most common elements in a list.
"""
# ------------------------------------------------------------------------------------------------------------

# Basic Example
from collections import Counter

fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
fruit_counts = Counter(fruits)
# print(fruit_counts)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})
# print(fruit_counts.keys())  # <-- To get all keys
# print(fruit_counts.values())  # <-- To get all values

# ------------------------------------------------------------------------------------------------------------

# Exercise 1: Counting Words in a Text
def count_words(text):
    words = text.split()
    word_counts = Counter(words)
    return word_counts


text = "this is a sample text with several words this is a sample"
word_counts = count_words(text)
# print(word_counts)
# Output: Counter({'this': 2, 'is': 2, 'a': 2, 'sample': 2, 'text': 1, 'with': 1, 'several': 1, 'words': 1})

# ------------------------------------------------------------------------------------------------------------

# Exercise 2: Character Frequency in a String
def character_frequency(text):
    char_counts = Counter(text)
    return char_counts


text = "hello world"
char_counts = character_frequency(text)
# print(char_counts)
# Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# ------------------------------------------------------------------------------------------------------------

# Exercise 3: Most Common Elements
def most_common_elements(lst, n):
    element_counts = Counter(lst)
    most_common = element_counts.most_common(n)
    return most_common


elements = ['apple', 'banana', 'orange', 'apple', 'banana', 'apple', 'grape']
top_n = 2
common_elements = most_common_elements(elements, top_n)
# print(common_elements)  # [('apple', 3), ('banana', 2)]

# ------------------------------------------------------------------------------------------------------------

# Exercise 4: Comparing Two Texts
def compare_texts(text1, text2):
    words1 = text1.split()
    words2 = text2.split()

    counter1 = Counter(words1)
    counter2 = Counter(words2)

    common_words = counter1 & counter2
    unique_words1 = counter1 - counter2
    unique_words2 = counter2 - counter1

    return common_words, unique_words1, unique_words2


text1 = "this is a sample text with several words this is a sample"
text2 = "this text has different words and a different set of words"
common_words, unique_words1, unique_words2 = compare_texts(text1, text2)

print("Common words: ", common_words)
print("Unique words in text1: ", unique_words1)
print("Unique words in text2: ", unique_words2)
