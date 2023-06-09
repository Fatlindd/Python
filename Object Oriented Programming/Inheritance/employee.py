# 👩🏻‍💻 Polymorphism and Inheritance 👩🏻‍💻
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def work(self):
        print(f'{self.name} is working...')
    
class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level
    
    def work(self):
        print(f'{self.name} is coding...')
    
    def debug(self):
        print(f'{self.name} is debbuging...')

class Designer(Employee):
    def work(self):
        print(f'{self.name} is designing...')
    
    def draw(self):
        print(f'{self.name} is drawing...')
    
se = SoftwareEngineer('Max', 25, 6000, 'Junior')
se.work()

d = Designer('Philipp', 27, 7000)
d.work()
