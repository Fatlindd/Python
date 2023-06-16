
def count_value(data, value):
    count = 0
    for val in data.values():
        if val == value:
            count += 1
    return count
 
data = {'a': 1, 'b': 2, 'c': 2, 'd': 2}
value = 2
count = count_value(data, value)
print(f'The value {value} appears {count} times in the dictionary.')