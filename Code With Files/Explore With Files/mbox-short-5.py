# Check who has the most messages in the file. After all the data has been read and the dictinary
# has been created, look through the dictionary using a maximum loop to find who has the most
# messages and print how many messages the person has.

dict_email = dict()
maximum = 0
maximum_email = ''
fname = input('> Give the file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    
    if words[1] not in dict_email:
        dict_email[words[1]] = 1    # First entry
    else:
        dict_email[words[1]] += 1   # Additional counts

for email in dict_email:
    if dict_email[email] > maximum:
        # Update the maximum if needed
        maximum = dict_email[email]
        # Store the email of maximum
        maximum_email = email
print(maximum_email, maximum)