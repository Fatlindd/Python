
# 🔔 read() - reads the entire content of a file as a single string.
# 🔔 split() - convert the string into list based on spaces between words in string.
with open('Files/check_words.txt', 'rt') as file:
    word_list = file.read().split()
    count = 0
    for name in word_list:
        count += 1
print(f'Number of words: {count}')