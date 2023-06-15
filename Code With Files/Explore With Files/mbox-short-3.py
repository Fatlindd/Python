# Program that categorizes each email message by which day of the week the commit was done.

dict_days = dict()
# fname = 'Files/mbox-short.txt'
fname = input('> Give the file name: ')

try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened: ', fname)
    exit()

for line in fhand:
    words = line.split()
    
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in dict_days:
            dict_days[words[2]] = 1
        else:
            dict_days[words[2]] += 1
print(dict_days)