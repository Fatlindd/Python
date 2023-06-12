read_file = open('Files/check_words.txt', 'rt')

lengthOfNames = []
countWords = 0
for name in read_file.read().split():
    countWords += 1
    length = len(name)
    lengthOfNames.append(length)

print('Average: ', sum(lengthOfNames) / countWords)