# Car class 추상클래스 만들기
#     -attribute: 생성자에서 자동차 이름 설정
#     -method: info(self) -> 이름 출력
#     -abstract method: fuel(self)

# Electronic Car class
#     -attribute: 생성자에서 self.name 설정
#     -method: info(self) -> 이름 출력
#     -method: fuel(self) -> 사용연료(Electronic) 출력

from abc import *
class Car(metaclass=ABCMeta):
    def __init__(self, name = None):
        self.name = name
        return
    
    def get_info(self):
        print(self.name)
        return

    @abstractmethod
    def fuel(self):
        pass

class ElectronicCar(Car):
    def fuel(self):
        print('사용 연료: Electronic')

elec_car = ElectronicCar('koki')
elec_car.get_info()
elec_car.fuel()
