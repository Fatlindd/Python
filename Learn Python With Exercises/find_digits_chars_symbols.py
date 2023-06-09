def find_digits_chars_symbols(string):
    count_chars = 0
    count_digits = 0
    count_symbols = 0
    for char in string:
        if char.isdigit():
            count_digits += 1
        elif char.isalpha():
            count_chars += 1
        else:
            count_symbols += 1
    return f'Chars: {count_chars}\nDigits: {count_digits}\nSymbols: {count_symbols}'

string = '$egExG12.;!@0e9fVjD-i43&*nrRGE3>2<.fG'
print(find_digits_chars_symbols(string))