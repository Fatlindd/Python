import random

def add(x, y):
    return  x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def main():
    print('\n▶ Simple Calculator App ◀')
    print("1️⃣  Calculate addition")
    print("2️⃣  Calculate subtraction")
    print("3️⃣  Calculate multiplication")
    print("4️⃣  Calculate dividing")
    print("5️⃣  Exit")

    option = input('〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰\nYour choice: ')
    while True:
        x = int(input('X: '))
        y = int(input('Y: '))
        if option == '1':
            print(f'Result: {x} + {y} = ', add(x, y), '\n')
        elif option == '2':
            print(f'Result: {x} - {y} = ', sub(x, y), '\n')
        elif option == '3':
            print(f'Result: {x} * {y} = ' ,mul(x, y), '\n')
        elif option == '4':
            print(f'Result: {x} / {y} = ', div(x, y), '\n')
        else: 
            print('⚠ Invalid operator!')
            exit()
        
        repeat = input('Do you want to change operator (y/n)? ')
        if repeat.lower() == 'y':
            main()

if __name__ == '__main__':
    main()