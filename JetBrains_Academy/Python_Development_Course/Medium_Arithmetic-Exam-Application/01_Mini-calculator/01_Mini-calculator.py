# write your code here
def get_params():
    num1, operator, num2 = input().split()
    return int(num1), int(num2), operator

def calculate(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2

print(calculate(*get_params()))
