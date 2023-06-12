
# 🔔 isupper() check if word or string is all uppercase.
fileToRead = open('Files/check_words.txt', 'rt')
def isUpperCase(fileToRead):
    words = fileToRead.read().split()
    countWords = 0
    countChars = 0
    for word in words:
        if word.isupper():
            countWords += 1
        for char in word:
            if char.isupper():
                countChars += 1
    print(f'Number of upper word: {countWords}')
    print(f'Number of upper chars: {countChars}')

isUpperCase(fileToRead)