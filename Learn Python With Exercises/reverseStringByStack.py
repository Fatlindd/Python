
def reverse_stack(string):
    stack = []
    for char in string:
        stack.append(char)
    
    # pop all characters of string and add it to the rev
    rev = ''
    while len(stack) > 0:
        last = stack.pop() # last element of list
        rev = rev + last
    return rev

# 👤
user_input = input('> What is your string: ')
reverse = reverse_stack(user_input) # 📞 calling function
print(f'Reverse of {user_input} is {reverse}.')