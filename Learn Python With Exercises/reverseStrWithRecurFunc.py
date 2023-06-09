def reverse_recur(string):
    if len(string) == 0:
        return string
    else:
        return reverse_recur(string[1:]) + string[0]

# user_input = 'Lindi'
user_input = input('> Give a string: ')
reverse = reverse_recur(user_input)
print(f'Reverse of {user_input} is {reverse}.')