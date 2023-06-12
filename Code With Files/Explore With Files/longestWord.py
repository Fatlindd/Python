
with open('Files/check_words.txt', 'rt') as file:
    words = file.read().split()

def longestWord(words):
    longest = ''
    for word in words:
        if len(word) > len(longest):
            longest = word
    print(f'Longest word: {longest}')

longestWord(words)

    