def is_balanced(s1, s2):
    is_balanced = True

    for char in s1:
        if char in s2:
            continue
        else:
            is_balanced = False
    return is_balanced

# s1 = 'xyza'
s1 = 'xyz'
s2 = 'dxhfyklzj'
print(is_balanced(s1, s2))