
def saveToDictionary(file):
    with open('Files/text.txt', 'rt') as file:
        content = file.read().split()

    words = dict()
    for word in content:
        words[word] = 'value'
    
    print('⚠ Words from text.txt are saved into dictionary!')
    w = input('> Check for word: ')
    if w in words:
        print('Yes!')
    else:
        print('No!')

# fileName = 'Files/text.txt'
fileName = input('> Your file name: ')
saveToDictionary(fileName)



