
with open('Files/check_words.txt', 'rt') as file:
    words = file.read().split()

def display_words(words_list):
    for word in words_list:
        if len(word) < 4:
            print(word)

display_words(words)