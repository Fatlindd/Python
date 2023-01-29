
class BankAccount:
    print('!!! To Put Your Card In ATM Press 1 !!!')
    user_input = input('Enter card: ')

    def __init__(self, PIN):
        self.__balance = 1000
        self.pincode = PIN
    
    