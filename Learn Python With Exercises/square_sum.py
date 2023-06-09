def square_sum(num):
    sum = 0
    for i in range(num + 1):
        squre = i ** 2
        sum += squre
        print(f'{i} ** 2 = {squre}')
    return sum

num = int(input('Enter a range number: '))
print('Sum: ', square_sum(num))