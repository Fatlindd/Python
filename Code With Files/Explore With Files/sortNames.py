
with open('Files/names.txt', 'rt') as file:
    words = file.read().split()

def sortNames(words):
    words.sort()
    newFile = open('Files/sorted_names.txt', 'w')
    for word in words:
        newFile.write(word + '\n')
sortNames(words)