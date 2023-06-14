

def upperLineFile(file):
    openFile = open(file, 'rt')
    readFile = openFile.read().strip()
    print(readFile.upper())

# 🔔 file is on Explore With Files/Files
file = input('Enter file name: ')
upperLineFile(file)