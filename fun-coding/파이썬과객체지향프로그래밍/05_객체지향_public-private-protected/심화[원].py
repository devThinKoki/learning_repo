# 원 클래스 만들기
# - attribute: 원의 반지름, 원의 이름
# - method:
#       원 이름 리턴
#       원 넓이 리턴
#       원의 둘레의 길이 리턴
#   생성자에서만 attribute값 설정 가능
#   attribute는 private으로 설정

import math
class Circle:
    def __init__(self, radius, name):
        self.__radius = radius
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def get_area(self):
        return math.pow(self.__radius,2) * math.pi
    
    def get_length(self):
        return 2 * self.__radius * math.pi

circle = Circle(3, 'Koki')
print(circle.get_name(), circle.get_area(), circle.get_length())