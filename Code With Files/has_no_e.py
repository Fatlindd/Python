
def has_no_e(word):
    for char in word:
        if char == 'e':
            return False
    return True

with open('words.txt', 'rt') as file:
    words = file.read().split()

all_words, no_e_in_words = 0, 0
for line in words:
    word = line.strip()
    all_words += 1
    if has_no_e(word):
        no_e_in_words += 1
        print(word)
    
print("Percentage: {:.0%}".format(no_e_in_words / all_words))