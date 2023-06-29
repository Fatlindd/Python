class MoneyMachine:

    CURRENCY = "€"
    COIN_VALUES = {
        "cents": 0.01,
        "euros": 1,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0
    
    def report(self):
        """ Prints the current profit. """
        print(f"Money: {self.profit}{self.CURRENCY}")
    
    def process_coins(self):
        """ Returns the total calculated from coins inserted. """
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received
    
    def make_payment(self, cost):
        """ Returns True when payment is accepted, or False if insufficient. """
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {change}{self.CURRENCY} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
        