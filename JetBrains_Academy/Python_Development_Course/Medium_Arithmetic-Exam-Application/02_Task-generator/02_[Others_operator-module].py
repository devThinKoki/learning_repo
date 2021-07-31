import random
import operator
y = {'+':operator.add, '-':operator.sub, '*':operator.mul}
x = random.randint(2, 9)
z = random.randint(2, 9)
op = random.choice(list(y.keys()))
print(f'{x} {op} {z}')
user_result = int(input())
answer = y.get(op)(x, z)
if answer == user_result:
    print('Right!')
else:
    print('Wrong!')