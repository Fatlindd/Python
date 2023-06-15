# Write a program to read through a mail log, build a histogram using a dictionary to 
# count how many messages have come each email address, and print the dictionary.

dict_email = dict()
fname = input('> Give file name: ')
try: 
    fhand = open(fname)
except FileNotFoundError:
    print(f'File cannot be opened {fname}')
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in dict_email:
            dict_email[words[1]] = 1
        else:
            dict_email[words[1]] += 1
print(dict_email)
