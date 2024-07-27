
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to {self.account_holder}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount} from {self.account_holder}'s account.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_balance(self):
        print(f"BankAccount({self.account_number}, {self.account_holder}, {self.balance})")

    def __str__(self):
        return f"BankAccount({self.account_number}, {self.account_holder}, {self.balance})"

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.01):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
        print(f"Applied interest to {self.account_holder}'s account. New balance: {self.balance}")

    def __str__(self):
        return f"SavingsAccount({self.account_number}, {self.account_holder}, {self.balance}, {self.interest_rate})"


class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=100.0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.account_holder}'s account. New balance: {self.balance}")
        else:
            print("Exceeded overdraft limit or invalid withdrawal amount.")

    def __str__(self):
        return f"CheckingAccount({self.account_number}, {self.account_holder}, {self.balance}, {self.overdraft_limit})"


def main():
    # Create a savings account
    savings = SavingsAccount("SA12345", "Alice", balance=1000.0, interest_rate=0.05)

    # Create a checking account
    checking = CheckingAccount("CA67890", "Bob", balance=500.0, overdraft_limit=200.0)

    # Perform operations on savings account
    savings.deposit(200.0)
    savings.withdraw(150.0)
    savings.check_balance()
    savings.apply_interest()

    # Perform operations on checking account
    checking.deposit(300.0)
    checking.withdraw(900.0)
    checking.check_balance()

    # Print account details
    print(savings)
    print(checking)


if __name__ == "__main__":
    main()