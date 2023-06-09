
class Phone:
    video_call = True
    def __init__(self, brand, price, network):
        self.brand = brand
        self.price = price
        self.network = network
    
    def recharge(self):
        print('Eating Electricity!')
        print('Electrons are Yummy!')

my_phone = Phone('Apple', 800, 'TMobile')
my_phone.recharge()

class Watch:
    def __init__(self, brand, price, has_gps):
        self.brand = brand
        self.price = price
        self.has_gps = has_gps
    
    def recharge(self):
        print('Eating Electricity!')
        print('Electrons are Yummy!')

my_watch = Watch('Fitbit', 200, False)
my_watch.recharge()

class SmartDevice:
    def recharge(self):
        print('Eating Electricity!')
        print('Electrons are Yummy!')
        