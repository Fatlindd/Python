
class SmartDevice:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def recharge(self):
        print('Eating Electricity!')
        print('Electrons are Yummy!')
        

class Phone(SmartDevice):
    video_call = True
    def __init__(self, brand, price, network):
        super().__init__(brand, price)
        self.network = network

my_phone = Phone('Apple', 800, 'TMobile')
print(my_phone.price)
my_phone.recharge()

class Watch(SmartDevice):
    def __init__(self, brand, price, has_gps):
        SmartDevice.__init__(self, brand, price)
        self.steps_count = 0
        self.has_gps = has_gps

my_watch = Watch('Fitbit', 200, False)
print(my_watch.brand)
my_watch.recharge()

