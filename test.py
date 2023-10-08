

class Human:
    def __init__(self, name: str, age: int, work: str):
        self.name = name
        self.age = age
        self.work = work
        
    def __str__(self):
        return f'Это человек по имени {self.name}, ему {self.age} лет и он {self.work}'

talan = Human('Настя',30,'Студент')
varya = Human('Варя',8,'Ребенок')

print(talan)
print(varya)