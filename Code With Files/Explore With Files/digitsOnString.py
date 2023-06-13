s1 = 'PYnative29@#8496'
countNumber = 0
sumNumbers = 0
for char in s1:
    if char.isdigit():
        sumNumbers += int(char)
        countNumber += 1

print('Sum of numbers: ', sumNumbers)
print(f'Average of digits: { sumNumbers // countNumber}')