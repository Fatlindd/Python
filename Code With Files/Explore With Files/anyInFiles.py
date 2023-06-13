string = 'Emma25 is Data Scientist64 and AI Expert.'
print('The original string is: ' + string)

res = []
# split string by whitespaces
temp = string.split()

# words with both alphabets and numbers
# isdigit() for numbers + isalpha() for alphabets
# use any() to check each character

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)
    
print("Dispaying words with alphabets and numbers")
for i in res:
    print(i)
