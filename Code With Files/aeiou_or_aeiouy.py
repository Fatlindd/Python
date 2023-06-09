def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True

with open('files/words.txt', 'rt') as word:
    file = word.read().split()

aeiou = 0
aeiouy = 0
for line in file:
    word = line.strip()
    if uses_all(word, 'aeiou'):
        aeiou += 1
    if uses_all(word, 'aeiouy'):
        aeiouy += 1
    
print(f'aeiou: {aeiou}')
print(f'aeiouy: {aeiouy}')
