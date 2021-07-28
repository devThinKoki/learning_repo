class calculator:
    def __init__(self, a, b, sign):
        self.a = int(a)
        self.b = int(b)
        self.sign = sign

    def operation(self):
        if self.sign == '+':
            return self.a + self.b
        if self.sign == '-':
            return self.a - self.b
        if self.sign == '*':
            return self.a * self.b


data = input().split(' ')
data_calc = calculator(data[0], data[2], data[1])
print(data_calc.operation())