
class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = 0
        self._num_bugs_solved = 0
    
    def code(self):
        self._num_bugs_solved += 1
    
    def get_salary(self):
        return self._salary

    def set_salary(self, base_value):
        self._salary = self._calculate_salary(base_value)
    
    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3
    
se = SoftwareEngineer('Max', 25)
print(se.name, se.age)

for i in range(70):
    se.code()

se.set_salary(5000)
print(se.get_salary())