def reverse_number(num):
    reverse = 0
    while num > 0:
        last_digit = num % 10
        reverse = reverse * 10 + last_digit
        num = num // 10
    return reverse

user_input = int(input('> Enter a number: '))
reverse = reverse_number(user_input)
print(f'Reverse of {user_input} is {reverse}.')