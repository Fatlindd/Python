from datetime import datetime
import time

def get_user_birthday():
    date_str = input('> Enter your birthday in DD/MM/YYYY: ')
    try:
        birthday = datetime.strptime(date_str, '%d/%m/%Y')
    except TypeError:
        birthday = datetime(*(time.strptime(date_str, '%d/%m/%Y')[0:6]))
    
    return birthday

def days_remaining(birth_date):
    now = datetime.now()
    current_year = datetime(now.year, birth_date.month, birth_date.day)
    days = (current_year - now).days
    if days < 0:
        next_year = datetime(now.year + 1, birth_date.month, birth_date.day)
        days = (next_year - now).days
    return days

def calculate_age(birth_date):
    today = datetime.today()
    days = (today - birth_date).days
    age = days // 365
    return age

birthday = ''
while True:
    print("1. Enter your birthday\n2. Calculate age\n3. Days reamining")
    answer = input('> Choose: ')
    
    if answer == '1':
        birthday = get_user_birthday()

    if birthday != '':
        if answer == '2':   
            age = calculate_age(birthday)
            print(f'Your age is {age}.')

        if answer == '3':
            days = days_remaining(birthday)
            print(f'Your next birthday is for {days} days.')
    else:
        print('First add your birthday!')