
# if the given string's length is at least 3 add 'ing'
# if the given string already ends with 'ing' add 'ly'
# if the given string is less than 3, leave it unchanged

def add_string(string):
    if len(string) > 2:
        if string[-3:] == 'ing':
            string += 'ly'
        else:
            string += 'ing'
    return string

print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))