a, operator, b = input().split()

arithmetic = {"*": lambda x, y: x * y,
              "+": lambda x, y: x + y,
              "-": lambda x, y: x - y}

print(arithmetic[operator](int(a), int(b)))