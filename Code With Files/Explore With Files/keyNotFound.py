
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_update = ['a', 'c', 'f']

while keys_to_update:
    # pop() method is used to remove the last element from the list 
    # if no index is specified inside it. 
    key = keys_to_update.pop()
    if key in data:
        data[key] *= 2
    else:
        print(f'Key {key} not found!')
print(data)