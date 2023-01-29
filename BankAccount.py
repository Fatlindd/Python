import time
import sys, subprocess
import maskpass

class BankAccount:
    print('!!! To Put Your Card In ATM Press 1 !!!')
    user_input = input('Enter card: ')

    def __init__(self, PIN):
        self.__balance = 1000
        self.pincode = PIN
    
    def login(self):
        if self.user_input == '1':
            print('Loading...', end= '\r')
            time.sleep(2)
            count = 3
            while count > 0:
                pin = input('Enter your 4 digits code: ')
                if pin == str(self.pincode):
                    print('Loading...', end= '\r')
                    time.sleep(2)
                    self.clearScreen()
                    self.list()
                    break
                else:
                    print('Your PIN Code is wrong! Try Again!')
                    count -= 1
            else:
                time.sleep(2)
                self.clearScreen()
                print('Your Accoung is blocked!')
        else:
            print('Your input is wrong!')
            while True:
                self.user_input = input('Enter a card: ')
                if self.user_input == '1':
                    self.login()
                else:
                    print('Your input is wrong!')

    def list(self):
        print('1. Get your Balance')
        print('2. Deposit Money')
        print('3. Change Password')
        print('4. Withdraw Money')

        choice = int(input('Your choice: '))
        if choice == 1:
            self.clearScreen()
            self.getBalance()
        elif choice == 2:
            self.clearScreen()
            self.deposit()
        elif choice == 3:
            self.clearScreen()
            self.changePassword()
        elif choice == 4:
            self.clearScreen()
            self.withdraw()

    def getBalance(self):
        print(f'Your balance: {self.__balance}€')
        option = input('Back to menu?(Y/N): ')
        if option.lower() != 'n':
            self.list()
        else:
            print('Thank You For Choosing Us!')
    
    def deposit(self):
        amount = int(input('Deposit money: '))
        self.__balance += amount
        print('________________________________')
        print(f'Bilance: {self.__balance - amount}€')
        print(f'Available: {self.__balance}€')

        print('________________________________')
        option = input('Back to menu?(Y/N): ')
        if option.lower() != 'n':
            self.clearScreen()
            self.list()
        else:
            print('Thank You For Choosing Us!')
    
    def changePassword(self):
        print('________________________________')
        print(f'Curren PIN Code: {self.pincode}')
        new_pin_code = input('New PIN Code: ')
        if len(new_pin_code) == 4:
            print('________________________________')
            time.sleep(2)
            self.clearScreen()
            print('Your password is updated!')
            self.pincode = int(new_pin_code)
            self.login()
        else:
            self.clearScreen()
            print('Your PIN Code must be 4 digits!')
            self.changePassword()
        
        print('________________________________')
        option = input('Back to menu?(Y/N): ')
        if option.lower() != 'n':
            self.clearScreen()
            self.list()
        else:
            print('Thank You For Choosing Us!')
    
    def withdraw(self):
        amount = int(input('Withdraw money: '))
        if self.__balance > amount:
            self.__balance = self.__balance - amount
            print(f'Your current balance: {self.__balance}€')
        else:
            print(f'In your current balance you have: {self.__balance}€')
            print('No more money for you!')
        
        option = input('Back to menu?(Y/N): ')
        if option.lower() != 'n':
            self.clearScreen()
            self.list()
        else:
            print('Thank You For Choosing Us!')
    
    def clearScreen(self):
        os = sys.platform
        if os == 'win32':
            subprocess.run('cls', shell=True)

my_account = BankAccount(1234)
my_account.login()