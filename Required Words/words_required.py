"""
1. Write a function named uses_all that takes a word and a string of required letters, and that returns True if
the word uses all the required letters at least once.
2. How many words are there that use all the vowels aeiou?
3. How about aeiouy
"""

def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False

    return True

aeiou = 0
aeiouy = 0

fin = open('words.txt', 'rt')
for line in fin:
    word = line.strip()
    if uses_all(word, 'aeiou'):
        aeiou += 1
    if uses_all(word, 'aeiouy'):
        aeiouy += 1

print(f'aeiou: {aeiou}')
print(f'aeiouy: {aeiouy}')
