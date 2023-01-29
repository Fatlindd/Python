import time
import sys, subprocess
class BankAccount:
    print('!!! To Put Your Card In ATM Press 1 !!!')
    user_input = input('Enter card: ')

    def __init__(self, PIN):
        self.__balance = 1000
        self.pincode = PIN
    
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

    
    def getBalance(self):
        print(f'Your balance: {self.__balance}€')
        option = input('Back to menu?(Y/N): ')
        if option.lower() != 'n':
            self.list()
        else:
            print('Thank You For Choosing Us!')
    
    def clearScreen(self):
        os = sys.platform
        if os == 'win32':
            subprocess.run('cls', shell=True)
