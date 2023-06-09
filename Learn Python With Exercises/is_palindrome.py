def is_palindrome(string):
    for i in range(0, int(len(string) / 2)):
        if string[i] == string[len(string) - i - 1]:
            return True
    return False

print(is_palindrome('kapak'))

