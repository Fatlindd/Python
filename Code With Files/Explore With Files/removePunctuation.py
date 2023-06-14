# line.maketrans('', '', string.punctuation): The maketrans() method is a 
# string method that creates a translation table. 

# The first argument '' represents the characters that we want to replace, 
# and we leave it empty (i.e., no characters to replace). 
# The second argument '' represents the characters with which we want to replace 
# the characters in the first argument, and we leave it empty as well. The third 
# argument string.punctuation represents the characters we want to remove from the line.

# The translate() method is another string method that applies the translation 
# table to the string. It replaces or removes characters based on the translation table. 

import string

fileName = input('> Give the file name: ')
try:
    fhand = open(fileName)
except:
    print('File cannot be opened:', fileName)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)