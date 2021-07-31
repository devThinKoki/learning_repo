import random
def random_generate():
    number_1, number_2 = random.randint(2,9), random.randint(2,9)
    operator = random.choice(['+', '-', '*'])
    print(str(number_1), operator, str(number_2))
    return number_1, number_2, operator

def calculate(x, y, op):
    operators = {
        '+': lambda a, b: a + b, 
        '-': lambda a,b: a - b,
        '*': lambda a, b: a * b
    }
    return operators[op](x, y)

def compare_result(numb_1, numb_2, operator):
    result =  calculate(numb_1, numb_2, operator)
    user = int(input())
    if user == result:
        print('Right!')
    else:
        print('Wrong!')

compare_result(*random_generate())