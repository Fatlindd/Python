# write program to read through the mbox-short.txt and figure out who has sent the greatest
# number of mail messages.
fname = input('> Enter name of file: ')
if len(fname) < 1: fname = 'mbox-short.txt'
fhand = open(fname)

list_words = list()
for line in fhand:
    if not line.startswith('From:'): continue
    line = line.split()
    list_words.append(line[1])

# count email address saved on list_words
counts = dict()
for word in list_words:
    counts[word] = counts.get(word, 0) + 1

maxEmail = None
emailAddr = None
for email, count in counts.items():
    if maxEmail is None or count > maxEmail:
        maxEmail = count
        emailAddr = email
print(f'Maximum email are send from:\n{emailAddr, maxEmail}') 