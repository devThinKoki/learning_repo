import random


class Calculator:

    def __init__(self):
        self.a = 0
        self.b = 0
        self.sign = None
        self.result = 0

    def operation(self):
        if self.sign == '+':
            self.result = self.a + self.b
        elif self.sign == '-':
            self.result = self.a - self.b
        elif self.sign == '*':
            self.result = self.a * self.b

    def create_operation(self):
        type_operation = ['+', '-', '*']
        self.sign = random.choice(type_operation)
        self.a = random.randint(2, 9)
        self.b = random.randint(2, 9)
        print(f'{self.a} {self.sign} {self.b}')

    def compare_result(self):
        answer = int(input())
        if self.result == answer:
            print('Right!')
        else:
            print('Wrong!')

data_calc = Calculator()
data_calc.create_operation()
data_calc.operation()
data_calc.compare_result()