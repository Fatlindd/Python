
# 🔔 read() - 
# 🔔 split() - 
with open('Files/check_words.txt', 'rt') as file:
    word_list = file.read().split()
    count = 0
    for name in word_list:
        count += 1
print(f'Number of words: {count}')