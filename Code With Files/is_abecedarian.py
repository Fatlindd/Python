
def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

file = open('words.txt')
abecedarians = 0
for line in file:
    word = line.strip()
    if is_abecedarian(word):
        abecedarians += 1

print(f'abecedarians: {abecedarians}')