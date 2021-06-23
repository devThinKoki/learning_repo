class Figure:
    def __init__(self, name, color):
        self.__name = name
        self.__color = color

class Quadrangle(Figure):
    def set_area(self, width, height):
        self.__width = width
        self.__height = height
    
    def get_info(self):
        print(self.name, self.color, self.__width * self.__height)
# 다음 세 코드가 실행된 후, 최종 값 예상해보고, 왜 이와 같이 작성하였는지 이해해보자(상속 개념에 대한 이해)
square = Quadrangle("square1", "black")
square.set_area(5,5)
square.get_info()
# 예상 결과값
# square1, black, 25