# Car class 만들기
#   -attribute: 생성자에서 self.name 설정
#   -method: info(self)-> 이름을 출력

# Eletronic Car class
#   -attribute: 생성자에서 self.name 설정
#   -method[override]: info(self) -> 이름과 사용 연료(Eletronic) 출력

# Gasoline Car class
#   -attribute: 생성자에서 self.name 설정
#   -method[override]: info(self) -> 이름과 사용 연료(Gasoline) 출력


class Car:
    def __init__(self, name):
        self.name = name
    
    def get_info(self):
        print(self.name)
    
class Eletronic_Car(Car):
    def __init__(self, name):
        self.name = name
        self.Fuel = 'Eletronic'
    def get_info(self):
        print(self.name, self.Fuel)

class Gasoline_Car(Car):
    def __init__(self, name):
        self.name = name
        self.Fuel = 'Gasoline'
    def get_info(self):
        print(self.name, self.Fuel)

elec = Eletronic_Car('koki')
gaso = Gasoline_Car('tasaka')
print(elec.get_info(), gaso.get_info())
