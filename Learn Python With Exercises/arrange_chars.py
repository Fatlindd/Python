
def arrange_chars(string):
    lower = []
    upper = []
    for char in string:
        if char.islower():
            lower.append(char)
        else:
            upper.append(char)
    
    return ''.join(lower + upper)

string = 'ahnsfWEFerlRXjdHsasjeIqQ'
print(arrange_chars(string))